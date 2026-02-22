import nltk
import string
import random
import streamlit as st
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from nltk.stem import WordNetLemmatizer
from fitness_data import faq_data

# Pre-download NLTK data
@st.cache_resource
def download_nltk():
    nltk.download('punkt')
    nltk.download('wordnet')

download_nltk()
lemmer = WordNetLemmatizer()

def LemNormalize(text):
    remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)
    return [lemmer.lemmatize(token) for token in nltk.word_tokenize(text.lower().translate(remove_punct_dict))]

@st.cache_resource
def prepare_nlp_data():
    faq_questions = list(faq_data.keys())
    tfidf_vec = TfidfVectorizer(tokenizer=LemNormalize, stop_words='english')
    tfidf_matrix = tfidf_vec.fit_transform(faq_questions)
    return faq_questions, tfidf_vec, tfidf_matrix

faq_questions, tfidf_vec, tfidf_matrix = prepare_nlp_data()

def get_bot_response(user_input):
    user_tfidf = tfidf_vec.transform([user_input])
    vals = cosine_similarity(user_tfidf, tfidf_matrix)
    flat = vals.flatten()
    idx_sorted = flat.argsort()[::-1]
    
    if flat[idx_sorted[0]] < 0.15:
        return "I'm here to help, but I'm not sure about that. Try asking about diet, exercise, or mental health! 🏃‍♂️", []

    best_match_idx = idx_sorted[0]
    answer = faq_data[faq_questions[best_match_idx]]
    
    related = [faq_questions[idx_sorted[1]], faq_questions[idx_sorted[2]]]
    other_pool = [q for i, q in enumerate(faq_questions) if i not in idx_sorted[:10]]
    different = random.choice(other_pool)
    
    return answer, related + [different]