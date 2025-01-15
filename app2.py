import streamlit as st
from langchain_groq import ChatGroq
import PyPDF2
import docx
import os

# Title of the app
st.title('🦜🔗 ChatGroq Quickstart with File Upload')

groq_api_key = st.secrets['GROQ_api_key']

# Function to extract text from PDF
def extract_pdf_text(pdf_file):
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    text = ''
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text

# Function to extract text from Word document (docx)
def extract_docx_text(docx_file):
    doc = docx.Document(docx_file)
    text = ''
    for para in doc.paragraphs:
        text += para.text + '\n'
    return text

# Function to extract text from a plain text file
def extract_text_file(file):
    return file.read().decode("utf-8")

# Function to generate a response from the model
def generate_response(input_text):
    llm = ChatGroq(temperature=0, groq_api_key=groq_api_key, model_name="mixtral-8x7b-32768")
    response = llm.invoke(input_text)  # Use `invoke` to generate the response

    # Directly access the content attribute from the response
    content = response.content if hasattr(response, 'content') else 'No content returned from the model.'

    # Display only the content
    st.info(content)

# File upload section
uploaded_file = st.file_uploader("Choose a file", type=["txt", "pdf", "docx"])

# If a file is uploaded
if uploaded_file is not None:
    if uploaded_file.type == "application/pdf":
        file_text = extract_pdf_text(uploaded_file)
        st.success("PDF file uploaded successfully!")
    elif uploaded_file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
        file_text = extract_docx_text(uploaded_file)
        st.success("Word document uploaded successfully!")
    elif uploaded_file.type == "text/plain":
        file_text = extract_text_file(uploaded_file)
        st.success("Text file uploaded successfully!")
    else:
        st.error("Unsupported file type!")

    # Display a preview of the text from the file
    st.subheader("Preview of the extracted content:")
    st.text_area("Extracted Content", file_text[:1000], height=300)  # Display first 1000 characters for preview

    # Now, add query functionality
    st.subheader("Ask a question from the file")
    query = st.text_input("Your Query:", "")

    if query:
        # Pass the query and file content to the model for generating a response
        generate_response(f"File content:\n{file_text}\nQuery: {query}")
else:
    st.warning("Please upload a file to get started!")

