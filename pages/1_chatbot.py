import streamlit as st
import os
import google.generativeai as genai

# CONFIGURE GEMINI
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

# FORCE WORKING MODEL
model = genai.GenerativeModel("gemini-3-flash-preview")

# CSS
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #00c6ff, #ffffff);
    color: black;
}

h1, h2, h3, p, label {
    color: black !important;
}

.card {
    background: rgba(255,255,255,0.65);
    padding: 18px;
    border-radius: 14px;
    margin-bottom: 15px;
}
</style>
""", unsafe_allow_html=True)

# TITLE
st.title("🤖 Arjun AI Assistant (Free AI - Gemini)")

st.markdown(
    '<div class="card">Powered by Google Gemini (Free)</div>',
    unsafe_allow_html=True
)

# CHAT HISTORY
if "history" not in st.session_state:
    st.session_state.history = []

# INPUT
user = st.text_input("Ask anything...")

# RESPONSE
if user:
    st.session_state.history.append(("You", user))

    try:
        response = model.generate_content(user)
        reply = response.text
    except Exception as e:
        reply = f"Error: {e}"

    st.session_state.history.append(("AI", reply))

# DISPLAY CHAT
for role, msg in st.session_state.history:
    st.markdown(
        f'<div class="card"><b>{role}:</b> {msg}</div>',
        unsafe_allow_html=True
    )