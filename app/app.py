import streamlit as st
import requests
from streamlit_lottie import st_lottie
import time

# --- Page Config ---
st.set_page_config(page_title="A Special Surprise", page_icon="💐")

# --- Updated CSS for Visibility ---
# I've changed the text color to a dark gray/pink so it shows up on the light background
st.markdown("""
    <style>
    .letter-body { 
        background-color: #fffaf0; 
        padding: 25px; 
        border-radius: 10px; 
        border: 2px solid #ffccd5; 
        color: #4a4a4a !important; 
    }
    .letter-body h3, .letter-body p {
        color: #d63384 !important; /* Dark pink for contrast */
    }
    </style>
""", unsafe_allow_html=True)

def load_lottieurl(url):
    try:
        r = requests.get(url)
        return r.json() if r.status_code == 200 else None
    except:
        return None

# URLs for the bouquets
main_url = "https://assets5.lottiefiles.com/packages/lf20_mDnmhAgZkb.json"
surprise_url = "https://assets2.lottiefiles.com/packages/lf20_w51pcehl.json"

lottie_main = load_lottieurl(main_url)
lottie_surprise = load_lottieurl(surprise_url)

# Display Top Bouquet
if lottie_main:
    st_lottie(lottie_main, height=300, key="main")

# The Letter with explicit color styles
st.markdown(f"""
<div class="letter-body">
    <h3>Dear Anisha Kanchii,</h3>
    <p>
    Just like these flowers, my appreciation for you keeps growing. You make everything a 
    bit more colorful and a lot more meaningful.
    <br><br>
    Since I can't be there to give you a real bouquet right this second, I coded this 
    digital one to always stay in bloom for you. Thank you for being exactly who you are.
    <br><br>
    <strong>Sincerely yours,</strong><br>
    Ryan
    </p>
</div>
""", unsafe_allow_html=True)

if st.button("Click for an extra surprise! 💖"):
    st.balloons()
    if lottie_surprise:
        st_lottie(lottie_surprise, height=400, key="surprise")
    st.markdown("<h2 style='text-align:center; color:#d63384;'>A gift for you!</h2>", unsafe_allow_html=True)
