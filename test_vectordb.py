from rag.loader import load_documents
from rag.splitter import split_documents
from rag.vectordb import create_vector_db

documents = load_documents()

chunks = split_documents(documents)

vectordb = create_vector_db(chunks)

print()

print("Total Chunks Stored:", vectordb._collection.count())