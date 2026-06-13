import os
import json
import pytest
from unittest.mock import patch
from invoice_llm.pipeline import InvoiceParserRAGPipeline
from invoice_llm.exceptions import DocumentIngestionError, LLMInferenceError, FeedbackLoggingError

@pytest.fixture
def clean_pipeline(tmp_path):
    """Generates an isolated pipeline instance with localized test path structures."""
    lake_dir = tmp_path / "data_lake_cache"
    feedback_file = tmp_path / "feedback_stream.jsonl"
    return InvoiceParserRAGPipeline(lake_directory=str(lake_dir), training_path=str(feedback_file))

def test_ingest_document_valid_payload(clean_pipeline):
    text_data = "FINMATICS INVOICE REVENUE RECORD ROW METRICS #2026-X94 IBAN DE445001"
    processed_count = clean_pipeline.ingest_and_index_document("doc_99", text_data)
    
    assert processed_count > 0
    assert len(clean_pipeline.vector_db_registry) == processed_count
    assert os.path.exists(os.path.join(clean_pipeline.lake_directory, "doc_99.txt"))

@pytest.mark.parametrize("bad_id, bad_text", [
    ("", "Valid text layer string variables"),
    ("doc_10", ""),
    ("doc_11", "    "),
    (None, "Valid text"),
])
def test_ingest_document_validation_exceptions(clean_pipeline, bad_id, bad_text):
    with pytest.raises(DocumentIngestionError, match="Payload content or file identification"):
        clean_pipeline.ingest_and_index_document(bad_id, bad_text)

def test_generate_few_shot_prompt_formatting(clean_pipeline):
    prompt = clean_pipeline.generate_few_shot_prompt("Target tracking search string payload")
    assert "FEW-SHOT CONTROLS" in prompt
    assert "CONSTRAINT SPECIFICATION SCHEMA" in prompt

@pytest.mark.parametrize("bad_context", [None, "", "   "])
def test_generate_few_shot_prompt_empty_exception(clean_pipeline, bad_context):
    with pytest.raises(LLMInferenceError, match="Cannot compile context configurations"):
        clean_pipeline.generate_few_shot_prompt(bad_context)

def test_log_human_feedback_persistence(clean_pipeline):
    raw_ctx = "Context parameter text fields"
    m_out = {"invoice_id": "1", "gross_amount": 100.0}
    corrections = {"gross_amount": 119.00}
    
    line_out = clean_pipeline.log_human_feedback(raw_ctx, m_out, corrections)
    
    assert os.path.exists(clean_pipeline.training_path)
    parsed_json = json.loads(line_out)
    assert parsed_json["metadata"]["requires_parameter_tuning"] is True
    
    with open(clean_pipeline.training_path, "r", encoding="utf-8") as f:
        file_lines = f.readlines()
    assert len(file_lines) == 1

@pytest.mark.parametrize("ctx, model_out", [
    (None, {"valid": "dict"}),
    ("Valid context", None),
])
def test_log_human_feedback_validation_exceptions(clean_pipeline, ctx, model_out):
    with pytest.raises(FeedbackLoggingError, match="Logging event aborted"):
        clean_pipeline.log_human_feedback(ctx, model_out, {})

# ==============================================================================
# 🎯 MOCK INJECTIONS FOR 100% SYSTEM EXCEPTION COVERAGE
# ==============================================================================

def test_pipeline_initialization_system_failure():
    """Forces os.makedirs to fail to trigger initialization exception catch blocks."""
    with patch("os.makedirs") as mock_makedirs:
        mock_makedirs.side_effect = PermissionError("Write access denied")
        with pytest.raises(DocumentIngestionError, match="Failed to initialize data lake"):
            InvoiceParserRAGPipeline(lake_directory="/unauthorized_path")

def test_ingest_document_unexpected_system_error(clean_pipeline):
    """Forces the built-in open() call to fail to trigger generic exception wrappers."""
    with patch("builtins.open") as mock_open:
        mock_open.side_effect = RuntimeError("Disk partition corruption")
        with pytest.raises(DocumentIngestionError, match="System exception error encountered"):
            clean_pipeline.ingest_and_index_document("doc_crash", "Valid invoice text payload")

def test_log_human_feedback_write_failure(clean_pipeline):
    """Forces file appending to fail to trigger feedback logging error catch blocks."""
    raw_ctx = "Valid Context"
    m_out = {"invoice_id": "1"}
    
    with patch("builtins.open") as mock_open:
        mock_open.side_effect = IOError("Storage media disconnected")
        with pytest.raises(FeedbackLoggingError, match="Persistent logging task caught critical file write failure"):
            clean_pipeline.log_human_feedback(raw_ctx, m_out, {})