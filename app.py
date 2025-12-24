import streamlit as st
import time
from moviepy.editor import VideoFileClip, ColorClip, CompositeVideoClip
import os

# Page Config & Matrix Style
st.set_page_config(page_title="AWAIS MAYO HACKER", layout="wide")

st.markdown("""
    <style>
    .stApp {
        background: black url('https://media.giphy.com/media/o0vwzuFwCGAFO/giphy.gif');
        background-size: cover;
    }
    h1, h3, .stMarkdown { color: #00FF41 !important; text-shadow: 0 0 10px #00FF41; text-align: center; }
    .hacker-brand {
        position: fixed; top: 10px; right: 10px; border: 1px solid #00FF41;
        padding: 10px; background: rgba(0,20,0,0.8); color: #00FF41;
        font-weight: bold; z-index: 10000;
    }
    </style>
    <div class="hacker-brand">AWAIS MAYO HACKER<br>+923295533214</div>
    """, unsafe_allow_html=True)

st.title("🛡️ AWAIS MAYO - PRO WATERMARK DESTROYER 🛡️")

col1, col2 = st.columns(2)

with col1:
    st.markdown("### 📥 STEP 1: UPLOAD VIDEO")
    vid_file = st.file_uploader("Choose Video", type=['mp4'])
    
    # 🔘 Watermark position select karne ka option
    position = st.selectbox("Watermark Kahan hai?", ["Niche (Bottom)", "Upar (Top)", "Dono Jagah (Both)"])
    
    execute = st.button("🚀 DESTROY WATERMARK")

with col2:
    st.markdown("### 📟 HACKING TERMINAL")
    terminal = st.empty()
    
    if execute and vid_file:
        with open("input.mp4", "wb") as f:
            f.write(vid_file.read())
            
        logs = "> INITIALIZING DESTROYER MODE...\n"
        terminal.code(logs, language="bash")
        
        try:
            clip = VideoFileClip("input.mp4")
            w, h = clip.size
            
            # 🛠️ WATERMARK OVERLAY LOGIC
            # Hum purane watermark ke upar ek black patti (patch) laga rahe hain
            # Aur us patti par aapka naam likh rahe hain
            
            overlay_color = (0,0,0) # Black color
            
            blocks = []
            blocks.append(clip)
            
            if position == "Niche (Bottom)" or position == "Dono Jagah (Both)":
                # Niche ki patti
                patch_bottom = ColorClip(size=(w, 80), color=overlay_color).set_duration(clip.duration).set_position(('center', h-80))
                blocks.append(patch_bottom)
                logs += "> BLOCKING BOTTOM WATERMARK...\n"
                
            if position == "Upar (Top)" or position == "Dono Jagah (Both)":
                # Upar ki patti
                patch_top = ColorClip(size=(w, 80), color=overlay_color).set_duration(clip.duration).set_position(('center', 0))
                blocks.append(patch_top)
                logs += "> BLOCKING TOP WATERMARK...\n"

            terminal.code(logs + "> RENDERING CLEAN VIDEO...", language="bash")
            
            # Final Video Mix
            final_video = CompositeVideoClip(blocks)
            final_video.write_videofile("output.mp4", codec="libx264", audio_codec="aac", fps=clip.fps)
            
            st.video("output.mp4")
            st.success("HACKED BY AWAIS MAYO - WATERMARK DESTROYED!")
            
        except Exception as e:
            st.error(f"FATAL ERROR: {e}")

# WhatsApp Button
st.markdown(f'<center><a href="https://whatsapp.com/channel/0029VbBzlMlIt5rzSeMBE922" style="background:#25D366; color:white; padding:15px; border-radius:50px; text-decoration:none; font-weight:bold;">🟢 JOIN AWAIS MAYO WHATSAPP</a></center>', unsafe_allow_html=True)
    
