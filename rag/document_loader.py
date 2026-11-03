
from pathlib import Path
import re


BASE_DIR = Path(__file__).resolve().parent.parent
KNOWLEDGE_BASE_DIR = BASE_DIR / "knowledge_base"


def clean_text(text):
    text = re.sub(r"\n{3,}", "\n\n", text)
    text = re.sub(r"[ \t]+", " ", text)
    return text.strip()


def split_into_chunks(text, chunk_size=600, overlap=80):
    """
    Split a document into heading-aware chunks.
    Each chunk retains its section heading.
    """

    text = clean_text(text)

    # Split at Markdown headings
    sections = re.split(r"(?=^#{1,3}\s)", text, flags=re.MULTILINE)

    chunks = []

    for section in sections:
        section = section.strip()

        if not section:
            continue

        if len(section) <= chunk_size:
            chunks.append(section)
            continue

        # Preserve the heading in every chunk
        lines = section.split("\n")
        heading = lines[0]
        body = "\n".join(lines[1:]).strip()

        start = 0

        while start < len(body):
            end = min(start + chunk_size - len(heading), len(body))

            if end < len(body):
                boundary = body.rfind(" ", start, end)
                if boundary > start:
                    end = boundary

            content = body[start:end].strip()

            if content:
                chunks.append(f"{heading}\n{content}")

            if end >= len(body):
                break

            start = end - overlap

    return chunks


def load_documents():
    documents = []

    for file_path in KNOWLEDGE_BASE_DIR.glob("*.md"):
        text = file_path.read_text(encoding="utf-8")
        chunks = split_into_chunks(text)

        for index, chunk in enumerate(chunks):
            heading_match = re.search(
                r"^#{1,3}\s+(.+)$",
                chunk,
                flags=re.MULTILINE
            )

            documents.append({
                "id": f"{file_path.stem}_{index}",
                "text": chunk,
                "metadata": {
                    "source": file_path.name,
                    "section": (
                        heading_match.group(1).strip()
                        if heading_match else "General"
                    ),
                    "chunk": index
                }
            })

    return documents


if __name__ == "__main__":
    docs = load_documents()

    print("Total chunks created:", len(docs))

    for doc in docs:
        print("\n------------------------------")
        print("ID:", doc["id"])
        print("Source:", doc["metadata"]["source"])
        print("Section:", doc["metadata"]["section"])
        print("Text:", doc["text"][:250])
