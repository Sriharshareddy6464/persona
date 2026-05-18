from langchain_text_splitters import RecursiveCharacterTextSplitter
import uuid


splitter = RecursiveCharacterTextSplitter(

    chunk_size=750,
    chunk_overlap=100

)


def create_chunks(
        text:str,
        metadata:dict
):

    docs = splitter.create_documents(
        [text]
    )

    chunks=[]

    for doc in docs:

        chunks.append({

            "chunk_id":
            str(uuid.uuid4()),

            "content":
            doc.page_content,

            "metadata":
            metadata

        })

    return chunks