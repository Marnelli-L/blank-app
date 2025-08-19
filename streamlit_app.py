import streamlit as st
from datetime import datetime

st.set_page_config(
    page_title="💖 Date Picker for Gwen",
    page_icon="💌",
    layout="centered",
    initial_sidebar_state="auto",
)

st.markdown(
    """
    <style>
    body {
        background: linear-gradient(135deg, #ffe0ef 0%, #fff0f6 100%);
    }
    .big-font {
        font-size:36px !important;
        color: #ff69b4;
        font-family: 'Comic Sans MS', cursive, sans-serif;
        text-align: center;
        margin-bottom: 10px;
    }
    .cute-box {
        background: #fff0f6;
        border-radius: 24px;
        padding: 36px 28px 28px 28px;
        margin-top: 24px;
        box-shadow: 0 6px 24px #ffe0ef;
        text-align: center;
    }
    .emoji {
        font-size: 54px;
        margin-bottom: 12px;
        text-align: center;
    }
    .subtitle {
        font-size: 22px !important;
        color: #d72660;
        font-family: 'Comic Sans MS', cursive, sans-serif;
        text-align: center;
        margin-bottom: 18px;
    }
    .footer {
        font-size: 16px;
        color: #bdbdbd;
        text-align: center;
        margin-top: 40px;
        font-family: 'Comic Sans MS', cursive, sans-serif;
    }
    .heart {
        color: #ff69b4;
        font-size: 22px;
        vertical-align: middle;
    }
    .option-list {
        font-size: 18px;
        color: #d72660;
        margin-bottom: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown('<div class="emoji">💌</div>', unsafe_allow_html=True)
st.markdown('<div class="big-font">Hey Love (GWEN CLAIRE SALAZAR CHAVEZ! 💕</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">I made this just for you.</div>', unsafe_allow_html=True)

st.markdown(
    """
    <div class="cute-box">
        <div class="emoji">🌸</div>
        <div style="font-size:20px; color:#d72660; font-family:'Comic Sans MS', cursive, sans-serif;">
            Would you like to go out with me? <br>
            Please pick where you'd like to go for our next date!
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

options = [
    "😉 Netflix and Chill",
    "🌳 Picnic in the Park",
    "☕ Headache Cafe",
    "🎳 Bowling",
    "🎨 Away Painting Session",
    "🍦 Ice Cream NANAMAN",
    "🛍️ Shopping Spree (WAG)",
    "🏞️ Nature Walk (AYAW KO)",
    "🍕 Pizza!!!!!",
    "🎤 Blackout Karaoke ulit?",
    "🌌 Stargazing"
]

choice = st.selectbox("Choose your favorite date idea:", options)

st.markdown(
    """
    <div class="option-list">
        
    </div>
    """,
    unsafe_allow_html=True,
)

if st.button("Send my choice! 💌"):
    st.markdown(
        f"""
        <div class="cute-box">
            <div class="emoji">🥰</div>
            <div class="big-font">Yay! Can't wait for our <b>{choice}</b> together!<br>
            I'll make it extra special for you. 💖</div>
            <div style="margin-top:18px; font-size:18px; color:#d72660;">
                Thank you for choosing!<br>
                I'll message you soon with the details. <span class="heart">💌</span>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.balloons()
else:
    st.markdown(
        """
        <div class="cute-box">
            <div class="emoji">💭</div>
            <div class="big-font">I'm so excited to see what you pick, Love! 😘</div>
            <div style="margin-top:12px; font-size:18px; color:#d72660;">
                No matter what you choose, every moment with you is my AWAY MOMENTS. 💗
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.markdown(
    f"""
    <div class="footer">
        Made with <span class="heart">♥</span> by NELLI, {datetime.now().strftime('%B %Y')}
    </div>
    """,
    unsafe_allow_html=True,
)
