from langgraph.graph import StateGraph,START,END
from typing import Annotated,TypedDict
from langchain_core.messages import HumanMessage,BaseMessage
from langgraph.graph.message import add_messages
from langchain_groq import ChatGroq
from langgraph.checkpoint.memory import MemorySaver
import os
from dotenv import load_dotenv

# 1. Load environment variables for local development
load_dotenv()

def get_groq_api_key():
    """
    Retrieves the Groq API key from environment variables or Streamlit secrets.
    Ensures the application works both locally (.env) and on Streamlit Cloud (Secrets).
    """
    # 1. Check Standard Environment Variable
    api_key = os.getenv("GROQ_API_KEY") or os.getenv("LANGCHAIN_GROQ_API_KEY")
    
    # 2. Fallback to Streamlit Secrets (for Cloud deployment)
    if not api_key:
        try:
            import streamlit as st
            # Check both possible naming conventions in st.secrets
            api_key = st.secrets.get("GROQ_API_KEY") or st.secrets.get("LANGCHAIN_GROQ_API_KEY")
        except (ImportError, FileNotFoundError, Exception):
            pass
            
    return api_key

# Initialize API Key
api_key = get_groq_api_key()

# 2. Initialize Model with robust error checking
if not api_key:
    raise ValueError(
        "Groq API Key not found! Please check your .env file (locally) "
        "or add 'GROQ_API_KEY' to your Streamlit Cloud Secrets."
    )

model = ChatGroq(api_key=api_key, model="llama-3.3-70b-versatile")

class ChatState(TypedDict):
    messages:Annotated[list[BaseMessage],add_messages]

def chat_node(state:ChatState):
    messages=state["messages"]
    response =model.invoke(messages)
    return {"messages":[response]}



checkpointer=MemorySaver()
graph=StateGraph(ChatState)

graph.add_node("chat_node",chat_node)

graph.add_edge(START,"chat_node")
graph.add_edge("chat_node",END)

workflow=graph.compile(checkpointer=checkpointer)


if __name__ == "__main__":
    config={"configurable":{"thread_id":"chat_session_1"}}

    while True:
        user_input=input("User: ")

        if user_input.lower() in ["quit","exit","q"]:
            print("Goodbye!")
            break

        response=workflow.invoke({"messages":[HumanMessage(content=user_input)]},config=config)
        print(f"Assistant: {response['messages'][-1].content}")
