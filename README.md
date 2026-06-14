## 🧩 System Architecture & Data Flow

```text
 📥 Raw PDF/Image Invoices
           │
           ▼
 🛠️ [Defensive Data Ingestion] ──> Extract Structural Text Metadata
                                               │
                                               ▼
 ✂️ [Token-Optimized Chunking] ──> Sliding-Window Character Segmentation
                                               │
                                               ▼
 🔍 [Context Conditioning Layer] ──> Inject Explicit Schema Boundaries (JSON)
                                               │
                                               ▼
 👥 [Human-in-the-Loop Audit] ──> Catch & Intercept Real-Time Drops
                                               │
                                               ▼
 💾 [Feedback Alignment Layer] ──> Compile Validated Ground-Truth Pairs
                                               │
                                               ▼
 🚀 [Immutable JSONL Stream] ──> Downstream LLM Parameter Fine-Tuning