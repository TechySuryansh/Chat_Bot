from langgraph.graph import StateGraph,START,END
from typing import Annotated,TypedDict
from langchain_core.messages import HumanMessage,BaseMessage
from langgraph.graph.message import add_messages
from langchain_groq import ChatGroq
from langgraph.checkpoint.memory import MemorySaver
import os
from dotenv import load_dotenv
import uuid


load_dotenv()

def get_groq_api_key():
    
    
    api_key = os.getenv("GROQ_API_KEY") or os.getenv("LANGCHAIN_GROQ_API_KEY")
    

    if not api_key:
        try:
            import streamlit as st
            api_key = st.secrets.get("GROQ_API_KEY") or st.secrets.get("LANGCHAIN_GROQ_API_KEY")
        except (ImportError, FileNotFoundError, Exception):
            pass
            
    return api_key

 
api_key = get_groq_api_key()


if not api_key:
    raise ValueError(
        "Groq API Key not found! Please check your .env file (locally) "
        "or add 'GROQ_API_KEY' to your Streamlit Cloud Secrets."
    )

model = ChatGroq(api_key=api_key, model="llama-3.3-70b-versatile",streaming=True)

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

def generate_thread():
    thread_id=uuid.uuid4()
    return thread_id



if __name__ == "__main__":
    config={"configurable":{"thread_id":"chat_session_1"}}

    while True:
        user_input=input("User: ")

        if user_input.lower() in ["quit","exit","q"]:
            print("Goodbye!")
            break

        response=workflow.invoke({"messages":[HumanMessage(content=user_input)]},config=config)
        print(f"Assistant: {response['messages'][-1].content}")
