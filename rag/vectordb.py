from langchain_chroma import Chroma

from rag.embeddings import get_embedding_model


def create_vector_db(chunks, persist_directory="vector_db"):
    """
    Create and save Chroma Vector Database.
    """

    embeddings = get_embedding_model()

    vectordb = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=persist_directory
    )

    print("Vector Database Created Successfully!")

    return vectordb