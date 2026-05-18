# Phase 2 — Chunking Pipeline

Status: 🚧 Active

Goal:

Convert extracted PDF text into structured chunks
for downstream retrieval and vector storage.

Architecture:

PDF
↓
Upload
↓
Extract Text
↓
Chunk Service
↓
Structured Chunks

---

## Step 1 — Install Dependency

```bash
pip install langchain-text-splitters
```

Verify:

```bash
pip show langchain-text-splitters
```

---

## Step 2 — Create Service

Create:

src/services/chunk_service.py

```python
from langchain_text_splitters import RecursiveCharacterTextSplitter
import uuid


splitter = RecursiveCharacterTextSplitter(

    chunk_size=750,
    chunk_overlap=100

)


def create_chunks(
        text:str,
        metadata:dict
):

    docs = splitter.create_documents(
        [text]
    )

    chunks=[]

    for doc in docs:

        chunks.append({

            "chunk_id":
            str(uuid.uuid4()),

            "content":
            doc.page_content,

            "metadata":
            metadata

        })

    return chunks
```

---

## Step 3 — Modify Upload Route

Update:

src/api/upload.py

Add import:

```python
from src.services.chunk_service import create_chunks
```

Locate:

```python
pdf_data = extract_pdf_text(filepath)
```

Add below:

```python
metadata = {

    "filename":
    file.filename,

    "pages":
    pdf_data["pages"]

}


chunks = create_chunks(

    pdf_data["text"],
    metadata

)
```

Replace response with:

```python
return {

    "success":True,

    "filename":
    file.filename,

    "saved_as":
    filepath,

    "pages":
    pdf_data["pages"],

    "characters":
    pdf_data["characters"],

    "chunks":
    len(chunks),

    "sample_chunk":
    chunks[0]["content"][:300]

}
```

---

## Step 4 — Test

Run:

```bash
python -m uvicorn src.api.main:app --reload
```

Open:

http://127.0.0.1:8000/docs

Upload:

sample.pdf

Expected:

```json
{

"success":true,

"filename":"resume.pdf",

"pages":2,

"characters":3939,

"chunks":8,

"sample_chunk":"Sriharsha..."

}
```

---

## Step 5 — Validate Chunk Quality

Inspect:

- chunk count
- chunk overlap
- chunk boundaries
- sentence continuity

Experiment:

chunk_size:

- 500
- 750
- 1000

chunk_overlap:

- 50
- 100
- 200

Current default:

```python
chunk_size=750
chunk_overlap=100
```

Do NOT over-optimize now.

---

## Step 6 — Commit

```bash
git add .

git commit -m "complete phase 2 chunking pipeline"
```

---

Success Condition:

PDF
↓
Upload
↓
Extract
↓
Chunk
↓
Structured chunks available

Next:

Phase 3 → Embedding Pipeline