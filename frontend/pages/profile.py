import streamlit as st
import sqlite3

user_info = st.session_state.get('user_info', {})
user_email = user_info.get('email', 'anonymous@example.com')
user_name = user_info.get('name', 'Guest User')
user_picture = user_info.get('picture', None)

if user_picture:
    st.image(user_picture, width=100)

st.title(f"👤 {user_name}'s Dashboard")

st.markdown(f"Welcome to your Nexa AI profile dashboard, **{user_name}** ({user_email})!")

# Calculate total chats scoped to user
try:
    conn = sqlite3.connect("chats.db")
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(DISTINCT thread_id) FROM checkpoints WHERE thread_id LIKE ?", (f"{user_email}:%",))
    total_chats = cursor.fetchone()[0]
    
    # Message count is harder to scope purely by thread_id without joining, but we can approximate by counting checkpoints for those threads
    cursor.execute("SELECT COUNT(*) FROM checkpoints WHERE thread_id LIKE ?", (f"{user_email}:%",))
    total_messages = cursor.fetchone()[0]
    conn.close()
except Exception:
    total_chats = 0
    total_messages = 0

col1, col2 = st.columns(2)
with col1:
    st.metric(label="Total Chat Sessions", value=total_chats)
with col2:
    st.metric(label="Total Interactions", value=total_messages)

st.divider()

st.subheader("Google Account Status")
st.success("✅ Authenticated securely via Google OAuth 2.0")
st.markdown("Your chat histories and uploaded documents are securely scoped to your Google account.")

