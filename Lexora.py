import streamlit as st
import requests

st.set_page_config(
    page_title="Lexora: A Modular Language Understanding Framework for Assistive Applications",
    page_icon="🧩",
    layout="wide"
)

st.markdown(
    """
    <style>
    /* Remove top padding & background fixes */
    .block-container {
        padding-top: 1rem !important;
        padding-bottom: 2rem !important;
        max-width: 1200px;
        margin: auto;
    }
    body {
        font-family: 'Inter', sans-serif;
        background-color: #111111;
        color: #f1f1f1;
    }
    h1, h2, h3 {
        font-weight: 600;
    }
    textarea {
        border-radius: 12px !important;
    }
    /* Cards */
    .stMarkdown, .stJson {
        background: #1c1c1c;
        padding: 1.2rem 1rem;
        border-radius: 14px;
        box-shadow: 0px 2px 8px rgba(0,0,0,0.25);
        margin-bottom: 1.5rem;
    }
    /* Header text */
    .main-title {
        text-align: center;
        font-size: 2.5rem;
        font-weight: 700;
        color: #8ee693; /* green highlight */
        margin-bottom: 0.3rem;
    }
    .subtitle {
        text-align: center;
        font-size: 1.1rem;
        color: #cccccc;
        margin-bottom: 2rem;
    }
    /* Footer */
    footer {
        bottom: 10px;
        left: 0;
        right: 0;
        text-align: center;
        font-size: 0.9rem;
        color: #888888;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("<div class='main-title'>🧩 Lexora</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Uncover Meaning · Extract Knowledge · Enable Intelligence</div>", unsafe_allow_html=True)

with st.form("text_form"):
    user_input = st.text_area(
        "💬 Enter your text:",
        height=180,
        placeholder="Paste or type text here for analysis..."
    )
    submitted = st.form_submit_button("🚀 Analyze", use_container_width=True)

BASE_URL = "http://127.0.0.1:8000"

if submitted and user_input:
    ner = requests.post(f"{BASE_URL}/ner", json={"text": user_input}).json()
    sentiment = requests.post(f"{BASE_URL}/sentiment", json={"text": user_input}).json()
    keywords = requests.post(f"{BASE_URL}/keywords", json={"text": user_input}).json()
    summary = requests.post(f"{BASE_URL}/summary", json={"text": user_input}).json()

    col1, col2 = st.columns(2, gap="large")

    with col1:
        st.subheader("🔍 Named Entity Recognition (NER)")
        st.json(ner)

        st.subheader("🧠 Sentiment Analysis")
        st.json(sentiment)

    with col2:
        st.subheader("📌 Keyword Extraction")
        st.json(keywords)

        st.subheader("📝 Text Summarization")
        st.json(summary)

st.markdown(
    "<footer>Lexora is a lightweight, modular language engine built for real-world apps.<br>Future: 🌍 Multilingual · 🎯 Intent Classification · 🤖 Chatbot Integration</footer>",
    unsafe_allow_html=True
)

