import streamlit as st
import time
from moviepy.editor import VideoFileClip, vfx
import os

# Page Setup
st.set_page_config(page_title="AWAIS MAYO HACKER", layout="wide")

# 🟢 ULTRA HACKING CSS (Matrix Rain + Branding + Blur)
st.markdown("""
    <style>
    /* Full Screen Matrix Animation */
    .stApp {
        background: black url('https://media.giphy.com/media/o0vwzuFwCGAFO/giphy.gif');
        background-size: cover;
        background-attachment: fixed;
    }

    /* Floating Hacker Identity */
    .hacker-brand {
        position: fixed;
        top: 10px;
        left: 50%;
        transform: translateX(-50%);
        color: #00FF41;
        font-size: 20px;
        font-family: 'Courier New', monospace;
        font-weight: bold;
        text-shadow: 0 0 20px #00FF41;
        z-index: 9999;
        background: rgba(0,0,0,0.7);
        padding: 10px;
        border: 1px solid #00FF41;
        border-radius: 10px;
    }

    /* WhatsApp Button Styling */
    .wa-btn {
        display: inline-block;
        padding: 15px 30px;
        background-color: #25D366;
        color: white !important;
        border-radius: 50px;
        text-decoration: none;
        font-weight: bold;
        box-shadow: 0 0 20px #25D366;
        margin-top: 20px;
        transition: 0.3s;
    }
    .wa-btn:hover { transform: scale(1.1); box-shadow: 0 0 40px #25D366; }

    /* Terminal Styles */
    h1, h3 { color: #00FF41 !important; text-align: center; text-shadow: 0 0 10px #00FF41; }
    .stButton>button {
        background: transparent !important;
        color: #00FF41 !important;
        border: 2px solid #00FF41 !important;
        box-shadow: 0 0 15px #00FF41;
        font-size: 20px;
        width: 100%;
    }
    </style>

    <div class="hacker-brand">
        AWAIS MAYO HACKER | +923295533214
    </div>
    """, unsafe_allow_html=True)

# 🎵 Background Hacking Music
st.components.v1.html("""
    <iframe src="https://www.youtube.com/embed/Z_8G0zHMAS8?autoplay=1&mute=0" width="0" height="0" frameborder="0"></iframe>
""", height=0)

st.title("💀 AWAIS MAYO - ULTIMATE WATERMARK BLURRER 💀")

col1, col2 = st.columns(2)

with col1:
    st.markdown("### 📥 INJECT TARGET")
    vid_file = st.file_uploader("Upload Video", type=['mp4'])
    if st.button("🚀 EXECUTE BLUR SCRIPT"):
        if vid_file:
            with open("temp_in.mp4", "wb") as f:
                f.write(vid_file.read())
            
            with st.spinner(""):
                t = st.empty()
                log = ""
                for msg in ["> ACCESSING CORE...", "> TARGET: " + vid_file.name, "> BLURRING WATERMARK...", "> AUTHORIZING 923295533214...", "> SUCCESS!"]:
                    log += msg + "\n\n"
                    t.code(log, language="bash")
                    time.sleep(1)
                
                # 🛠️ REAL BLUR/CROP LOGIC
                clip = VideoFileClip("temp_in.mp4")
                # Watermark aksar corners pe hota hai, hum bottom 10% blur/crop kar rahe hain
                w, h = clip.size
                final = clip.crop(y1=0, y2=h-60) # Standard TikTok WM removal
                final.write_videofile("temp_out.mp4", codec="libx264")
                
                st.video("temp_out.mp4")
                st.success("CLEANED BY AWAIS MAYO HACKER")
        else:
            st.error("NO FILE DETECTED!")

with col2:
    st.markdown("### 📢 CONNECT WITH ME")
    st.write("Join my WhatsApp Channel for latest hacks and updates!")
    st.markdown("""
        <a href="https://whatsapp.com/channel/0029VbBzlMlIt5rzSeMBE922" target="_blank" class="wa-btn">
            🟢 JOIN WHATSAPP CHANNEL
        </a>
    """, unsafe_allow_html=True)
    st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNHJueW9ueXp0bm9ueXp0bm9ueXp0bm9ueXp0bm9ueXp0JmVwPXYxX2ludGVybmFsX2dpZl9ieV9pZCZjdD1n/o0vwzuFwCGAFO/giphy.gif")

