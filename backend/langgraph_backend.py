import os
import uuid

from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.tools import tool
# pyrefly: ignore [missing-import]
from langchain_google_genai import ChatGoogleGenerativeAI
import sqlite3
# pyrefly: ignore [missing-import]
from langgraph.checkpoint.sqlite import SqliteSaver
from langgraph.prebuilt import create_react_agent
# pyrefly: ignore [missing-import]
from duckduckgo_search import DDGS

import backend.rag_utils as rag_utils

load_dotenv()

def get_gemini_api_key():
    api_key = os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY") or os.getenv("LANGCHAIN_GEMINI_API_KEY")
    return api_key

api_key = get_gemini_api_key()
if not api_key:
    raise ValueError("Gemini API Key not found! Please set GEMINI_API_KEY in .env")

# Initialize the LLM
model = ChatGoogleGenerativeAI(api_key=api_key, model="gemini-3.6-flash", streaming=True)

@tool
def web_search(query: str) -> str:
    """Use this tool to search the web for current events, facts, or any information you don't know."""
    try:
        results = DDGS().text(query, max_results=3)
        return "\n".join([f"{r['title']}: {r['body']}" for r in results])
    except Exception as e:
        return f"Error searching the web: {str(e)}"

@tool
def document_search(query: str) -> str:
    """Use this tool to search through the user's uploaded documents for specific information."""
    return rag_utils.search_documents(query)

# Define tools list for the agent
tools = [web_search, document_search]

# Set up the memory checkpointer
conn = sqlite3.connect('chats.db', check_same_thread=False)
checkpointer = SqliteSaver(conn)

def state_modifier(state, config):
    persona = config.get("configurable", {}).get("persona", "You are a helpful AI assistant.")
    prompt = persona + "\n\nWhen answering from documents via the document_search tool, you MUST explicitly cite the original filename of the document your information came from."
    return [SystemMessage(content=prompt)] + state["messages"]

# Create the agent workflow using LangGraph's prebuilt ReAct agent
workflow = create_react_agent(
    model,
    tools=tools,
    checkpointer=checkpointer,
    prompt=state_modifier
)
def generate_thread():
    return uuid.uuid4()

if __name__ == "__main__":
    config = {"configurable": {"thread_id": "chat_session_1", "persona": "You are a helpful AI assistant."}}
    while True:
        user_input = input("User: ")
        if user_input.lower() in ["quit", "exit", "q"]:
            print("Goodbye!")
            break
        response = workflow.invoke({"messages": [HumanMessage(content=user_input)]}, config=config)
        print(f"Assistant: {response['messages'][-1].content}")
