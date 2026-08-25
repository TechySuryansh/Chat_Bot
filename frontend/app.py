import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st

# pyrefly: ignore [missing-import]
from streamlit_google_auth import Authenticate
import dotenv

dotenv.load_dotenv()

st.set_page_config(
    page_title="Nexa AI",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Authenticator configuration
authenticator = Authenticate(
    secret_credentials_path='google_credentials.json',
    cookie_name='nexa_ai_auth',
    cookie_key='nexa_secret_cookie_key',
    redirect_uri='http://localhost:8501',
)

# Check authentication
authenticator.check_authentification()

if not st.session_state.get('connected'):
    st.markdown("<h1 style='text-align: center; margin-top: 50px;'>Welcome to Nexa AI</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center;'>Please sign in to access your secure chat workspace.</p>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        authorization_url = authenticator.get_authorization_url()
        st.markdown(f'<a href="{authorization_url}" target="_self" style="display: block; text-align: center; background-color: #4285F4; color: white; padding: 10px; border-radius: 5px; text-decoration: none; font-weight: bold;">Sign in with Google</a>', unsafe_allow_html=True)
    
    st.stop()

# User is authenticated
if st.sidebar.button("Logout"):
    authenticator.logout()
    st.rerun()

st.sidebar.divider()

pages = {
    "Nexa AI - Chatbot": [
        st.Page("pages/chat.py", title="Chat", icon="💬", default=True),
        st.Page("pages/profile.py", title="Profile / Dashboard", icon="👤"),
        st.Page("pages/settings.py", title="Data & Settings", icon="⚙️"),
    ]
}

pg = st.navigation(pages)
pg.run()
