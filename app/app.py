import streamlit as st
import requests
from streamlit_lottie import st_lottie

# Page config for a "sweet" feel
st.set_page_config(page_title="A Special Surprise", page_icon="💐")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Lottie animation of a blooming bouquet
lottie_flowers = load_lottieurl("https://assets2.lottiefiles.com/packages/lf20_mDnmhAgZkb.json")

# Layout
st.title("A Little Something for You...")

# Display the animated bouquet
if lottie_flowers:
    st_lottie(lottie_flowers, height=400, key="flowers")

st.markdown("---")

# The Letter
st.markdown("""
### Dear Girlfriend,

I wanted to send you something that wouldn't wither and would brighten your day every time you open it. 

Just like these flowers, my appreciation for you keeps growing. You make everything a bit more colorful and a lot more meaningful. Thank you for being exactly who you are.

**Sincerely yours,**
[Your Name]
""")

# Optional: Add some celebratory balloons when they reach the bottom
if st.button("Click for a surprise!"):
    st.balloons()
