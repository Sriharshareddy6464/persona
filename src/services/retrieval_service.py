from src.services.embedding_service import (
    generate_embeddings
)

from src.services.vector_service import (
    collection
)


def retrieve_chunks(
        query: str,
        filename: str = None,
        top_k: int = 5
):

    query_embedding = generate_embeddings(
        query
    )

    if filename:

        results = collection.query(

            query_embeddings=[
                query_embedding
            ],

            n_results=top_k,

            where={

                "filename":
                filename

            }

        )

    else:

        results = collection.query(

            query_embeddings=[
                query_embedding
            ],

            n_results=top_k

        )

    documents = results.get(
        "documents",
        [[]]
    )[0]

    return documents