import chromadb


client = chromadb.PersistentClient(
    path="./chroma_db"
)


collection = client.get_or_create_collection(
    name="persona_documents"
)


def store_chunks(
        chunks,
        vectors
):

    ids=[]

    docs=[]

    embeddings=[]

    metadatas=[]


    for chunk,vector in zip(
            chunks,
            vectors
    ):

        ids.append(
            chunk["chunk_id"]
        )

        docs.append(
            chunk["content"]
        )

        embeddings.append(
            vector
        )

        metadatas.append(
            chunk["metadata"]
        )


    collection.add(

        ids=ids,

        documents=docs,

        embeddings=embeddings,

        metadatas=metadatas

    )