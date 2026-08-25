import streamlit as st
import os
import sys
import shutil

# Ensure the root directory is in the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

import backend.rag_utils as rag_utils

st.title("⚙️ Data & Settings")

st.header("Upload Documents for RAG")
st.markdown("Upload a PDF to give Nexa AI context. The AI will use these documents to answer your questions and will cite the source file.")

uploaded_file = st.file_uploader("Choose a PDF file", type=["pdf"])

if uploaded_file is not None:
    if st.button("Ingest Document"):
        with st.spinner("Ingesting document..."):
            temp_dir = "temp_uploads"
            os.makedirs(temp_dir, exist_ok=True)
            file_path = os.path.join(temp_dir, uploaded_file.name)
            
            with open(file_path, "wb") as f:
                f.write(uploaded_file.getbuffer())
            
            try:
                chunks = rag_utils.ingest_document(file_path)
                if chunks > 0:
                    st.success(f"Successfully ingested {uploaded_file.name} into {chunks} chunks!")
                else:
                    st.warning("Failed to ingest document or no text found.")
            except Exception as e:
                st.error(f"Error during ingestion: {e}")
            finally:
                if os.path.exists(file_path):
                    os.remove(file_path)

st.divider()

st.header("AI Persona Settings")
st.markdown("Customize how the AI talks to you.")

if "persona" not in st.session_state:
    st.session_state.persona = "You are a helpful AI assistant."

new_persona = st.text_input("System Persona", value=st.session_state.persona)

if st.button("Save Persona"):
    st.session_state.persona = new_persona
    st.success("Persona saved successfully! It will be used in your next chat message.")
