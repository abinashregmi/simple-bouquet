import streamlit as st
import requests
from streamlit_lottie import st_lottie
import time

# --- Page Config & Styling ---
st.set_page_config(page_title="A Special Surprise for You", page_icon="💐", layout="centered")

# Custom CSS for spacing and text focus
st.markdown("""
    <style>
    .big-font { font-size:18px !important; line-height: 1.6; }
    .title-text { text-align: center; color: #d63384; }
    .letter-body { background-color: #fffaf0; padding: 25px; border-radius: 10px; border: 1px solid #ffccd5; margin-bottom: 20px;}
    </style>
""", unsafe_allow_html=True)


# --- Helper Function to Load Lottie ---
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


# --- Load Animation URLs ---
# 1. Main header bouquet
lottie_flowers_main = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_mDnmhAgZkb.json")

# 2. Surprise blooming bouquet animation (triggered by button)
lottie_surprise_bouquet = load_lottieurl("https://assets2.lottiefiles.com/packages/lf20_w51pcehl.json")


# --- App Content ---
st.markdown("<h1 class='title-text'>A Little Something for You...</h1>", unsafe_allow_html=True)

# Main Bouquet Animation
if lottie_flowers_main:
    st_lottie(lottie_flowers_main, height=350, speed=1, loop=True, quality="high", key="main_flowers")

# --- The Letter ---
st.markdown("""
<div class="letter-body">
    <h3>Dear Anisha Kanchii,</h3>
    <p class="big-font">
    Just like these flowers, my appreciation for you keeps growing. You make everything a bit more colorful and a lot more meaningful.
    <br><br>
    Since I can't be there to give you a real bouquet right this second, I coded this digital one to always stay in bloom for you. Thank you for being exactly who you are.
    <br><br>
    **Sincerely yours,**<br>
    Ryan
    </p>
</div>
""", unsafe_allow_html=True)

# --- Surprise Button and Animation ---
st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)
if st.button("Click for an extra surprise! 💖", help="Click to see your gift bloom!"):
    st.balloons() # We'll keep a quick balloon burst, but focus on the bouquet
    
    # Empty space to clear old layout and center the surprise
    placeholder = st.empty()
    
    with placeholder.container():
        st.markdown("<h2 class='title-text'>A gift for you!</h2>", unsafe_allow_html=True)
        # Display the surprise bouquet - make it larger and not looping (bloom once then stop on final frame)
        st_lottie(lottie_surprise_bouquet, height=600, speed=0.8, loop=False, quality="high", key="surprise_flowers")
        time.sleep(1) # Small pause for effect
        st.markdown("<h3 style='text-align: center;'>Thinking of you always.</h3>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)
