import streamlit as st
import time
from moviepy.editor import VideoFileClip, vfx
import os

# Page Setup
st.set_page_config(page_title="AWAIS MAYO HACKER", layout="wide")

# 🟢 MATRIX RAIN + BRANDING + WHATSAPP BUTTON CSS
st.markdown("""
    <style>
    /* Background Matrix Animation */
    .stApp {
        background: black url('https://media.giphy.com/media/o0vwzuFwCGAFO/giphy.gif') !important;
        background-size: cover !important;
        background-attachment: fixed !important;
    }

    /* Floating Hacker ID */
    .hacker-brand {
        position: fixed; top: 10px; right: 10px;
        color: #00FF41; font-size: 18px; font-family: 'Courier New', monospace;
        font-weight: bold; text-shadow: 0 0 15px #00FF41;
        z-index: 9999; background: rgba(0,20,0,0.8);
        padding: 10px; border: 1px solid #00FF41; border-radius: 5px;
        animation: blinker 1.5s linear infinite;
    }
    @keyframes blinker { 50% { opacity: 0.3; } }

    /* Button & Text Styles */
    h1, h3 { color: #00FF41 !important; text-align: center; text-shadow: 0 0 10px #00FF41; }
    .wa-btn {
        display: block; width: 250px; margin: 20px auto; padding: 15px;
        background-color: #25D366; color: white !important;
        text-align: center; border-radius: 50px; font-weight: bold;
        text-decoration: none; box-shadow: 0 0 20px #25D366;
    }
    </style>
    <div class="hacker-brand">AWAIS MAYO HACKER<br>+923295533214</div>
    """, unsafe_allow_html=True)

# 🎵 Hacking Music (Silent Video for Audio)
st.components.v1.html("""
    <iframe width="0" height="0" src="https://www.youtube.com/embed/Z0p_M-3YmFw?autoplay=1&mute=0" frameborder="0" allow="autoplay"></iframe>
""", height=0)

st.title("🛡️ AWAIS MAYO - ULTIMATE WATERMARK BLURRER 🛡️")

# WhatsApp Channel Button
st.markdown('<a href="https://whatsapp.com/channel/0029VbBzlMlIt5rzSeMBE922" target="_blank" class="wa-btn">🟢 JOIN WHATSAPP CHANNEL</a>', unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown("### 📥 UPLOAD TARGET")
    vid_file = st.file_uploader("", type=['mp4'])
    if st.button("🚀 EXECUTE BLUR SCRIPT"):
        if vid_file:
            with open("temp_in.mp4", "wb") as f:
                f.write(vid_file.read())
            
            log_box = st.empty()
            log_text = "> INITIALIZING CORE...\n\n"
            log_box.code(log_text, language="bash")
            
            try:
                # 🛠️ REAL BLUR/CROP LOGIC
                clip = VideoFileClip("temp_in.mp4")
                w, h = clip.size
                # Watermark aksar corners mein hota hai, hum bottom area ko crop kar ke video clean kar rahe hain
                # Is se TikTok logo mukammal khatam ho jayega
                final = clip.crop(y1=0, y2=h-70) 
                
                log_text += "> BYPASSING SECURITY...\n> WATERMARK NEUTRALIZED...\n> GENERATING CLEAN FILE..."
                log_box.code(log_text, language="bash")
                
                final.write_videofile("temp_out.mp4", codec="libx264", audio_codec="aac")
                st.video("temp_out.mp4")
                st.success("DECRYPTION SUCCESSFUL!")
            except Exception as e:
                st.error(f"SYSTEM FAILURE: {e}")
        else:
            st.error("NO TARGET DETECTED!")

with col2:
    st.markdown("### 📟 LIVE TERMINAL")
    st.image("https://media.giphy.com/media/o0vwzuFwCGAFO/giphy.gif", caption="SYSTEM_LOGS_ACTIVE")
