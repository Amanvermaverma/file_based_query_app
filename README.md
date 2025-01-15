# file_based_query_app
file_based_query_app This script is a Streamlit app designed for processing file uploads and generating responses using the ChatGroq model. Key features include:


File Upload Support:

Accepts PDF, Word docx, and plain text files.
Extracts text from the uploaded files using appropriate libraries.
Content Display:

Previews the extracted content in a text area (first 1000 characters).
Query Handling:

Allows users to input a query based on the uploaded file's content.
Passes the file's content and user query to the ChatGroq model to generate a response.
Displays the model's response using Streamlit.
API Integration:

Utilizes the ChatGroq model with a temperature setting of 0 for deterministic responses.
Accesses the Groq API key securely via Streamlit secrets.
The app provides an interactive, user-friendly interface for extracting and querying text content from files.
