# Flask Blood Report ML Demo
Educational interface for the project's existing Random Forest CBC classifier.

## Setup
1. Copy `random_forest_pipeline.joblib` from your trained project into this folder, beside `app.py`.
2. Open a terminal in this folder.
3. (Recommended) create and activate a virtual environment.
4. Install packages: `pip install -r requirements.txt`
5. Run: `python app.py`
6. Open `http://127.0.0.1:5000` in a browser.

The feature names in `app.py` must match the model training columns: WBC, RBC, HGB, PLT, NEUT, LYMPH, MONO, EOS, BASO. Confirm the numeric class-ID mapping and input units against your dataset/training code.

Educational prototype only; not a medical device or clinical diagnosis. Use synthetic or anonymized examples only. Flask debug server is local development only.
## Retrieval-Augmented Generation (RAG)

HemoPredict integrates a Retrieval-Augmented Generation (RAG) pipeline to provide context-aware educational explanations of predicted blood disorders.

### RAG Architecture

1. **Knowledge Base:** Medical information about CBC parameters and blood disorders is maintained in Markdown files.
2. **Document Processing:** The document loader extracts and splits knowledge into smaller, meaningful text chunks.
3. **Embedding Generation:** Sentence Transformers (`all-MiniLM-L6-v2`) converts text chunks into numerical embeddings.
4. **Vector Database:** ChromaDB stores embeddings, document content, and metadata locally.
5. **Semantic Retrieval:** Relevant medical information is retrieved based on the prediction and CBC values.
6. **LLM Generation:** Groq API uses the retrieved context to generate structured educational explanations.

### Technologies Used

- Sentence Transformers
- ChromaDB
- Groq API
- Retrieval-Augmented Generation (RAG)
- Flask
- Python

### Knowledge Base Updates

New medical knowledge can be added to the Markdown files inside `knowledge_base/`. The vector database can then be rebuilt using:

```bash
python -m rag.vector_store
```

**Note:** HemoPredict is an educational prototype and is not intended to replace professional medical diagnosis.
