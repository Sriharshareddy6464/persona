from fastapi import APIRouter, UploadFile, File
from datetime import datetime
from src.services.pdf_service import extract_pdf_text
from src.services.chunk_service import create_chunks
from src.services.embedding_service import (
    generate_embeddings,
    generate_batch_embeddings
)
from src.services.vector_service import store_chunks
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

    # validate file type

    if not file.filename.lower().endswith(".pdf"):

        return {

            "success": False,

            "message":
            "Only PDF files allowed"

        }

    try:

        # create unique filename

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

        # save uploaded file

        with open(
            filepath,
            "wb"
        ) as f:

            content = await file.read()

            f.write(content)

        # extract text

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

        # metadata

        metadata = {

            "filename":
            file.filename,

            "pages":
            pdf_data["pages"]

        }

        # chunk generation

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

        # embeddings

        sample_vector = generate_embeddings(

            chunks[0]["content"]

        )

        vectors = generate_batch_embeddings(

            chunks

        )

        # store vectors

        store_chunks(

            chunks,
            vectors

        )

        # response

        return {

            "success": True,

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

            "embedding_dimension":
            len(sample_vector),

            "embedding_preview":
            sample_vector[:5],

            "stored_vectors":
            len(vectors),

            "sample_chunk":

            chunks[0]["content"][:300]

        }

    except Exception as e:

        return {

            "success": False,

            "message":
            "Upload failed",

            "error":
            str(e)

        }