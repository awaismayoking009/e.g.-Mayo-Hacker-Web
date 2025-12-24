import streamlit as st
import time

# Page Configuration
st.set_page_config(page_title="AWAIS MAYO HACKER", layout="wide")

# CSS for Matrix Rain, Danger Icons, and Pulsing Identity
st.markdown("""
    <style>
    /* Full Black Background with Matrix GIF */
    .stApp {
        background-color: #000000 !important;
        background-image: url('https://media.giphy.com/media/o0vwzuFwCGAFO/giphy.gif');
        background-size: cover;
        background-attachment: fixed;
    }

    /* Hacking Green Text Glow */
    h1, h2, h3, p, label, .stMarkdown {
        color: #00FF41 !important;
        font-family: 'Courier New', monospace !important;
        text-shadow: 0 0 12px #00FF41;
        text-align: center;
    }

    /* Identity Box: Awais Mayo Hacker 923295533214 */
    .hacker-identity {
        position: fixed;
        top: 20px;
        right: 20px;
        border: 2px solid #00FF41;
        padding: 15px;
        background: rgba(0, 40, 0, 0.9);
        color: #00FF41;
        z-index: 10000;
        font-weight: bold;
        box-shadow: 0 0 20px #00FF41;
        animation: blink 1s infinite;
        font-size: 14px;
        border-radius: 5px;
    }

    @keyframes blink {
        0% { opacity: 1; border-color: #00FF41; }
        50% { opacity: 0.7; border-color: #ff0000; } /* Subtle red alert flash */
        100% { opacity: 1; border-color: #00FF41; }
    }

    /* Professional Terminal Box */
    .stCodeBlock {
        border: 1px solid #00FF41 !important;
        box-shadow: 0 0 10px #00FF41;
    }

    /* Hacking Button */
    .stButton>button {
        background: linear-gradient(to bottom, #003300, #000000) !important;
        color: #00FF41 !important;
        border: 2px solid #00FF41 !important;
        font-size: 22px !important;
        font-weight: bold !important;
        height: 60px !important;
        width: 100% !important;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background: #00FF41 !important;
        color: #000000 !important;
        box-shadow: 0 0 30px #00FF41;
    }
    </style>

    <div class="hacker-identity">
        SYSTEM OWNER: AWAIS MAYO HACKER<br>
        SECURE LINE: +923295533214<br>
        STATUS: BYPASSING WATERMARK...
    </div>

    <iframe src="https://www.youtube.com/embed/5K1R0ToE6vE?autoplay=1&mute=0" width="0" height="0" frameborder="0"></iframe>
    """, unsafe_allow_html=True)

st.markdown("# 💀 AWAIS MAYO HACKER - CENTRAL COMMAND 💀")
st.write("### [ SECURITY LEVEL: CLASSIFIED ]")

col1, col2 = st.columns(2)

with col1:
    st.markdown("### 📥 INJECT SOURCE")
    uploaded_file = st.file_uploader("", type=['mp4', 'mov'])
    execute = st.button("🚀 EXECUTE HACK_REMOVER.EXE")

with col2:
    st.markdown("### 📟 TERMINAL LOGS")
    terminal = st.empty()
    
    if execute and uploaded_file:
        progress_text = ""
        steps = [
            "> INITIALIZING AWAIS MAYO HACKING CORE...",
            "> ESTABLISHING ENCRYPTED TUNNEL...",
            "> TARGET: " + uploaded_file.name,
            "> BYPASSING METADATA PROTOCOLS...",
            "> REMOVING WATERMARK SIGNATURES...",
            "> [923295533214] AUTHORIZATION GRANTED...",
            "> SYSTEM OVERRIDE SUCCESSFUL!"
        ]
        
        for s in steps:
            progress_text += s + "\n\n"
            terminal.code(progress_text, language="bash")
            time.sleep(1.2)
        
        st.video(uploaded_file)
    elif execute:
        st.error("FATAL ERROR: NO DATA INPUT DETECTED")
