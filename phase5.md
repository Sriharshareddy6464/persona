# Phase 5 — Retrieval Layer

Status: 🚧 Active

Goal:

Convert user questions into embeddings,
search stored vectors,
and retrieve relevant chunks.

Architecture:

User Query
↓
Generate Query Embedding
↓
ChromaDB Search
↓
Top K Retrieval
↓
Relevant Chunks Returned

---

## Step 1 — Create Retrieval Service

Create:

src/services/retrieval_service.py

```python
import chromadb

from src.services.embedding_service import (
    generate_embeddings
)


client = chromadb.PersistentClient(
    path="./chroma_db"
)

collection = client.get_collection(
    "persona_documents"
)


def retrieve_documents(
        query:str,
        top_k:int=5
):

    query_embedding = generate_embeddings(
        query
    )

    results = collection.query(

        query_embeddings=[

            query_embedding

        ],

        n_results=top_k

    )

    return results
```

---

## Step 2 — Create Query API

Create:

src/api/query.py

```python
from fastapi import APIRouter

from src.services.retrieval_service import (
    retrieve_documents
)


router = APIRouter()


@router.get("/query")

def query_documents(
        q:str
):

    results = retrieve_documents(
        q
    )

    return {

        "query":q,

        "results":

        results["documents"][0]

    }
```

---

## Step 3 — Register Router

Open:

src/api/main.py

Current:

```python
from fastapi import FastAPI
from src.api.upload import router
```

Update:

```python
from fastapi import FastAPI

from src.api.upload import router

from src.api.query import (
    router as query_router
)


app=FastAPI()

app.include_router(
    router
)

app.include_router(
    query_router
)


@app.get("/")

def root():

    return {

        "message":
        "Persona API running"

    }
```

---

## Step 4 — Run Server

```bash
python -m uvicorn src.api.main:app --reload
```

Open:

http://127.0.0.1:8000/docs

You should now see:

GET

/query

---

## Step 5 — Test Retrieval

Example:

```txt
What cloud technologies are used?
```

or:

```txt
What is infrastructure automation?
```

or:

```txt
What skills does Sriharsha have?
```

Expected:

```json
{

"query":
"What cloud technologies are used?",

"results":[

"...retrieved chunk...",

"...retrieved chunk..."

]

}
```

---

## Step 6 — Validation

Check:

- retrieval works
- top_k returns multiple chunks
- relevant chunks returned
- no crashes
- Chroma persistence survives restart

---

## Step 7 — Experiment

Modify:

```python
top_k=5
```

Try:

```python
top_k=3
top_k=8
top_k=10
```

Observe quality.

---

## Step 8 — Commit

```bash
git add .

git commit -m "complete phase 5 retrieval pipeline"
```

Success:

User Query
↓
Embedding
↓
Vector Search
↓
Retrieved Context

Next:

Phase 6 → Response Generation Layer