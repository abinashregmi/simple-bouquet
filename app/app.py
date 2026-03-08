import streamlit as st
import requests
from streamlit_lottie import st_lottie

# Page config
st.set_page_config(page_title="For Anisha Kanchii", page_icon="💐")

# CSS to fix invisible text and style the letter
st.markdown("""
    <style>
    .letter-box {
        background-color: #fffaf0;
        padding: 30px;
        border-radius: 15px;
        border: 2px solid #ffccd5;
        color: #333333 !important; /* Forces text to be dark */
        margin-bottom: 20px;
        font-family: 'Arial';
    }
    .letter-box h3 { color: #d63384 !important; }
    .letter-box p { color: #4a4a4a !important; font-size: 18px; }
    </style>
""", unsafe_allow_html=True)

def load_lottie(url):
    try:
        r = requests.get(url)
        return r.json() if r.status_code == 200 else None
    except:
        return None

# Load the Surprise Bouquet
lottie_surprise = load_lottie("https://assets2.lottiefiles.com/packages/lf20_w51pcehl.json")

# Display the Letter
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

# The Surprise Logic
if st.button("Click for your surprise! 💐"):
    if lottie_surprise:
        # This replaces the balloons with the actual bouquet animation
        st_lottie(lottie_surprise, height=500, key="surprise_bloom")
        st.markdown("<h2 style='text-align:center; color:#d63384;'>For You!</h2>", unsafe_allow_html=True)
    else:
        # If the library still isn't working, this error will show instead of the laptop
        st.error("The bouquet animation is still loading. Please check your requirements.txt!")
