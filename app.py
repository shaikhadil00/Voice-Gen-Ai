import streamlit as st
import whisper
import tempfile
import webbrowser
import datetime
import os

# -------------------------
# PAGE CONFIG
# -------------------------
st.set_page_config(
    page_title="VoiceGenie AI",
    page_icon="🎙",
    layout="centered"
)

# -------------------------
# PREMIUM DARK UI
# -------------------------
st.markdown("""
<style>

/* FULL BACKGROUND */
.stApp {
    background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
    background-attachment: fixed;
    color: white;
}

/* TITLE */
.big-title {
    font-size: clamp(60px, 6vw, 80px);
    font-weight: 900;
    text-align: center;
    color: white;
    letter-spacing: 2px;
    text-shadow: 
        0px 0px 15px rgba(255,255,255,0.6),
        0px 0px 35px rgba(0,200,255,0.5);
}

.sub-text {
    text-align: center;
    font-size: 20px;
    color: #e0e0e0;
    margin-bottom: 30px;
}

/* AUDIO INPUT BOX */
[data-testid="stAudioInput"] {
    background: rgba(0, 0, 0, 0.8);
    padding: 25px;
    border-radius: 25px;
    border: 1px solid rgba(255,255,255,0.2);
    box-shadow: 0px 15px 35px rgba(0,0,0,0.6);
}

/* AUDIO LABEL */
[data-testid="stAudioInput"] label {
    color: white !important;
    font-size: 22px !important;
    font-weight: 600 !important;
}

/* CUSTOM MESSAGE BOX */
.custom-box {
    background: rgba(255,255,255,0.08);
    padding: 18px;
    border-radius: 18px;
    font-size: 20px;
    color: white;
    margin-top: 15px;
    box-shadow: 0px 8px 25px rgba(0,0,0,0.5);
}

/* REMOVE FOOTER */
footer {visibility: hidden;}

</style>
""", unsafe_allow_html=True)

# -------------------------
# TITLE
# -------------------------
st.markdown('<p class="big-title">🎙 VoiceGenie AI</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-text">Universal Smart NLP Voice Assistant</p>', unsafe_allow_html=True)
st.divider()

# -------------------------
# LOAD MODEL
# -------------------------
@st.cache_resource
def load_model():
    return whisper.load_model("tiny")

with st.spinner("🔄 Loading AI Model..."):
    model = load_model()

st.markdown('<div class="custom-box">AI Model Ready!</div>', unsafe_allow_html=True)

# -------------------------
# MOCK BANK DATA
# -------------------------
user_account = {
    "name": "Adil",
    "balance": 50000
}

transactions = [
    "Paid ₹2000 to Amazon",
    "Received ₹5000 from Friend",
    "Recharge ₹299"
]

# -------------------------
# MIC INPUT
# -------------------------
audio_value = st.audio_input("🎤 Click and Speak")

# -------------------------
# INTENT DETECTION
# -------------------------
def detect_intent(text):
    text = text.lower()

    if "youtube" in text:
        return "open_youtube"

    elif "google" in text:
        return "open_google"

    elif "movie" in text or "watch" in text:
        return "open_movie_app"

    elif "balance" in text:
        return "check_balance"

    elif "transfer" in text or "send money" in text:
        return "transfer_money"

    elif "transaction" in text or "history" in text:
        return "transaction_history"

    elif "time" in text:
        return "tell_time"

    elif "date" in text:
        return "tell_date"

    elif "hello" in text or "hey" in text:
        return "greeting"

    else:
        return "unknown"

# -------------------------
# ACTION ENGINE
# -------------------------
def execute_action(intent):

    if intent == "open_youtube":
        st.markdown(
            '<div class="custom-box">▶️ Click the button below to open YouTube.</div>',
            unsafe_allow_html=True
        )
        st.link_button("▶️ Open YouTube", "https://youtube.com")

    elif intent == "open_google":
        st.markdown(
            '<div class="custom-box">🌐 Click the button below to open Google.</div>',
            unsafe_allow_html=True
        )
        st.link_button("🌐 Open Google", "https://google.com")

    elif intent == "open_movie_app":
        st.markdown(
            '<div class="custom-box">🎬 Click the button below to open the Movie Recommender.</div>',
            unsafe_allow_html=True
        )
        st.link_button(
            "🎬 Open Movie Recommender",
            "https://movie-recommendation-system-r5kpzip4ebajza7qemsryp.streamlit.app/"
        )

    elif intent == "check_balance":
        st.markdown(
            f'<div class="custom-box">💰 Your balance is ₹{user_account["balance"]}</div>',
            unsafe_allow_html=True
        )

    elif intent == "transfer_money":
        amount = 5000
        user_account["balance"] -= amount
        transactions.insert(0, f"Transferred ₹{amount} to Account B")

        st.markdown(
            f'<div class="custom-box">💸 Transferred ₹{amount}. Remaining balance: ₹{user_account["balance"]}</div>',
            unsafe_allow_html=True
        )

    elif intent == "transaction_history":
        st.markdown(
            '<div class="custom-box">📜 Last Transactions:</div>',
            unsafe_allow_html=True
        )

        for t in transactions:
            st.markdown(
                f'<div class="custom-box">➡ {t}</div>',
                unsafe_allow_html=True
            )

    elif intent == "tell_time":
        now = datetime.datetime.now().strftime("%H:%M:%S")
        st.markdown(
            f'<div class="custom-box">Current Time: {now}</div>',
            unsafe_allow_html=True
        )

    elif intent == "tell_date":
        today = datetime.datetime.now().strftime("%d %B %Y")
        st.markdown(
            f'<div class="custom-box">Today\'s Date: {today}</div>',
            unsafe_allow_html=True
        )

    elif intent == "greeting":
        st.markdown(
            '<div class="custom-box">Hello! How can I help you?</div>',
            unsafe_allow_html=True
        )

    else:
        st.markdown(
            '<div class="custom-box">Command not recognized.</div>',
            unsafe_allow_html=True
        )
# -------------------------
# PROCESS AUDIO
# -------------------------
if audio_value is not None:

    with st.spinner("🧠 Processing your voice..."):

        with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp_file:
            tmp_file.write(audio_value.getvalue())
            temp_path = tmp_file.name

        try:
            result = model.transcribe(temp_path, fp16=False)
            text = result["text"].strip()

            if text == "":
                st.markdown('<div class="custom-box">No speech detected. Speak clearly and try again.</div>', unsafe_allow_html=True)
            else:
                st.markdown(f'<div class="custom-box">You said: {text}</div>', unsafe_allow_html=True)
                intent = detect_intent(text)
                execute_action(intent)

        except Exception as e:
            st.markdown(f'<div class="custom-box">Error: {e}</div>', unsafe_allow_html=True)

        finally:
            if os.path.exists(temp_path):
                os.remove(temp_path)

st.markdown("---")
