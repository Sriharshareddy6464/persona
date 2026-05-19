# Phase 3 — Embedding Pipeline

Status: DONE

Goal:

Convert text chunks into vector embeddings using local models.

Architecture:

PDF
↓
Upload
↓
Extract
↓
Chunk
↓
Embedding Service
↓
Vectors

---

## Step 1 — Install Dependencies

```bash
pip install sentence-transformers
pip install langchain-huggingface
```

Verify:

```bash
pip show sentence-transformers
```

---

## Step 2 — Create Service

Create:

src/services/embedding_service.py

```python
from langchain_huggingface import HuggingFaceEmbeddings


embedding_model = HuggingFaceEmbeddings(

    model_name=
    "sentence-transformers/all-MiniLM-L6-v2"

)


def generate_embeddings(
        text:str
):

    vector = embedding_model.embed_query(
        text
    )

    return vector
```

---

## Step 3 — Update upload.py

Add import:

```python
from src.services.embedding_service import generate_embeddings
```

After:

```python
chunks=create_chunks(...)
```

Add:

```python
sample_vector = generate_embeddings(

    chunks[0]["content"]

)
```

---

## Step 4 — Update Response

Add:

```python
"embedding_dimension":
len(sample_vector),

"embedding_preview":
sample_vector[:5]
```

Response becomes:

```python
return {

    "success":True,

    "pages":
    pdf_data["pages"],

    "characters":
    pdf_data["characters"],

    "chunks":
    len(chunks),

    "embedding_dimension":
    len(sample_vector),

    "embedding_preview":
    sample_vector[:5]

}
```

---

## Step 5 — Run

```bash
python -m uvicorn src.api.main:app --reload
```

Upload PDF.

Expected:

```json
{
"chunks":6,
"embedding_dimension":384,
"embedding_preview":[0.02,-0.11,...]
}
```

---

## Validation

Check:

- embeddings generated
- vector length consistent
- no crashes
- dimensions remain fixed

Expected:

MiniLM

384 dimensions

---

## Commit

```bash
git add .

git commit -m "complete phase 3 embedding pipeline"
```

Success:

PDF
↓
Extract
↓
Chunk
↓
Embedding
↓
Vector generated

Next:

Phase 4 → ChromaDB