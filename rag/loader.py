from langchain_community.document_loaders import PyPDFDirectoryLoader


def load_documents(pdf_folder="data/pdfs"):
    """
    Load all PDF documents from the specified folder.
    """

    loader = PyPDFDirectoryLoader(pdf_folder)

    documents = loader.load()

    print(f"{len(documents)} pages loaded.")

    return documents