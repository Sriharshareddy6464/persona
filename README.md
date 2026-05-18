# Persona — Customisable Production RAG Application

AI-powered retrieval and resume intelligence system built to transform static documents into contextual, searchable knowledge.

Persona starts as a production-oriented Retrieval-Augmented Generation (RAG) application and evolves toward Resume + Job Description intelligence, skill-gap analysis, interview preparation, and AI-assisted career workflows.

---

## Problem

Most resume tools are static.

Users upload a resume and receive:

- ATS scores
- keyword suggestions
- generic recommendations

These systems lack contextual understanding.

They cannot answer:

- What skills am I actually missing?
- Am I suitable for this role?
- Which projects improve my profile?
- What should I prepare for interviews?
- What should I learn next?

Information becomes trapped inside documents.

Persona converts documents into a searchable knowledge system using Retrieval-Augmented Generation.

Instead of:

```text
Open PDF
↓
Search manually
↓
Read everything
```

Persona enables:

```text
Upload
↓
Ask
↓
Retrieve
↓
Generate
```

---

## Architecture

```text
Resume PDF
      ↓

FastAPI Upload API
      ↓

PDF Extraction Layer
      ↓

Chunking Pipeline
      ↓

Embedding Generation
(nomic-embed-text)

      ↓

Vector Database
(ChromaDB)

      ↓

Semantic Retrieval
      ↓

LLM Generation
(llama3 via Ollama)

      ↓

Answer Generation
```

Current implementation runs locally.

Advantages:

- No OpenAI dependency
- No API cost
- Full privacy
- Customizable pipeline
- Local inference

---

## Milestones

### v1.0 — Local Resume RAG MVP

Status: Released

Completed:

- PDF upload endpoint
- PDF extraction pipeline
- text chunking
- embedding generation
- vector database integration
- semantic retrieval
- local LLM integration
- document-aware retrieval
- question-answering endpoint

Flow:

```text
PDF
↓
Chunk
↓
Embed
↓
Store
↓
Retrieve
↓
Generate
```

---

### v2.0 — Resume + JD Intelligence

Planned

Inputs:

- Resume (.pdf)
- Job Description

Outputs:

- Match score
- JD-aware retrieval
- skill gap analysis
- recommendations
- session memory

---

### v3.0 — Resume Optimization Layer

Planned

Features:

- adaptive resume generation
- ATS optimization
- role-specific tailoring
- cover letter generation

Logic:

Resume generation activates only above score threshold.

---

### v4.0 — Career Intelligence Layer

Planned

Features:

- interview preparation
- company research
- market analysis
- learning recommendations
- project suggestions

---

## Tech Stack

| Layer | Technology |
|---|---|
| Backend | FastAPI |
| Language | Python |
| LLM Runtime | Ollama |
| LLM | llama3 |
| Embedding Model | nomic-embed-text |
| Vector Database | ChromaDB |
| PDF Processing | PyMuPDF |
| AI Pipeline | RAG |
| Storage | Persistent Chroma Storage |
| Server | Uvicorn |

---

## Current Status

Current MVP supports:

✅ Upload PDF

✅ Extract text

✅ Generate chunks

✅ Generate embeddings

✅ Store vectors

✅ Semantic retrieval

✅ Ask questions

✅ Local LLM answer generation

---

Current limitations:

- filename handling still basic
- retrieval ranking needs tuning
- no JD support
- no session memory
- no structured outputs
- no persistent user memory

---

## Future Improvements

### Resume + JD Intelligence

- automatic skill extraction
- role fit analysis
- match scoring
- missing skill detection

---

### Resume Optimization

- adaptive resumes
- ATS optimization
- role-specific resume tailoring

---

### Interview Assistant

- interview preparation
- expected questions
- answer recommendations

---

### Company Intelligence

- company research
- hiring trends
- market analysis

---

### Infrastructure

- Redis caching
- session management
- async pipelines
- Docker deployment
- observability
- monitoring
- cloud deployment

---

## Local Setup

Clone repository:

```bash
git clone <repo-url>

cd persona
```

Create virtual environment:

```bash
python -m venv venv
```

Activate:

Windows:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Start Ollama:

```bash
ollama run llama3
```

Run application:

```bash
python -m uvicorn src.api.main:app --reload
```

Open Swagger:

```txt
http://127.0.0.1:8000/docs
```

---

## Vision

Building systems beyond static AI tools.

Toward deployable, customizable, production-oriented AI infrastructure systems.