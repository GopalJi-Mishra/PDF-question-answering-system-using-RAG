import streamlit as st
from RAG import answer_question

st.title("PDF Question Answering")

pdf = st.file_uploader("Upload PDF", type="pdf")
question = st.text_input("Ask a question")

if st.button("Answer"):
    if pdf and question:
        answer = answer_question(pdf, question)
        st.write(answer)