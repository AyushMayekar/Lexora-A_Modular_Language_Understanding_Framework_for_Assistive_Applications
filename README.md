# Lexora: A Modular Language Understanding Framework for Assistive Applications

Welcome to the Lexora repository! 🚀  
Lexora is a lightweight, modular NLP (Natural Language Processing) system designed to **uncover meaning, extract knowledge, and enable intelligence** from raw text. By integrating state-of-the-art language models with a clean and intuitive interface, Lexora empowers developers, researchers, and businesses to analyze text effortlessly.

---

## Key Features

- **🔍 Named Entity Recognition (NER)**: Automatically detects and classifies entities such as people, organizations, locations, dates, and more.
- **🧠 Sentiment Analysis**: Analyzes emotions behind the text (positive, negative, neutral), enabling insights into customer feedback, reviews, or conversations.
- **📌 Keyword Extraction**: Identifies the most relevant and impactful keywords from the input text, useful for search optimization and summarization.
- **📝 Text Summarization**: Generates concise summaries while preserving context and meaning, perfect for long documents or articles.
- **🌍 Extensible Design**: Future roadmap includes **multilingual support**, **intent classification**, and **chatbot integration**.

---

## Technology Stack

- **Python**: Core language for backend processing and API integration.
- **FastAPI**: For building high-performance REST APIs that expose NLP endpoints.
- **Hugging Face Transformers**: Pre-trained models powering NER, sentiment analysis, and summarization.
- **Streamlit**: Frontend framework for an interactive and user-friendly dashboard.
- **Requests**: For seamless communication between frontend and backend.

---

## Installation

1. **Clone the Repository**:

   ```sh
   git clone https://github.com/AyushMayekar/Lexora-A_Modular_Language_Understanding_Framework_for_Assistive_Applications
````

2. **Install dependencies**:

   ```sh
   pip install -r requirements.txt
   ```

3. **Start the backend (FastAPI server)**:

   ```sh
   uvicorn routes:app --reload
   ```

   The API will run at `http://127.0.0.1:8000`

4. **Start the frontend (Streamlit app)**:

   ```sh
   streamlit run Lexora.py
   ```

5. **Access the application**:
   Open your browser and go to: `http://localhost:8501`

---

## Contact

For further information about **Lexora**, please reach out to the project creator via [LinkedIn](https://www.linkedin.com/in/ayush-mayekar-b9b883284).

Thank you for exploring Lexora and contributing to its growth! 🤝