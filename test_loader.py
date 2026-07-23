from rag.loader import load_documents

documents = load_documents()

print(documents[0].page_content[:500])