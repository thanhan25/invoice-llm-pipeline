
# Invoice LLM Intelligence & Fine-Tuning Pipeline 📑

[![Continuous Integration Quality Gate](https://github.com/thanhan25/invoice-llm-pipeline/actions/workflows/ci.yml/badge.svg)](https://github.com/thanhan25/invoice-llm-pipeline/actions)
![Python Version](https://img.shields.io/badge/python-3.11%20%7C%203.12-blue.svg)
![Build Status](https://img.shields.io/badge/quality__gate-passed-green.svg)

A production-grade data ingestion and context-conditioning pipeline engineered to transform unstructured multi-format corporate invoices (PDFs, TIFFs, Scans) into deterministic, schema-validated JSON data structures. This system integrates token-optimized sliding-window text chunking, defensive JSON validation schema layers, and an automated curation pipeline to stream high-fidelity ground-truth training pairs (JSONL) for targeted downstream LLM fine-tuning.

## 🏗️ System Architecture & Data Flow

```text
 📥 Raw PDF/Image Invoices
           │
           ▼
 🛠️ [Defensive Ingestion Layer] ──> Extract Structural Text Metadata
                                               │
                                               ▼
 ✂️ [Token-Optimized Chunking]  ──> Sliding-Window Character Segmentation
                                               │
                                               ▼
 🔍 [Context Conditioning Layer]──> Inject Explicit Target Schemas (JSON)
                                               │
                                               ▼
 👥 [Human-in-the-Loop Audit]   ──> Intercept Low-Confidence Drops
                                               │
                                               ▼
 💾 [Feedback Alignment Store]  ──> Compile Validated Ground-Truth Pairs
                                               │
                                               ▼
 🚀 [Immutable JSONL Stream]    ──> Downstream LLM Parameter Fine-Tuning
```

## 🧠 Architecture Design & Quality Standards

- **PEP 517 Distribution Foundations:** Packaged using standard isolated distribution schemas (`pyproject.toml` utilizing declarative `setuptools` find maps) to ensure deterministic environments across production environments.
- **Token-Constrained Chunking Matrices:** Implements token-aware sliding window splitting mechanics to eliminate context window clipping and preserve layout-dependent table relations.
- **Decoupled Error Domains:** Utilizes dedicated structural exception models to trap extraction failures and schema anomalies without resorting to fragile string-matching blocks.
- **Automated Curation Pipelines:** Filters, cleans, and packages conversational prompt-response elements into production-ready `.jsonl` files optimized for Supervised Fine-Tuning (SFT).
- **Continuous Integration (CI):** Backed by an active GitHub Actions workflow validating rigorous code quality layouts (`black`, `isort`) and running testing matrices on every push.

## 📦 Core Package Map

```text
invoice-llm-pipeline/
│
├── .github/workflows/
│   └── ci.yml               # Multi-version continuous integration workflow runner
│
├── src/invoice_pipeline/
│   ├── __init__.py          # Package identification namespace hook
│   ├── app.py               # Document processing CLI engine entrypoint
│   ├── config.py            # Central environment variable validation vault
│   ├── extractors.py        # Token-optimized text parsing arrays
│   ├── models.py            # Schema definitions & LLM interface engines
│   └── exceptions.py        # Independent pipeline domain error types
│
├── tests/
│   └── test_ingestion.py    # Sandbox ingestion logic verification tests
│
└── pyproject.toml           # Unified metadata manifest and package rules
```

## 🚀 Installation & Environment Setup

Isolate your system dependencies and install the parsing engine package in editable development mode:

```bash
# Clone the open-source tracking repository assets
git clone [https://github.com/thanhan25/invoice-llm-pipeline.git](https://github.com/thanhan25/invoice-llm-pipeline.git)
cd invoice-llm-pipeline

# Sync package metadata structures along with quality tracking tools
python -m pip install -e .[dev]
```

## 🏃‍♂️ Running the Testing Framework Locally

Evaluate your local pipeline transformations and schema validation checks against automated coverage targets:

```bash
python -m pytest
```

## 📊 Operating the Processing Interface

Ingest raw unstructured documents, validate extraction schemas, and output synchronized fine-tuning records:

```bash
# 1. Parse a target directory of unstructured invoice documents
python src/invoice_pipeline/app.py --source data/raw_invoices/

# 2. Compile and stream validated ground-truth records to training targets
python src/invoice_pipeline/app.py --compile-training --output data/fine_tune_ready.jsonl
```
