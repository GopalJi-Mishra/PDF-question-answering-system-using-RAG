from fastapi import FastAPI, UploadFile, File, Form
from RAG import answer_question

app = FastAPI()

@app.post("/ask")
def ask_question(pdf: UploadFile = File(...), question: str = Form(...)):
    answer = answer_question(pdf.file, question)
    return {"question": question, "answer": answer}
