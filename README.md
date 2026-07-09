                                                         Voice-Genie-Ai

https://shaikhadil00-voice-gen-ai-app-f7itfi.streamlit.app/

VoiceGenie AI is a smart, voice-powered assistant prototype that transforms natural speech into meaningful actions using speech recognition and rule-based NLP. It enables hands-free web automation, personalized movie recommendations via OMDB API, real-time info display, and demo banking simulations. Built with Python, Streamlit, Whisper AI, and a content-based ML recommender system, VoiceGenie converts intent into action with high accuracy. Future plans include live banking APIs, biometric voice authentication, advanced conversational AI, and deployment on mobile and wearable devices — aiming to become a complete AI-powered personal assistant for daily life and financial management.

                                                      command to say in voice

Hello

Open Google

Open YouTube

I want to watch a movie

Check my balance

Transfer money

Show transaction history

What is the time?

What is today's date?

Note: The banking features use mock/demo data for demonstration purposes only and do not connect to any real bank or payment system.

<img width="1326" height="585" alt="image" src="https://github.com/user-attachments/assets/914f723f-a249-440a-871c-dc18fc5cb53a" />


if u want to host localy just change action engine with this 

# -------------------------
# ACTION ENGINE
# -------------------------
def execute_action(intent):

    if intent == "open_youtube":
        st.markdown('<div class="custom-box">Opening YouTube...</div>', unsafe_allow_html=True)
        webbrowser.open("https://youtube.com")

    elif intent == "open_google":
        st.markdown('<div class="custom-box">Opening Google...</div>', unsafe_allow_html=True)
        webbrowser.open("https://google.com")

    elif intent == "open_movie_app":
        st.markdown('<div class="custom-box">🎬 Opening Movie Recommender...</div>', unsafe_allow_html=True)
        webbrowser.open("https://movie-recommendation-system-r5kpzip4ebajza7qemsryp.streamlit.app/")

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
        st.markdown('<div class="custom-box">📜 Last Transactions:</div>', unsafe_allow_html=True)

        for t in transactions:
            st.markdown(f'<div class="custom-box">➡ {t}</div>', unsafe_allow_html=True)

    elif intent == "tell_time":
        now = datetime.datetime.now().strftime("%H:%M:%S")
        st.markdown(f'<div class="custom-box">Current Time: {now}</div>', unsafe_allow_html=True)

    elif intent == "tell_date":
        today = datetime.datetime.now().strftime("%d %B %Y")
        st.markdown(f'<div class="custom-box">Today\'s Date: {today}</div>', unsafe_allow_html=True)

    elif intent == "greeting":
        st.markdown('<div class="custom-box">Hello! How can I help you?</div>', unsafe_allow_html=True)

    else:
        st.markdown('<div class="custom-box">Command not recognized.</div>', unsafe_allow_html=True)
