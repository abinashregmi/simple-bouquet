import streamlit as st

# 1. Page Configuration
st.set_page_config(page_title="For Anisha Kanchii", page_icon="🎈")

# 2. Styling: High-contrast text so she can read it perfectly
st.markdown("""
    <style>
    .letter-box {
        background-color: #fffaf0;
        padding: 30px;
        border-radius: 15px;
        border: 2px solid #ffccd5;
        color: #1a1a1a !important; /* Forces dark text */
        text-align: center;
        margin-bottom: 20px;
        box-shadow: 2px 2px 12px rgba(0,0,0,0.1);
    }
    .letter-box h3 { color: #d63384 !important; font-size: 28px; }
    .letter-box p { color: #333333 !important; font-size: 20px; line-height: 1.6; }
    
    /* Center the button */
    .stButton { display: flex; justify-content: center; }
    </style>
""", unsafe_allow_html=True)

# 3. The Letter Content
st.markdown(f"""
<div class="letter-box">
    <h3>Dear Anisha Kanchii,</h3>
    <p>
    Just like the flowers, my appreciation for you keeps growing. 
    You make everything a bit more colorful and a lot more meaningful.
    <br><br>
    I coded this little surprise just for you to show how much I appreciate you. 
    Thank you for being exactly who you are.
    <br><br>
    <strong>Sincerely yours,</strong><br>
    Ryan
    </p>
</div>
""", unsafe_allow_html=True)

# 4. The Surprise Logic: Works every time!
if st.button("Click for your surprise! 🎈"):
    st.balloons()
    st.snow() # Adding a touch of magic
    st.markdown("<h2 style='text-align:center; color:#d63384;'>Sending you lots of love! ❤️</h2>", unsafe_allow_html=True)
