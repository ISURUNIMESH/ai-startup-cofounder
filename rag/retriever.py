from functools import lru_cache

from langchain_chroma import Chroma

from rag.embeddings import get_embedding_model


@lru_cache(maxsize=4)
def get_vector_db(persist_directory="vector_db"):
    """
    Load and reuse the Chroma vector database connection.
    """

    embeddings = get_embedding_model()

    return Chroma(
        persist_directory=persist_directory,
        embedding_function=embeddings
    )


@lru_cache(maxsize=8)
def get_retriever(persist_directory="vector_db", k=3):
    """
    Load the Chroma vector database and create a retriever.
    """

    vectordb = get_vector_db(persist_directory)

    retriever = vectordb.as_retriever(
        search_kwargs={"k": k}
    )

    return retriever
