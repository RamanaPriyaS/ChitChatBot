import streamlit as st
import google.generativeai as genai

# ✅ Step 1: Configure API Key (from Makersuite)
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])  

# ✅ Step 2: Use Gemini Flash 2.5 model
model = genai.GenerativeModel("models/gemini-1.5-flash-latest")

# ✅ Step 3: Setup persistent chat session
if "chat" not in st.session_state:
    st.session_state.chat = model.start_chat(history=[])

if "messages" not in st.session_state:
    st.session_state.messages = []

# ✅ Step 4: Streamlit UI
st.set_page_config(page_title="Rp",page_icon="😜")
st.markdown("""
<h1>AI Assisted Chatbot</h1>
<p style='font-size:18px; color:gray;'>Powered by RP</p>""", unsafe_allow_html=True)

# Show previous chat
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Input box
user_input = st.chat_input("Ask me anything...")

if user_input:
    st.chat_message("user").markdown(user_input)
    st.session_state.messages.append({"role": "user", "content": user_input})

    try:
        response = st.session_state.chat.send_message(user_input)
        bot_reply = response.text
        print(response)
        st.chat_message("assistant").markdown(bot_reply)
        st.session_state.messages.append({"role": "assistant", "content": bot_reply})
    except Exception as e:
        st.error(f"⚠️ Error: {e}")
