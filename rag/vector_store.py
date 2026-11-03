
from pathlib import Path
from functools import lru_cache

import chromadb
from sentence_transformers import SentenceTransformer

from rag.document_loader import load_documents


BASE_DIR = Path(__file__).resolve().parent.parent
CHROMA_DIR = BASE_DIR / "chroma_db"

EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"
COLLECTION_NAME = "hemopredict_knowledge"


@lru_cache(maxsize=1)
def get_embedding_model():
    """Load the embedding model once and reuse it."""
    return SentenceTransformer(EMBEDDING_MODEL)


@lru_cache(maxsize=1)
def get_chroma_client():
    """Create one persistent ChromaDB client."""
    return chromadb.PersistentClient(path=str(CHROMA_DIR))


def get_chroma_collection():
    """Get the HemoPredict knowledge collection."""
    client = get_chroma_client()

    return client.get_or_create_collection(
        name=COLLECTION_NAME,
        metadata={"hnsw:space": "cosine"}
    )


def build_vector_store():
    """Generate and store embeddings for all knowledge documents."""

    print("Loading documents...")

    documents = load_documents()

    if not documents:
        raise ValueError("No documents found in knowledge_base.")

    print("Documents loaded:", len(documents))

    model = get_embedding_model()

    texts = [doc["text"] for doc in documents]
    ids = [doc["id"] for doc in documents]
    metadatas = [doc["metadata"] for doc in documents]

    print("Generating embeddings...")

    embeddings = model.encode(
        texts,
        convert_to_numpy=True,
        normalize_embeddings=True
    )

    collection = get_chroma_collection()

    print("Removing old embeddings...")

    existing_ids = collection.get()["ids"]

    if existing_ids:
        collection.delete(ids=existing_ids)

    print("Storing updated embeddings...")

    collection.upsert(
        ids=ids,
        documents=texts,
        embeddings=embeddings.tolist(),
        metadatas=metadatas
    )

    print("\nVector database updated successfully!")
    print("Total chunks:", collection.count())
    print("Database:", CHROMA_DIR)


if __name__ == "__main__":
    build_vector_store()
