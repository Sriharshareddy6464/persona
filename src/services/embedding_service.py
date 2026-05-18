from langchain_huggingface import HuggingFaceEmbeddings


embedding_model = HuggingFaceEmbeddings(

    model_name=
    "sentence-transformers/all-MiniLM-L6-v2"

)


# single embedding
# used for preview/testing

def generate_embeddings(
        text:str
):

    vector = embedding_model.embed_query(
        text
    )

    return vector


# batch embeddings
# used for storage

def generate_batch_embeddings(
        chunks
):

    vectors=[]

    for chunk in chunks:

        vector = embedding_model.embed_query(

            chunk["content"]

        )

        vectors.append(
            vector
        )

    return vectors