from pypdf import PdfReader
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
from transformers import pipeline

model = SentenceTransformer("all-MiniLM-L6-v2")
generator = pipeline("text2text-generation", model="google/flan-t5-small")

def answer_question(pdf, question):

    reader = PdfReader(pdf)

    text = ""
    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text

    chunk_size = 500
    chunks = []

    for i in range(0, len(text), chunk_size):
        chunks.append(text[i:i + chunk_size])

    chunk_embedding = model.encode(chunks)

    dimension = chunk_embedding.shape[1]

    index = faiss.IndexFlatL2(dimension)

    vector = np.array(chunk_embedding, dtype=np.float32)
    index.add(vector)

    query_embedding = model.encode([question])
    query_vector = np.array(query_embedding, dtype=np.float32)

    D, I = index.search(query_vector, k=3)

    context = ""
    for idx in I[0]:
        context += chunks[idx] + "\n"

    prompt = f"""
Answer the question using the context below.

Context:
{context}

Question:
{question}

Answer:
"""
    response = generator(prompt, max_new_tokens=100)
    return response[0]["generated_text"]
