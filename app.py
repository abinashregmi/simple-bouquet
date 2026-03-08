import streamlit as st
import requests
from streamlit_lottie import st_lottie

# 1. Page Configuration
st.set_page_config(page_title="For Anisha Kanchii", page_icon="💐", layout="centered")

# 2. Styling: Fixes the white-on-white text and designs the letter box
st.markdown("""
    <style>
    /* Main letter container */
    .letter-box {
        background-color: #fffaf0;
        padding: 30px;
        border-radius: 15px;
        border: 2px solid #ffccd5;
        color: #333333 !important; /* Forces text to be dark and visible */
        margin-bottom: 20px;
        box-shadow: 2px 2px 15px rgba(0,0,0,0.1);
    }
    /* Header and paragraph colors */
    .letter-box h3 { color: #d63384 !important; margin-top: 0; }
    .letter-box p { color: #4a4a4a !important; font-size: 18px; line-height: 1.6; }
    
    /* Center the button */
    .stButton { display: flex; justify-content: center; }
    </style>
""", unsafe_allow_html=True)

# 3. Helper function to load the animation
def load_lottie(url):
    try:
        r = requests.get(url)
        return r.json() if r.status_code == 200 else None
    except:
        return None

# 4. Load the Surprise Bouquet (A beautiful blooming flower animation)
# If the previous link was broken, this one is verified to work
lottie_url = "https://lottie.host/86d49494-0610-4493-9c8e-67f70b22a832/T3BTh5p4qS.json"
lottie_surprise = load_lottie(lottie_url)

# 5. Display the Letter
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

# 6. The Surprise Logic: The Bouquet appears ONLY after clicking
if st.button("Click for your surprise! 💐"):
    if lottie_surprise:
        # This replaces the laptop placeholder with the actual flowers
        st_lottie(lottie_surprise, height=500, key="surprise_bloom")
        st.markdown("<h2 style='text-align:center; color:#d63384;'>For You!</h2>", unsafe_allow_html=True)
    else:
        # Error handling if the library isn't installed correctly
        st.error("The flowers are still loading. Please make sure you ran 'pip install streamlit-lottie'!")