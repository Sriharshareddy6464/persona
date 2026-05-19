# Phase 1 — Data Ingestion Pipeline

Goal:
Accept PDF files and prepare documents

Status: DONE

## Tasks

### Upload API

- [ ] Create upload route
- [ ] Accept multipart file upload
- [ ] Restrict file type (.pdf)
- [ ] Add max file size validation
- [ ] Save file temporarily

---

### File Structure

- [ ] Create uploads/ directory
- [ ] Create services/ directory
- [ ] Create utils/ directory

Structure:

src/

api/
services/
utils/

uploads/

---

### PDF Extraction

- [ ] Install pypdf
- [ ] Create extraction service
- [ ] Read PDF pages
- [ ] Merge extracted text
- [ ] Handle extraction failure
- [ ] Handle empty PDFs

---

### Metadata

Store:

- filename
- upload timestamp
- page count
- character count
- file size

---

### Logging

- [ ] Add logger.py
- [ ] Log uploads
- [ ] Log failures
- [ ] Log extraction results

---

### Test

Upload:

sample.pdf

Expected:

{
filename,
pages,
characters,
text_preview
}