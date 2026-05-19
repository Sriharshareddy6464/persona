# Persona v2 — Phase 1

Status: 🚧 Active

Goal:

Introduce session memory.

Store latest uploaded resume automatically.

---

## Step 1

Create:

src/core/session_store.py

```python
current_session = {

    "resume":None,

    "jd":None

}


def set_resume(
        filename:str
):

    current_session[
        "resume"
    ]=filename


def get_resume():

    return current_session[
        "resume"
    ]


def set_jd(
        jd:str
):

    current_session[
        "jd"
    ]=jd


def get_jd():

    return current_session[
        "jd"
    ]
```

---

## Step 2

Open:

upload.py

Import:

```python
from src.core.session_store import (
    set_resume
)
```

Locate:

```python
metadata = {

    "filename":
    file.filename.lower().strip(),

    "pages":
    pdf_data["pages"]

}
```

Below add:

```python
set_resume(

    file.filename.lower().strip()

)
```

Meaning:

Every upload automatically updates session.

---

## Step 3

Open:

query.py

Import:

```python
from src.core.session_store import (
    get_resume
)
```

Current:

```python
def query_documents(

        q:str,

        filename:str=None

)
```

Replace:

```python
def query_documents(

        q:str,

        filename:str=None

):


    if filename is None:

        filename=get_resume()
```

Now:

If user gives filename:

use it

Else:

auto use latest uploaded resume

---

## Step 4

Improve response:

Add:

```python
return{

    "query":q,

    "active_resume":
    filename,

    "answer":
    answer

}
```

---

## Step 5

Run:

```bash
python -m uvicorn src.api.main:app --reload
```

---

## Step 6

Test:

Upload:

resume.pdf

Then:

GET

/query

q:

What skills does Sriharsha have?

Leave:

filename empty

Expected:

Works automatically

---

## Step 7

Commit

```bash
git add .

git commit -m "add session memory for active resume"
```

Success:

Upload
↓
remember file
↓
query directly