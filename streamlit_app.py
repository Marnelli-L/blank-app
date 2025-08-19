import streamlit as st

st.set_page_config(
    page_title="💖 Date Night Picker",
    page_icon="💌",
    layout="centered",
    initial_sidebar_state="auto",
)

st.markdown(
    """
    <style>
    .big-font {
        font-size:32px !important;
        color: #ff69b4;
        font-family: 'Comic Sans MS', cursive, sans-serif;
    }
    .cute-box {
        background: #fff0f6;
        border-radius: 20px;
        padding: 30px;
        margin-top: 20px;
        box-shadow: 0 4px 16px #ffe0ef;
    }
    .emoji {
        font-size: 48px;
        margin-bottom: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown('<div class="emoji">💌</div>', unsafe_allow_html=True)
st.markdown('<div class="big-font">Hey love! 💕</div>', unsafe_allow_html=True)
st.write("Would you like to go out with me? Please pick where you'd like to go for our next date! 🌸")

options = [
    "🍣 Sushi Night",
    "🎬 Movie & Popcorn",
    "🌳 Picnic in the Park",
    "☕ Cozy Cafe",
    "🎳 Bowling Fun",
    "🎨 Art Gallery",
    "🍦 Ice Cream Adventure",
    "🛍️ Shopping Spree",
    "🏞️ Nature Walk",
    "🍕 Pizza Party"
]

choice = st.selectbox("Choose your favorite date idea:", options)

if st.button("Send my choice! 💌"):
    st.markdown(
        f"""
        <div class="cute-box">
            <div class="emoji">🥰</div>
            <div class="big-font">Yay! Can't wait for our <b>{choice}</b> together!<br>
            I'll make it extra special for you. 💖</div>
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
            <div class="big-font">I'm so excited to see what you pick! 😘</div>
        </div>
        """,
        unsafe_allow_html=True,
    )
