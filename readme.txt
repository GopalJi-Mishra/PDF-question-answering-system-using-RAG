How It Works

1. Upload a PDF.
2. The PDF text is extracted.
3. The text is divided into chunks.
4. Sentence embeddings are generated.
5. Embeddings are stored in FAISS.
6. The user's question is embedded.
7. The most relevant chunks are retrieved.
8. FLAN-T5 generates the final answer based on the retrieved context.