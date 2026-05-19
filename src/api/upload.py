from fastapi import APIRouter, UploadFile, File
from datetime import datetime
from src.services.pdf_service import extract_pdf_text
from src.services.chunk_service import create_chunks
from src.services.embedding_service import (
    generate_embeddings,
    generate_batch_embeddings
)
from src.services.vector_service import store_chunks
from src.core.session_store import set_active_resume

import os


router = APIRouter()

UPLOAD_DIR = "uploads"

os.makedirs(

    UPLOAD_DIR,

    exist_ok=True

)


@router.post("/upload")
async def upload_pdf(

        file: UploadFile = File(...)

):

    if not file.filename.lower().endswith(".pdf"):

        return {

            "success": False,

            "message":
            "Only PDF files allowed"

        }

    try:

        timestamp = datetime.now().strftime(

            "%Y%m%d_%H%M%S"

        )

        filename = (

            f"{timestamp}_{file.filename}"

        )

        filepath = os.path.join(

            UPLOAD_DIR,

            filename

        )

        with open(

                filepath,
                "wb"

        ) as f:

            content = await file.read()

            f.write(content)

        pdf_data = extract_pdf_text(

            filepath

        )

        if not pdf_data["success"]:

            return {

                "success": False,

                "message":
                "PDF extraction failed",

                "error":
                pdf_data["error"]

            }

        metadata = {

            "filename":
            filename.lower().strip(),

            "pages":
            pdf_data["pages"]

        }

        chunks = create_chunks(

            pdf_data["text"],
            metadata

        )

        if len(chunks) == 0:

            return {

                "success": False,

                "message":
                "No chunks generated"

            }

        vectors = generate_batch_embeddings(

            chunks

        )

        store_chunks(

            chunks,
            vectors

        )

        # V2 session memory

        set_active_resume(

            filename.lower().strip()

        )

        sample_vector = generate_embeddings(

            chunks[0]["content"]

        )

        return {

            "success": True,

            "active_resume":
            filename,

            "pages":
            pdf_data["pages"],

            "characters":
            pdf_data["characters"],

            "chunks":
            len(chunks),

            "embedding_dimension":
            len(sample_vector),

            "stored_vectors":
            len(vectors)

        }

    except Exception as e:

        return {

            "success": False,

            "message":
            "Upload failed",

            "error":
            str(e)

        }