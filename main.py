import streamlit as st
import time

# Page setup must be first Streamlit command
st.set_page_config(page_title="Arjun AI Suite", layout="wide")

# INTRO ANIMATION + GLOBAL CSS
st.markdown("""
<style>

/* INTRO SCREEN */
#intro {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100vh;
    background: linear-gradient(135deg, #00c6ff, #ffffff);
    display: flex;
    align-items: center;
    justify-content: center;
    flex-direction: column;
    z-index: 999999;
    animation: fadeOut 1s ease forwards;
    animation-delay: 2.5s;
}

.logo-circle {
    width: 110px;
    height: 110px;
    border-radius: 50%;
    background: #0f172a;
    color: white;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 45px;
    margin-bottom: 20px;
    animation: popIn 1s ease;
    box-shadow: 0px 8px 25px rgba(0,0,0,0.25);
}

#intro h1 {
    font-size: 3.5rem;
    color: #0f172a !important;
    margin: 0;
    animation: slideUp 1.2s ease;
}

#intro p {
    font-size: 1.2rem;
    color: #334155 !important;
    margin-top: 10px;
    animation: fadeIn 2s ease;
}

/* MAIN APP BACKGROUND */
.stApp {
    background: linear-gradient(135deg, #00c6ff, #ffffff);
    color: black;
}

/* TEXT */
h1, h2, h3, p, label {
    color: black !important;
}

/* SIDEBAR */
section[data-testid="stSidebar"] {
    background-color: #0f172a;
}

section[data-testid="stSidebar"] * {
    color: white !important;
}

/* INPUTS */
.stTextInput>div>div>input,
.stTextArea textarea,
.stNumberInput input,
.stSelectbox>div>div {
    border-radius: 10px;
    background-color: rgba(255,255,255,0.85);
    color: black;
}

/* BUTTONS */
.stButton>button {
    border-radius: 10px;
    background-color: #00aaff;
    color: white;
    border: none;
    padding: 10px 20px;
    font-weight: 600;
}

/* CARDS */
.card {
    background: rgba(255,255,255,0.65);
    padding: 18px;
    border-radius: 14px;
    margin-bottom: 15px;
    box-shadow: 0px 4px 12px rgba(0,0,0,0.12);
}

/* ANIMATIONS */
@keyframes slideUp {
    from {
        transform: translateY(45px);
        opacity: 0;
    }
    to {
        transform: translateY(0);
        opacity: 1;
    }
}

@keyframes fadeIn {
    from {
        opacity: 0;
    }
    to {
        opacity: 1;
    }
}

@keyframes popIn {
    from {
        transform: scale(0.4);
        opacity: 0;
    }
    to {
        transform: scale(1);
        opacity: 1;
    }
}

@keyframes fadeOut {
    to {
        opacity: 0;
        visibility: hidden;
    }
}

</style>

<div id="intro">
    <div class="logo-circle">AI</div>
    <h1>Arjun AI Suite</h1>
    <p>Smart • Fast • Multi-Purpose AI Platform</p>
</div>
""", unsafe_allow_html=True)

# Small pause so intro feels real
time.sleep(2.8)

# MAIN PAGE
st.title("🚀 Arjun AI Suite")

st.subheader("Developed by Arjun Sunil Pandey")

st.markdown(
    '<div class="card"><b>Project:</b> Multi-Purpose AI Assistant Platform</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="card">Welcome to Arjun AI Suite. Use the sidebar to explore all tools and features.</div>',
    unsafe_allow_html=True
)

col1, col2 = st.columns(2)

with col1:
    st.markdown('<div class="card">🤖 <b>Chatbot</b><br>Basic AI assistant for user queries.</div>', unsafe_allow_html=True)
    st.markdown('<div class="card">📊 <b>Data Viewer</b><br>Upload and display CSV data.</div>', unsafe_allow_html=True)
    st.markdown('<div class="card">🌍 <b>Translator</b><br>Translate text into different languages.</div>', unsafe_allow_html=True)
    st.markdown('<div class="card">🎮 <b>Mini Games</b><br>Fun games inside the AI suite.</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="card">🧠 <b>AI Agent</b><br>Solve mathematical expressions.</div>', unsafe_allow_html=True)
    st.markdown('<div class="card">📄 <b>Document Q&A</b><br>Ask questions from uploaded documents.</div>', unsafe_allow_html=True)
    st.markdown('<div class="card">📈 <b>Attendance Calculator</b><br>Calculate attendance percentage.</div>', unsafe_allow_html=True)
    st.markdown('<div class="card">✨ <b>Magic Modes</b><br>Useful tools like password generator, jokes, planner, and more.</div>', unsafe_allow_html=True)