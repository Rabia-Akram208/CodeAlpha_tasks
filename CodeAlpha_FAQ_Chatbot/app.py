import streamlit as st
from streamlit_lottie import st_lottie
import requests
from main import get_bot_response

# 1. Page Configuration
st.set_page_config(page_title="CareBuddy", layout="wide", initial_sidebar_state="collapsed")

# 2. Optimized CSS for Ultra-Tight Spacing & Small Fonts
st.markdown("""
    <style>
    /* Remove all top white space and headers */
    .block-container {
        padding-top: 0rem !important;
        padding-bottom: 0rem !important;
    }
    header {visibility: hidden;}
    [data-testid="stSidebar"] { display: none; }
    
    /* Global Theme */
    .stApp { background-color: #e0f7fa; }

    /* TIGHT HEADER SECTION */
    .header-box {
        text-align: center;
        margin-top: -40px; /* Pulls emoji/title to the very top */
        margin-bottom: -10px;
    }
    
    .carebuddy-title {
        color: #ff5722 !important; 
        font-size: 55px !important; /* Smaller Title */
        font-weight: 900 !important;
        margin: 0 !important;
            text-align: center;
    }

    .tagline {
        color: #01579b; 
        font-size: 12px; 
        font-weight: bold;
        margin-top: -5px !important;
            text-align: center;
    }

    /* REDUCED CHAT FONT AND TIGHT BOXES */
    /* Targets the message bubble */
    [data-testid="stChatMessage"] {
        padding: 2px !important;
        margin-bottom: -10px !important; /* Removes gap between messages */
    }

    /* Targets the text box inside the bubble */
    [data-testid="stChatMessageContent"] {
        border: 2px solid #01579b !important;
        border-radius: 10px !important;
        background-color: white !important;
        padding: 4px 8px !important; /* Tighter internal padding */
        box-shadow: 2px 2px 0px rgba(1, 87, 155, 0.1);
        color: #01579b !important;
    }

    /* Target specific text tags for font reduction */
    [data-testid="stChatMessageContent"] p, 
    [data-testid="stChatMessageContent"] li,
    [data-testid="stChatMessageContent"] div {
        font-size: 15px !important; /* Small, professional font size */
        line-height: 1.3 !important;
        margin-bottom: 2px !important;
    }

    /* RESET BUTTON (Small & Pinned Right) */
    div.stButton > button {
        border: 1.5px solid #01579b !important;
        background-color: white !important;
        color: #01579b !important;
        font-size: 11px !important;
        padding: 2px 10px !important;
        border-radius: 5px;
        margin-top: 5px;
    }

    /* Tighten Horizontal Line */
    hr { margin: 5px 0px !important; border-top: 1px solid #b2ebf2 !important; }
    </style>
    """, unsafe_allow_html=True)

# 3. Safe Animation Loader
def load_lottie(url):
    try:
        r = requests.get(url, timeout=5)
        return r.json() if r.status_code == 200 else None
    except: return None

lottie_salad = load_lottie("https://assets5.lottiefiles.com/packages/lf20_t9uon99z.json")

# 4. TOP CENTRE HEADER
col1, col2, col3 = st.columns([1, 4, 1])

with col2:
    st.markdown('<div class="header-box">', unsafe_allow_html=True)
    if lottie_salad:
        st_lottie(lottie_salad, height=110, key="salad") # Compact emoji
    st.markdown('<h1 class="carebuddy-title">🥗CareBuddy</h1>', unsafe_allow_html=True)
    st.markdown('<p class="tagline">Eat Healthy, Stay Fit</p>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

with col3:
    if st.button("Reset Chat"):
        st.session_state.messages = []
        st.session_state.suggestions = []
        st.rerun()

st.markdown("<hr>", unsafe_allow_html=True)

# 5. CHAT ENGINE
if "messages" not in st.session_state:
    st.session_state.messages = []

# Displaying chat (Styles applied via CSS)
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

def handle_query(query):
    if query:
        st.session_state.messages.append({"role": "user", "content": query})
        ans, suggs = get_bot_response(query)
        st.session_state.messages.append({"role": "assistant", "content": ans})
        st.session_state.suggestions = suggs
        st.rerun()

# Floating Input Bar
prompt = st.chat_input("Ask CareBuddy...")
if prompt:
    handle_query(prompt)

# Suggestions (Compact)
if "suggestions" in st.session_state and st.session_state.suggestions:
    st.markdown("<p style='text-align:center; font-size:11px; margin-bottom:2px;'>Recommended:</p>", unsafe_allow_html=True)
    cols = st.columns(3)
    for i, s in enumerate(st.session_state.suggestions):
        if cols[i].button(s, key=f"btn_{i}"):
            handle_query(s)