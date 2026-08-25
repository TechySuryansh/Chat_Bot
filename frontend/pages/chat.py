import streamlit as st
import sqlite3
import uuid
import sys
import os
from langchain_core.messages import HumanMessage, AIMessage

# Ensure the root directory is in the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

# Import backend logic
from backend.langgraph_backend import workflow, checkpointer

st.title("💬 Nexa AI Chat")

# Get user info from auth state
user_info = st.session_state.get('user_info', {})
user_email = user_info.get('email', 'anonymous@example.com')

# Initialize session state for thread_id, prefixed with email to isolate history
if "thread_id" not in st.session_state:
    st.session_state.thread_id = f"{user_email}:{uuid.uuid4()}"

if "persona" not in st.session_state:
    st.session_state.persona = "You are a helpful AI assistant."

# --- Sidebar: History ---
st.sidebar.header("Conversation History")

# Fetch history from sqlite
def get_history(email):
    try:
        conn = sqlite3.connect("chats.db")
        cursor = conn.cursor()
        cursor.execute("SELECT DISTINCT thread_id FROM checkpoints WHERE thread_id LIKE ? ORDER BY checkpoint_id DESC", (f"{email}:%",))
        threads = [row[0] for row in cursor.fetchall()]
        conn.close()
        return threads
    except Exception:
        return []

history = get_history(user_email)

# New Chat Button
if st.sidebar.button("➕ New Chat", use_container_width=True):
    st.session_state.thread_id = f"{user_email}:{uuid.uuid4()}"
    st.rerun()

st.sidebar.divider()

# List past threads
for thread in history:
    # Remove the email prefix for clean display
    display_name = thread.split(':')[1][:6] if ':' in thread else thread[:6]
    if st.sidebar.button(f"Chat {display_name}", key=f"hist_{thread}", use_container_width=True):
        st.session_state.thread_id = thread
        st.rerun()

# --- Main Chat Area ---
config = {"configurable": {"thread_id": st.session_state.thread_id, "persona": st.session_state.persona}}

# Load messages for the current thread
tuple_data = checkpointer.get_tuple(config)
messages = []
if tuple_data and "channel_values" in tuple_data.checkpoint and "messages" in tuple_data.checkpoint["channel_values"]:
    messages = tuple_data.checkpoint["channel_values"]["messages"]

# Display messages
for msg in messages:
    if isinstance(msg, HumanMessage):
        with st.chat_message("user", avatar="👤"):
            st.markdown(msg.content)
    elif isinstance(msg, AIMessage):
        with st.chat_message("assistant", avatar="🤖"):
            if isinstance(msg.content, list):
                content_str = ""
                for item in msg.content:
                    if isinstance(item, dict) and "text" in item:
                        content_str += item["text"]
                    elif isinstance(item, str):
                        content_str += item
                st.markdown(content_str)
            else:
                st.markdown(str(msg.content))

# --- Chat Input ---
if prompt := st.chat_input("Ask anything..."):
    # Immediately show the user's message
    with st.chat_message("user", avatar="👤"):
        st.markdown(prompt)
    
    # Generate and display the assistant's response
    with st.chat_message("assistant", avatar="🤖"):
        message_placeholder = st.empty()
        full_response = ""
        
        try:
            # We iterate through the stream
            for msg_chunk, metadata in workflow.stream(
                {"messages": [HumanMessage(content=prompt)]},
                config=config,
                stream_mode="messages"
            ):
                if metadata.get("langgraph_node") == "agent":
                    if isinstance(msg_chunk, AIMessage) and msg_chunk.content:
                        if isinstance(msg_chunk.content, list):
                            for item in msg_chunk.content:
                                if isinstance(item, dict) and "text" in item:
                                    full_response += item["text"]
                                elif isinstance(item, str):
                                    full_response += item
                        else:
                            full_response += str(msg_chunk.content)
                        message_placeholder.markdown(full_response + "▌")
                        
            message_placeholder.markdown(full_response)
        except Exception as e:
            st.error(f"Error: {e}")
