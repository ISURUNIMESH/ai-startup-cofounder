from langchain_chroma import Chroma

from rag.embeddings import get_embedding_model


def get_retriever(persist_directory="vector_db", k=3):
    """
    Load the Chroma vector database and create a retriever.
    """

    embeddings = get_embedding_model()

    vectordb = Chroma(
        persist_directory=persist_directory,
        embedding_function=embeddings
    )

    retriever = vectordb.as_retriever(
        search_kwargs={"k": k}
    )

    return retriever