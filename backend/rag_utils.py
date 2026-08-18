import os
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document

# Global vector store and embeddings
vector_store = None
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

def ingest_document(file_path: str):
    """Loads a PDF document, splits it, and adds it to the vector store."""
    global vector_store
    
    # Check if file exists
    if not os.path.exists(file_path):
        return 0
        
    loader = PyPDFLoader(file_path)
    docs = loader.load()
    
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    splits = text_splitter.split_documents(docs)
    
    if not splits:
        return 0
        
    if vector_store is None:
        vector_store = FAISS.from_documents(splits, embeddings)
    else:
        vector_store.add_documents(splits)
        
    return len(splits)

def search_documents(query: str) -> str:
    """Searches the uploaded documents for the given query and returns the context."""
    if vector_store is None:
        return "No documents have been uploaded yet. Please tell the user to upload a document first."
    
    docs = vector_store.similarity_search(query, k=3)
    if not docs:
        return "No relevant information found in the uploaded documents."
    
    return "\n\n".join([f"Source snippet from {os.path.basename(d.metadata.get('source', 'document'))}:\n{d.page_content}" for d in docs])
