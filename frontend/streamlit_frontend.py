import streamlit as st
import os
import sys
import uuid

# To allow importing from the 'backend' folder
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from backend.langgraph_backend import workflow
from langchain_core.messages import HumanMessage, AIMessage

# 1. Page Configuration
st.set_page_config(
    page_title="AI Assistant",
    page_icon="🤖",
    layout="centered"
)

# 2. Premium Branding & Typography (Inter Font)
st.markdown("""
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap" rel="stylesheet">
<style>
    /* Global Styles */
    html, body, [data-testid="stAppViewContainer"] {
        font-family: 'Inter', sans-serif;
        background: linear-gradient(135deg, #0f172a 0%, #1e1b4b 100%);
        color: #f8fafc;
    }

    /* Main Container Padding */
    .main .block-container {
        max-width: 900px;
        padding-top: 3rem;
    }

    /* Header Styling */
    h1 {
        background: linear-gradient(to right, #818cf8, #c084fc);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 800 !important;
        font-size: 3rem !important;
        text-align: center;
        letter-spacing: -0.02em;
        margin-bottom: 2rem !important;
    }

    /* Glassmorphism Cache Message */
    [data-testid="stChatMessage"] {
        background: rgba(30, 41, 59, 0.5) !important;
        backdrop-filter: blur(12px) !important;
        -webkit-backdrop-filter: blur(12px) !important;
        border: 1px solid rgba(255, 255, 255, 0.1) !important;
        border-radius: 20px !important;
        padding: 1.5rem !important;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06) !important;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
        margin-bottom: 1.5rem !important;
    }

    [data-testid="stChatMessage"]:hover {
        transform: translateY(-2px);
        border-color: rgba(129, 140, 248, 0.5) !important;
        box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.2) !important;
    }

    /* Message Typography */
    [data-testid="stChatMessage"] p {
        font-size: 1.05rem;
        line-height: 1.6;
        color: #e2e8f0;
    }

    /* Chat Input Styling */
    .stChatInputContainer {
        border-radius: 25px !important;
        border: 1px solid rgba(255, 255, 255, 0.1) !important;
        background: rgba(30, 41, 59, 0.7) !important;
        backdrop-filter: blur(10px) !important;
        padding: 0.5rem !important;
    }
    
    .stChatInputContainer:focus-within {
        border-color: #818cf8 !important;
        box-shadow: 0 0 0 2px rgba(129, 140, 248, 0.2) !important;
    }

    /* Status/Loading Indicator */
    .stStatusWidget {
        background: transparent !important;
        border: none !important;
        color: #818cf8 !important;
    }

    /* Hide Streamlit Branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}

</style>
""", unsafe_allow_html=True)

# 3. Initialize Session State
def generate_thread_id():
    return str(uuid.uuid4())

def load_conversation(thread_id):
    config={"configurable":{"thread_id":thread_id}}
    state_values=workflow.get_state(config).values
    return  state_values.get("messages",[])


def add_thread(thread_id):
    if thread_id not in st.session_state.chat_threads:
        st.session_state.chat_threads.append(thread_id)

def reset_chat():
    new_id=generate_thread_id()
    st.session_state.thread_id=new_id
    st.session_state.message_history=[]
    add_thread(new_id)

if "chat_threads" not in st.session_state:
    st.session_state.chat_threads=[]

if "thread_id" not in st.session_state:
    st.session_state.thread_id=generate_thread_id()
    add_thread(st.session_state.thread_id)

if "message_history" not in st.session_state:
    st.session_state.message_history=[]



# 4. Main UI
st.markdown("<h1>Intelligent Assistant</h1>", unsafe_allow_html=True)

# 5. Message Display
for message in st.session_state.message_history:
    # Use refined avatars
    avatar = "👤" if message["role"] == "user" else "🤖"
    with st.chat_message(message["role"], avatar=avatar):
        st.markdown(message["content"])

# 6. Interaction
if prompt := st.chat_input("Ask me anything..."):
    # User Message
    config={"configurable":{"thread_id":st.session_state.thread_id}}
    st.session_state.message_history.append({"role":"user","content":prompt})
    with st.chat_message("user", avatar="👤"):
        st.markdown(prompt)

    # Agent Processing
    with st.chat_message("assistant", avatar="🤖"):
        placeholder = st.empty()
        full_response = ""
        
        with st.status("Thinking...", expanded=False) as status:
            try:
                # Streaming through events
                for msg, metadata in workflow.stream(
                    {"messages": [HumanMessage(content=prompt)]}, 
                    config=config,
                    stream_mode="messages"
                ):
                    # We only care about tokens coming from our assistant chat node
                    if metadata.get("langgraph_node") == "chat_node":
                        full_response += msg.content
                        placeholder.markdown(full_response + " ▌")
                
                # Final finish
                placeholder.markdown(full_response)
                status.update(label="Ready", state="complete", expanded=False)
                
            except Exception as e:
                st.error(f"Error: {e}")
                full_response = "I encountered an error. Please check your connection."

        st.session_state.message_history.append({"role": "assistant", "content": full_response})

# 7. Sidebar Customization
with st.sidebar:
    st.markdown("<h2 style='color:#818cf8;'>🤖 AI Assistant</h2>", unsafe_allow_html=True)

    if st.button("➕ New Chat", use_container_width=True):
        reset_chat()

    st.markdown("### 💬 My Conversations")
    for tid in reversed(st.session_state.chat_threads):
        label = f"🗨️ ...{tid[-8:]}"
        if st.button(label, key=tid, use_container_width=True):
            st.session_state.thread_id = tid
            messages = load_conversation(tid)
            temp_messages = []
            for msg in messages:
                role = "user" if isinstance(msg, HumanMessage) else "assistant"
                temp_messages.append({"role": role, "content": msg.content})
            st.session_state.message_history = temp_messages

    st.markdown("---")
    st.caption("Powered by LangGraph & Streamlit")
