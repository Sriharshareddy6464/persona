import chromadb

from src.services.embedding_service import (
    generate_embeddings
)

client=chromadb.PersistentClient(
    path="./chroma_db"
)

collection=client.get_collection(
    "persona_documents"
)


def retrieve_documents(
        query:str,
        filename:str=None,
        top_k:int=5
):

    query_embedding=generate_embeddings(
        query
    )

    query_args={

        "query_embeddings":[
            query_embedding
        ],

        "n_results":top_k

    }

    if filename:

        query_args["where"]={

            "filename":
            filename

        }

    results=collection.query(
        **query_args
    )

    return results