# 🥗 Task 2: CareBuddy AI (Fitness & Nutrition Chatbot)

## 📝 Project Overview
**CareBuddy** is an intelligent conversational agent developed during my **CodeAlpha** internship. It is designed to act as a personal health assistant, providing scientifically backed information on nutrition, exercise, and mental well-being.

The chatbot uses **Natural Language Processing (NLP)** to understand user intent, allowing it to provide relevant answers even if the user's wording doesn't exactly match the database.

## 🚀 Key Features
- **Intelligent Query Matching:** Uses TF-IDF Vectorization and Cosine Similarity to find the best response from the knowledge base.
- **Smart Text Processing:** Implements NLTK-based lemmatization to handle different word forms (e.g., "running" vs "run").
- **Dynamic Suggestions:** After every response, the bot provides 3 follow-up questions to keep the user engaged.
- **Interactive UI:** Built with Streamlit, featuring Lottie animations and a "Reset Chat" function to clear session history.

## 🛠️ Technical Implementation

### 1. Data Processing (`main.py` & `fitness_data.py`)
The bot's intelligence comes from a custom pipeline:
* **Tokenization & Lemmatization:** Breaking sentences into core words using `nltk`.
* **TF-IDF Vectorization:** Converting text into numerical data that the computer can "compare."
* **Cosine Similarity:** Calculating the mathematical "closeness" between the user's input and the stored FAQs.

### 2. Frontend Interface (`app.py`)
- **Session State:** Stores chat history so the conversation feels continuous.
- **Lottie Animations:** Uses JSON-based animations for a modern, friendly look.

## ⚙️ Installation & Usage

1. **Install Dependencies:**
   pip install streamlit nltk scikit-learn requests streamlit-lottie