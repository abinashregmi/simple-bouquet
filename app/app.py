import streamlit as st
import requests
from streamlit_lottie import st_lottie

# Page Config
st.set_page_config(page_title="For Anisha Kanchii", page_icon="💐")

# CSS to fix the "invisible text" and center the surprise
st.markdown("""
    <style>
    .letter-box {
        background-color: #fffaf0;
        padding: 25px;
        border-radius: 15px;
        border: 2px solid #ffccd5;
        color: #333333 !important;
        margin-bottom: 20px;
    }
    h3, p { color: #d63384 !important; }
    .stButton>button {
        background-color: #d63384;
        color: white;
        border-radius: 20px;
    }
    </style>
""", unsafe_allow_html=True)

def load_lottie(url):
    try:
        r = requests.get(url)
        return r.json() if r.status_code == 200 else None
    except:
        return None

# Load the Surprise Bouquet (Hidden until button is clicked)
surprise_bouquet_url = "https://assets2.lottiefiles.com/packages/lf20_w51pcehl.json"
lottie_surprise = load_lottie(surprise_bouquet_url)

# 1. The Letter
st.markdown(f"""
<div class="letter-box">
    <h3>Dear Anisha Kanchii,</h3>
    <p>
    Just like these flowers, my appreciation for you keeps growing. 
    You make everything a bit more colorful and a lot more meaningful.
    <br><br>
    I coded this digital surprise to always stay in bloom for you. 
    Thank you for being exactly who you are.
    <br><br>
    <strong>Sincerely yours,</strong><br>
    Ryan
    </p>
</div>
""", unsafe_allow_html=True)

# 2. The Surprise Logic (No balloons, just the bouquet)
if st.button("Click for your bouquet! 💐"):
    if lottie_surprise:
        # This renders the big bouquet only after the click
        st_lottie(lottie_surprise, height=500, key="surprise_bloom")
        st.markdown("<h2 style='text-align:center; color:#d63384;'>For You!</h2>", unsafe_allow_html=True)
    else:
        st.error("The bouquet is taking a moment to bloom. Please refresh!")
