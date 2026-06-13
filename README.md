
# Automated Invoice Ledger Parser & LLM Fine-Tuning Pipeline

An enterprise-grade, object-oriented data science pipeline engineered to automate structural metadata extraction from highly unstructured accounting layouts (invoice images, digitizations, and raw text ledgers). This framework integrates a Retrieval-Augmented Generation (RAG) extraction workflow with an asynchronous, defensive human-in-the-loop auditing layer to programmatically construct validated training datasets for local LLM parameter fine-tuning.

## 📐 Production Framework Architecture

1. **Defensive Data Ingestion Layer** : Consolidates multi-source text inputs into an isolated local data lake tracking layer. Implements token-optimized character sliding-window chunk division rules to structure text payloads for vectorized indexing coordinates.
2. **Dynamic In-Context Conditioning Layer** : Generates high-fidelity few-shot training contexts fortified with explicit schema boundaries to guarantee zero-leakage structural formatting (JSON) outputs from open-source foundational models.
3. **Automated Feedback Alignment Layer** : Implements decoupled custom exception handlers and error classes to safely intercept real-time schema adjustments, appending verified ground-truth matrix coordinates directly to an immutable JSONL training stream.

## 🚀 Local Installation & Deployment

### 1. Verification of Workspace Isolation

Ensure an active Python environment matching development benchmarks (Python 3.11 or higher) is initialized on your machine:

python --version

### 2. Dependency Resolution Ingestion

Clone the repository path, instantiate your localized parameters, and download the development ecosystem packages inside your active workspace context:

git clone [https://github.com/thanhan25/invoice-llm-pipeline.git](https://www.google.com/search?q=https://github.com/thanhan25/invoice-llm-pipeline.git)

cd invoice-llm-pipeline

cp .env.example .env

pip install -e ".[dev]"

### 3. Executing Core Execution Traces

Execute the internal pipeline orchestration file directly to verify data logging operations:

python src/invoice_llm/pipeline.py

## 🧪 Quality Assurance Gates & PyTest Coverage

The codebase enforces full type-safety alignment and styling rules. Verification check arrays are evaluated via automated PyTest suites running mock-patched storage network drops. To execute the linting rules and check code coverage thresholds locally, run the terminal commands below:

# 1. Formatting alignments

python -m isort src tests

python -m black src tests

# 2. Syntax compliance validation

python -m flake8 src tests

# 3. Test matrix validation checks (Enforces a 90% coverage limit)

python -m pytest

## 🔖 Semantic Version Release Roadmap

This project tracks architectural shifts matching strict Semantic Versioning (vMAJOR.MINOR.PATCH) release guidelines:

* **v1.0.0 (Production Master Freeze)** : Baseline release featuring pyproject.toml packaging, custom domain exceptions, structured asynchronous-ready log streams, and 96.83% unit test coverage verification metrics.
