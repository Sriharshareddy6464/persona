# Phase 4 — Vector Storage Pipeline

Status: DONE

Goal:

Store embeddings and metadata
inside ChromaDB.

Architecture:

PDF
↓
Upload
↓
Extract
↓
Chunk
↓
Embedding
↓
ChromaDB

---

## Step 1 — Install

```bash
pip install chromadb
```

---

## Step 2 — Create Service

Create:

src/services/vector_service.py

```python
import chromadb


client = chromadb.PersistentClient(
    path="./chroma_db"
)


collection = client.get_or_create_collection(
    name="persona_documents"
)


def store_chunks(
        chunks,
        vectors
):

    ids=[]

    docs=[]

    embeddings=[]

    metadatas=[]


    for chunk,vector in zip(
            chunks,
            vectors
    ):

        ids.append(
            chunk["chunk_id"]
        )

        docs.append(
            chunk["content"]
        )

        embeddings.append(
            vector
        )

        metadatas.append(
            chunk["metadata"]
        )


    collection.add(

        ids=ids,

        documents=docs,

        embeddings=embeddings,

        metadatas=metadatas

    )
```

---

## Step 3 — Create Batch Embeddings

Update:

embedding_service.py

Add:

```python
def generate_batch_embeddings(
        chunks
):

    vectors=[]

    for chunk in chunks:

        vector=embedding_model.embed_query(

            chunk["content"]

        )

        vectors.append(
            vector
        )

    return vectors
```

---

## Step 4 — Update upload.py

Add imports:

```python
from src.services.vector_service import store_chunks

from src.services.embedding_service import generate_batch_embeddings
```

After:

```python
chunks=create_chunks(...)
```

Add:

```python
vectors=generate_batch_embeddings(
    chunks
)

store_chunks(
    chunks,
    vectors
)
```

---

## Response

Add:

```python
"stored_vectors":
len(vectors)
```

Expected:

```json
{
"chunks":6,
"stored_vectors":6
}
```

---

## Verify

Open folder:

```txt
persona/

chroma_db/
```

Should appear.

Persistence means:

restart server

data still exists

---

## Commit

```bash
git add .

git commit -m "complete phase 4 vector storage pipeline"
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
Store