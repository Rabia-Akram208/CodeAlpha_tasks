import streamlit as st
from deep_translator import GoogleTranslator
from gtts import gTTS

# --- 1. PAGE CONFIG ---
st.set_page_config(page_title="LingoBot AI", page_icon="🔮", layout="wide")

# --- 2. PREVIOUS THEME & LAYOUT FIXES (CSS) ---
st.markdown("""
    <style>
    /* REMOVE ALL PADDING & MARGINS */
    .block-container {
        padding-top: 0rem !important;
        padding-bottom: 0rem !important;
        max-width: 100% !important;
    }
    
    /* ORIGINAL AMETHYST GRADIENT BACKGROUND */
    .stApp {
        background: radial-gradient(circle at top left, #e0c3fc, #fbc2eb, #a18cd1, #8ec5fc);
        background-size: 400% 400%;
        animation: gradient 15s ease infinite;
    }
    @keyframes gradient { 0% {background-position: 0% 50%;} 50% {background-position: 100% 50%;} 100% {background-position: 0% 50%;} }

    /* HEADER FIX - Visible and tight to top */
    .header-container {
        text-align: center;
        padding-top: 20px !important;
        margin-bottom: -10px !important;
        overflow: visible !important;
    }

    .app-title {
        color: #4834d4 !important;
        font-weight: 800 !important;
        font-size: 4rem !important; 
        margin: 0 !important;
        line-height: 1.1 !important;
    }

    .app-punchline {
        color: #4834d4;
        font-size: 1.2rem;
        font-weight: 600;
        margin-top: 0px !important;
    }

    /* THE PROFESSIONAL GLASS CARD */
    .glass-card {
        background: rgba(255, 255, 255, 0.3);
        backdrop-filter: blur(25px);
        border-radius: 30px;
        border: 1px solid rgba(255, 255, 255, 0.4);
        padding: 30px;
        text-align: center;
        box-shadow: 0 15px 35px rgba(0,0,0,0.05);
        margin-top: 0px !important;
    }

    /* THE ONE-LINE EXIT BUTTON FIX */
    div.stButton > button {
        white-space: nowrap !important;
        width: auto !important;
        min-width: 120px;
        background: linear-gradient(90deg, #8E2DE2 0%, #4A00E0 100%) !important;
        color: white !important;
        border-radius: 50px !important;
        border: none !important;
        padding: 10px 25px !important;
        font-weight: bold !important;
    }
    
    .quote-line { 
        color: #4834d4; 
        font-size: 1.15rem; 
        font-style: italic; 
        display: block; 
        margin: 4px 0;
        font-weight: 500;
    }

    /* Result styling */
    .result-card {
        background-color: rgba(255, 255, 255, 0.4);
        padding: 20px;
        border-radius: 15px;
        border-top: 4px solid #4A00E0;
        color: #1E293B;
        text-align: left;
    }

    header {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# --- 3. STATE MANAGEMENT ---
if 'page' not in st.session_state:
    st.session_state.page = 'welcome'

def render_header():
    st.markdown("""
        <div class="header-container">
            <h1 class="app-title">LingoBot AI</h1>
            <p class="app-punchline">"Your voice, globally understood."</p>
        </div>
    """, unsafe_allow_html=True)

# --- 4. WELCOME PAGE ---
if st.session_state.page == 'welcome':
    render_header()
    _, center, _ = st.columns([1, 2, 1])
    with center:
        st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
        # Orb Style Icon
        st.markdown("<h1 style='font-size: 80px; margin: 0;'>🌍</h1>", unsafe_allow_html=True)
        st.markdown("""
            <div style="margin: 15px 0;">
                <span class="quote-line">"Your world, now in every language."</span>
                <span class="quote-line">"Break the silence. Speak the world."</span>
                <span class="quote-line">"Simple steps to a world without borders."</span>
            </div>
        """, unsafe_allow_html=True)
        if st.button("Get Started →"):
            st.session_state.page = 'main'
            st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)

# --- 5. MAIN TRANSLATOR PAGE ---
else:
    # Exit button right, title centered
    col_empty, col_title, col_exit = st.columns([1, 6, 1])
    with col_title:
        render_header()
    with col_exit:
        st.write("<div style='height:45px;'></div>", unsafe_allow_html=True)
        if st.button("Back"):
            st.session_state.page = 'welcome'
            st.rerun()

    st.markdown("<hr style='margin:10px 0;'>", unsafe_allow_html=True)
    
    all_langs = GoogleTranslator().get_supported_languages(as_dict=True)
    
    col_in, col_out = st.columns(2, gap="large")
    with col_in:
        st.markdown("**From**")
        src = st.selectbox("src", options=list(all_langs.keys()), index=list(all_langs.keys()).index('english'), label_visibility="collapsed")
        text_in = st.text_area("Say something...", placeholder="Type here...", height=150, label_visibility="collapsed")

    with col_out:
        st.markdown("**To**")
        tar = st.selectbox("tar", options=list(all_langs.keys()), index=list(all_langs.keys()).index('spanish'), label_visibility="collapsed")
        
        st.write("<div style='margin-top:10px;'></div>", unsafe_allow_html=True)
        if st.button("Translate Content ✨"):
            if text_in:
                res = GoogleTranslator(source=all_langs[src], target=all_langs[tar]).translate(text_in)
                st.markdown(f"<div class='result-card'><p style='margin:0;'>{res}</p></div>", unsafe_allow_html=True)
                st.code(res, language=None)
                
                tts = gTTS(text=res, lang=all_langs[tar])
                tts.save("v.mp3")
                st.audio("v.mp3")