# Persona — Production RAG System
Status: 🚧 In Development

Goal:
Build a production-oriented retrieval system focused on deployment,
observability, reliability, and AI infrastructure practices.

Architecture V1

PDF
↓
Chunking
↓
Embeddings
↓
ChromaDB
↓
Retriever
↓
FastAPI
↓
Response API

---

# Phase 0 — Foundation ✅

## Repository Setup

- [x] Initialize repository
- [x] Create project structure
- [x] Create .gitignore
- [x] Create .env.example
- [x] Setup virtual environment
- [x] Setup requirements.txt
- [x] Create README
- [x] Create docs folder
- [x] Create monitoring folder
- [x] Create docker folder
- [x] Create tests folder
- [x] Initial commit

Structure:

persona/

src/
ingestion.py
retrieval.py
embeddings.py
api.py
config.py

docs/
monitoring/
docker/
tests/

---

# Phase 1 — Data Ingestion Pipeline

Goal:
Accept PDF files and prepare documents.

Tasks:

- [ ] Create upload endpoint
- [ ] Add PDF validation
- [ ] Add file size limits
- [ ] Add upload folder structure
- [ ] Extract PDF text
- [ ] Handle extraction failures
- [ ] Add document metadata
- [ ] Add logging

Test:

- [ ] Upload PDF
- [ ] Verify extraction

Output:

PDF
↓
raw text

---

# Phase 2 — Chunking Pipeline

Goal:
Split documents efficiently.

Tasks:

- [ ] Add recursive text splitter
- [ ] Experiment chunk sizes
- [ ] Experiment overlap values
- [ ] Store metadata
- [ ] Add chunk identifiers
- [ ] Create chunk service

Test:

- [ ] Verify chunk count
- [ ] Verify overlap behavior

Output:

raw text
↓
chunks

---

# Phase 3 — Embedding Pipeline

Goal:
Convert chunks into vectors.

Tasks:

- [ ] Install sentence-transformers
- [ ] Add local embeddings
- [ ] Configure embedding service
- [ ] Add embedding cache
- [ ] Handle failures
- [ ] Add logging

Model:

all-MiniLM-L6-v2

Test:

- [ ] Generate embeddings
- [ ] Verify vector dimensions

Output:

chunks
↓
embeddings

---

# Phase 4 — Vector Database

Goal:
Store and retrieve embeddings.

Tasks:

- [ ] Setup ChromaDB
- [ ] Create collections
- [ ] Store vectors
- [ ] Store metadata
- [ ] Add retrieval service
- [ ] Add persistence

Test:

- [ ] Query stored vectors
- [ ] Restart application
- [ ] Verify persistence

Output:

query
↓
retrieved chunks

---

# Phase 5 — Retrieval Layer

Goal:
Create retrieval workflow.

Tasks:

- [ ] Build retriever
- [ ] Add top-k search
- [ ] Experiment k values
- [ ] Add metadata filtering
- [ ] Add similarity scoring

Future:

- [ ] BM25
- [ ] Hybrid retrieval
- [ ] reranking

Test:

- [ ] Verify relevant results

---

# Phase 6 — API Layer

Goal:
Expose system through FastAPI.

Tasks:

- [ ] Create /upload
- [ ] Create /query
- [ ] Create /health
- [ ] Add request schemas
- [ ] Add response schemas
- [ ] Add error handling

Test:

- [ ] Swagger works
- [ ] Upload works
- [ ] Query works

---

# Phase 7 — Dockerization

Goal:
Containerize system.

Tasks:

- [ ] Create Dockerfile
- [ ] Create docker-compose
- [ ] Add environment variables
- [ ] Verify container startup

Test:

- [ ] docker compose up

---

# Phase 8 — Redis Integration

Goal:
Improve performance.

Tasks:

- [ ] Setup Redis
- [ ] Add response cache
- [ ] Add query cache
- [ ] Add TTL
- [ ] Cache invalidation

Test:

- [ ] Verify cache hits

---

# Phase 9 — Reliability Layer

Goal:
Introduce production concepts.

Tasks:

- [ ] Rate limiting
- [ ] Retry logic
- [ ] Request timeout
- [ ] Structured logging
- [ ] Health checks

Future:

- [ ] Queue support
- [ ] Dead letter queue
- [ ] Circuit breakers

---

# Phase 10 — Observability

Goal:
Monitor behavior.

Tasks:

- [ ] Prometheus metrics
- [ ] Grafana dashboards
- [ ] Request metrics
- [ ] Latency metrics
- [ ] Error metrics

Test:

- [ ] Metrics visible

---

# Phase 11 — CI/CD

Goal:
Automated workflows.

Tasks:

- [ ] Add GitHub Actions
- [ ] Run tests
- [ ] Lint checks
- [ ] Docker build validation

---

# Phase 12 — Deployment

Goal:
Public deployment

Tasks:

- [ ] EC2 deployment
- [ ] Docker deployment
- [ ] Nginx reverse proxy
- [ ] SSL
- [ ] Domain setup

---

# Phase 13 — Documentation

Tasks:

- [ ] Architecture diagram
- [ ] Screenshots
- [ ] API examples
- [ ] Deployment guide
- [ ] Lessons learned
- [ ] Future roadmap
- [ ] Loom walkthrough

---

Ship Rule:

Do not jump phases.

Finish:
Build
↓
Test
↓
Commit
↓
Document

then move.