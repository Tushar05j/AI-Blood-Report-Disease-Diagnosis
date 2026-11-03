
from rag.vector_store import (
    get_embedding_model,
    get_chroma_collection
)


def retrieve_documents(query, top_k=3):
    """
    Retrieve relevant medical knowledge
    using semantic similarity.
    """

    if not query or not query.strip():
        return []

    model = get_embedding_model()
    collection = get_chroma_collection()

    total_documents = collection.count()

    if total_documents == 0:
        return []

    query_embedding = model.encode(
        [query],
        convert_to_numpy=True,
        normalize_embeddings=True
    )

    results = collection.query(
        query_embeddings=query_embedding.tolist(),
        n_results=min(top_k, total_documents),
        include=[
            "documents",
            "metadatas",
            "distances"
        ]
    )

    retrieved_documents = []

    if not results["documents"]:
        return []

    for index, document in enumerate(results["documents"][0]):

        metadata = results["metadatas"][0][index]

        retrieved_documents.append({
            "text": document,
            "source": metadata.get("source", "Unknown"),
            "section": metadata.get("section", "General"),
            "distance": results["distances"][0][index]
        })

    return retrieved_documents


if __name__ == "__main__":

    query = (
        "Low hemoglobin and its relationship "
        "with anemia and oxygen transport"
    )

    documents = retrieve_documents(query, top_k=3)

    for index, document in enumerate(documents, start=1):

        print(f"\n--- Result {index} ---")
        print("Source:", document["source"])
        print("Section:", document["section"])
        print("Distance:", document["distance"])
        print("Content:", document["text"])
