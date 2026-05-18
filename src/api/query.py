from fastapi import APIRouter

from src.services.retrieval_service import (
    retrieve_documents
)

router=APIRouter()


@router.get("/query")

def query_documents(

        q:str,

        filename:str=None

):

    results=retrieve_documents(

        query=q,

        filename=filename

    )

    return{

        "query":q,

        "source":

        filename,

        "results":

        results["documents"][0]

    }