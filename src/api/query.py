from fastapi import APIRouter

from src.services.retrieval_service import (
    retrieve_documents
)

from src.services.generation_service import (
    generate_response
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

    docs=results["documents"][0]

    answer=generate_response(

        q,
        docs

    )

    return{

        "query":q,

        "source":filename,

        "answer":answer

    }