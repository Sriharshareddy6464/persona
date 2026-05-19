from fastapi import APIRouter
from src.services.retrieval_service import retrieve_chunks
from src.services.llm_service import generate_response
from src.core.session_store import get_active_resume

router = APIRouter()


@router.get("/query")
async def query_documents(
        q: str
):

    active_resume = get_active_resume()

    if active_resume is None:

        return {

            "success": False,

            "message":
            "No resume uploaded"

        }

    results = retrieve_chunks(

        query=q,

        filename=active_resume

    )

    context = "\n".join(results)

    if len(context.strip()) == 0:

        return {

            "query": q,

            "active_resume":
            active_resume,

            "answer":
            "No matching information found"

        }

    prompt = f"""

You are a resume assistant.

Answer ONLY using provided context.

If answer does not exist say:

Information not available in resume.


Context:

{context}


Question:

{q}


Answer:

"""

    answer = generate_response(
        prompt
    )

    return {

        "query": q,

        "active_resume":
        active_resume,

        "answer":
        answer

    }