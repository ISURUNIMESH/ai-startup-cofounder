from rag.loader import load_documents
from rag.splitter import split_documents

documents = load_documents()

chunks = split_documents(documents)

print()

print("First Chunk:\n")
print(chunks[0].page_content)

print()

print("Metadata:\n")
print(chunks[0].metadata)