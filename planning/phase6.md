# Phase 6 — Response Generation Layer

Goal:

Convert retrieved chunks into useful answers.

Current:

Question
↓
Raw chunks

Target:

Question
↓
Retrieve
↓
Prompt
↓
LLM
↓
Answer

---

Install

```bash
pip install ollama
```

Install local model:

```bash
ollama pull llama3
```

Run:

```bash
ollama serve
```

---

Create:

src/services/generation_service.py

```python
import ollama


def generate_response(
        question:str,
        context:list
):

    combined_context = "\n\n".join(
        context
    )


    prompt = f"""

Answer ONLY from context.

Question:
{question}

Context:
{combined_context}

If answer unavailable,
say information not found.

"""


    response = ollama.chat(

        model="llama3",

        messages=[

            {

                "role":"user",

                "content":prompt

            }

        ]

    )


    return response["message"]["content"]
```

---

Update:

query.py

Add:

```python
from src.services.generation_service import (
    generate_response
)
```

Replace return:

```python
answer = generate_response(

    q,
    results["documents"][0]

)

return {

    "query":q,

    "source":filename,

    "answer":answer

}
```

---

Test:

"What skills does Sriharsha have?"

Expected:

Skills:
- Python
- AWS
- Docker
- Kubernetes
- FastAPI

instead of giant chunk dump