import streamlit as st
import cv2
import numpy as np
import tempfile
import os

# 🟢 HACKING INTERFACE CSS
st.set_page_config(page_title="AWAIS MAYO AI TERMINAL", layout="wide")
st.markdown("""
    <style>
    .stApp { background: black url('https://media.giphy.com/media/o0vwzuFwCGAFO/giphy.gif'); background-size: cover; }
    h1, h3, p { color: #00FF41 !important; text-shadow: 0 0 10px #00FF41; text-align: center; }
    .hacker-brand { position: fixed; top: 10px; right: 10px; border: 1px solid #00FF41; padding: 10px; background: rgba(0,20,0,0.8); color: #00FF41; font-weight: bold; }
    </style>
    <div class="hacker-brand">AWAIS MAYO HACKER<br>+923295533214</div>
    """, unsafe_allow_html=True)

st.title("💀 AWAIS MAYO - DIRECT AI REMOVER 💀")

uploaded_file = st.file_uploader("Upload Video", type=["mp4", "mov"])

if uploaded_file:
    # Save input video
    tfile = tempfile.NamedTemporaryFile(delete=False) 
    tfile.write(uploaded_file.read())
    
    st.video(tfile.name)
    
    st.markdown("### ⚙️ DECRYPTION SETTINGS")
    # User se puchenge ke watermark kahan hai
    side = st.radio("Watermark ki Location select karein:", ("Niche (Bottom)", "Upar (Top)"))
    
    if st.button("🚀 EXECUTE AI REMOVAL"):
        cap = cv2.VideoCapture(tfile.name)
        fps = cap.get(cv2.CAP_PROP_FPS)
        width  = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        
        # Output Setup
        out_path = "cleaned_by_mayo.mp4"
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        out = cv2.VideoWriter(out_path, fourcc, fps, (width, height))
        
        bar = st.progress(0)
        total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        
        count = 0
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret: break
            
            # 🧠 AI INPAINTING LOGIC
            # Hum ek mask (patti) banayenge jo watermark ko cover karegi
            mask = np.zeros((height, width), dtype=np.uint8)
            
            if side == "Niche (Bottom)":
                cv2.rectangle(mask, (0, height-80), (width, height), 255, -1)
            else:
                cv2.rectangle(mask, (0, 0), (width, 80), 255, -1)
            
            # Ye function watermark ko mita kar aas paas ke pixels bhar dega
            # Isse "Telea" algorithm kehte hain (AI ki tarah kaam karta hai)
            clean_frame = cv2.inpaint(frame, mask, 3, cv2.INPAINT_TELEA)
            
            out.write(clean_frame)
            count += 1
            if count % 10 == 0: bar.progress(count / total_frames)
            
        cap.release()
        out.release()
        
        st.success("✅ SYSTEM DECRYPTED SUCCESSFULLY!")
        st.video(out_path)
        with open(out_path, "rb") as f:
            st.download_button("📥 DOWNLOAD CLEAN VIDEO", f, file_name="Awais_Mayo_Clean.mp4")

# WhatsApp Channel Link
st.markdown('<center><a href="https://whatsapp.com/channel/0029VbBzlMlIt5rzSeMBE922" style="background:#25D366; color:white; padding:15px; border-radius:50px; text-decoration:none; font-weight:bold;">🟢 JOIN MY WHATSAPP CHANNEL</a></center>', unsafe_allow_html=True)

