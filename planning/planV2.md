# Persona v2 — Resume + JD Intelligence

Status: 🚧 Active

Goal:

Transform Persona from local RAG assistant into
resume + job-description intelligence system.

Inputs:

- Resume (.pdf)
- Job Description (text)

Outputs:

- Match score
- Missing skills
- Recommendations
- Combined querying

Architecture:

Resume PDF
        +
JD Text
        ↓

PDF Processing
        ↓

Resume Retrieval
        ↓

JD Extraction
        ↓

Skill Extraction
        ↓

Match Engine
        ↓

Recommendations
        ↓

Answer Layer

---

# Phase 1 — Session Memory

Problem:

Current:

query
↓
filename required

Bad UX

Goal:

Remember current uploaded resume automatically.

Tasks:

- [ ] create session_store.py
- [ ] store current resume
- [ ] auto-select uploaded resume
- [ ] remove filename requirement

Expected:

upload
↓
query directly

---

# Phase 2 — JD Input API

Goal:

Accept JD text.

Tasks:

Create:

src/api/jd.py

Endpoint:

POST /jd

Input:

{
"jd":"..."
}

Store:

current_jd

---

# Phase 3 — JD Parser

Goal:

Extract structured information.

Create:

src/services/jd_parser.py

Extract:

- role
- skills
- tools
- responsibilities
- experience

Output:

{
"role":"MLOps Engineer",

"skills":[
"Python",
"Docker",
"AWS"
]
}

---

# Phase 4 — Resume Skill Parser

Create:

resume_parser.py

Extract:

- skills
- projects
- technologies

Output:

{
"skills":[...]
}

---

# Phase 5 — Match Engine

Create:

match_service.py

Input:

resume skills
+
JD skills

Logic:

matched / total

Output:

{
score:75,

matched:[...],

missing:[...]

}

---

# Phase 6 — Match Endpoint

Create:

GET /match

Returns:

score
matched skills
missing skills

---

# Phase 7 — Query Both Sources

Current:

question
↓
resume only

Target:

question
↓
resume
+
JD
↓
retrieve
↓
answer

Example:

"What skills am I missing?"

---

# Phase 8 — Recommendation Layer

Create:

recommendation_service.py

Input:

missing skills

Output:

- learn
- build
- practice
- skip

Example:

Missing:

Kubernetes

Suggest:

Build container deployment project

---

# Commit Rule

Build
↓
Test
↓
Commit
↓
Document