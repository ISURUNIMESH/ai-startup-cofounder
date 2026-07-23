from rag.retriever import get_retriever

retriever = get_retriever()

query = "How to validate a startup idea?"

results = retriever.invoke(query)

print(f"\nRetrieved {len(results)} documents.\n")

for i, doc in enumerate(results, start=1):
    print("=" * 80)
    print(f"Result {i}")
    print("=" * 80)
    print(doc.page_content[:700])
    print("\nSource:", doc.metadata.get("source"))
    print("Page:", doc.metadata.get("page"))
    print()