from fastapi import APIRouter, UploadFile, File
import os
from datetime import datetime

router = APIRouter()

UPLOAD_DIR="uploads"

os.makedirs(UPLOAD_DIR,exist_ok=True)


@router.post("/upload")

async def upload_pdf(
        file:UploadFile=File(...)
):

    if not file.filename.endswith(".pdf"):

        return {

            "success":False,
            "message":"Only PDF files allowed"

        }

    timestamp=datetime.now().strftime(
        "%Y%m%d_%H%M%S"
    )

    filepath=f"{UPLOAD_DIR}/{timestamp}_{file.filename}"

    with open(filepath,"wb") as f:

        content=await file.read()

        f.write(content)

    return{

        "success":True,
        "filename":file.filename,
        "saved_as":filepath
    }