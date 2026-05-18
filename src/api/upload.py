from fastapi import APIRouter, UploadFile, File
from datetime import datetime
from src.services.pdf_service import extract_pdf_text
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
            "message": "Only PDF files allowed"

        }

    try:

        # generate unique filename

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

        # save uploaded pdf

        with open(
            filepath,
            "wb"
        ) as f:

            content = await file.read()

            f.write(content)

        # extract pdf content

        pdf_data = extract_pdf_text(
            filepath
        )

        if not pdf_data["success"]:

            return {

                "success": False,

                "message": "PDF extraction failed",

                "error": pdf_data["error"]

            }

        # response

        return {

            "success": True,

            "filename": file.filename,

            "saved_as": filepath,

            "pages": pdf_data["pages"],

            "characters": pdf_data["characters"],

            "preview":
            pdf_data["text"][:500]

        }

    except Exception as e:

        return {

            "success": False,

            "message": "Upload failed",

            "error": str(e)

        }