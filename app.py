import streamlit as st
import cv2
import numpy as np
import tempfile
import os

# --- Awais Mayo Hacking Style CSS ---
st.set_page_config(page_title="AWAIS MAYO - AI AREA SELECTOR", layout="wide")
st.markdown("""
    <style>
    .stApp { background: black url('https://media.giphy.com/media/o0vwzuFwCGAFO/giphy.gif'); background-size: cover; }
    h1, h3, p { color: #00FF41 !important; text-shadow: 0 0 10px #00FF41; text-align: center; }
    .hacker-brand { position: fixed; top: 10px; right: 10px; border: 1px solid #00FF41; padding: 10px; background: rgba(0,20,0,0.8); color: #00FF41; font-weight: bold; z-index: 1000; }
    </style>
    <div class="hacker-brand">AWAIS MAYO HACKER<br>+923295533214</div>
    """, unsafe_allow_html=True)

st.title("🛡️ AWAIS MAYO - PRECISION AI ERASER 🛡️")

uploaded_file = st.file_uploader("Video Upload Karein", type=["mp4", "mov"])

if uploaded_file:
    tfile = tempfile.NamedTemporaryFile(delete=False, suffix=".mp4")
    tfile.write(uploaded_file.read())
    
    st.video(tfile.name)
    
    st.markdown("### 🎯 CUSTOM WATERMARK AREA SELECTION")
    st.write("Sliders se box ko watermark ke upar fit karein:")
    
    # Precision Controls
    col1, col2 = st.columns(2)
    with col1:
        x_pos = st.slider("Horizontal Position (X)", 0, 100, 80)
        y_pos = st.slider("Vertical Position (Y)", 0, 100, 90)
    with col2:
        box_width = st.slider("Box Width", 10, 50, 20)
        box_height = st.slider("Box Height", 5, 30, 10)

    if st.button("🚀 EXECUTE AI PRECISION REMOVAL"):
        cap = cv2.VideoCapture(tfile.name)
        fps = cap.get(cv2.CAP_PROP_FPS)
        w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        
        # Convert percentages to actual pixels
        px = int((x_pos / 100) * w)
        py = int((y_pos / 100) * h)
        pw = int((box_width / 100) * w)
        ph = int((box_height / 100) * h)
        
        out_path = "precision_cleaned.mp4"
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        out = cv2.VideoWriter(out_path, fourcc, fps, (w, h))
        
        bar = st.progress(0)
        total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        
        f_count = 0
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret: break
            
            # 🧠 AI Masking at Custom Location
            mask = np.zeros(frame.shape[:2], dtype=np.uint8)
            # Create the selection box
            cv2.rectangle(mask, (px - pw//2, py - ph//2), (px + pw//2, py + ph//2), 255, -1)
            
            # VEMAKE Style Inpainting
            result = cv2.inpaint(frame, mask, 7, cv2.INPAINT_TELEA)
            
            out.write(result)
            f_count += 1
            if f_count % 15 == 0: bar.progress(f_count / total_frames)
            
        cap.release()
        out.release()
        
        st.success("✅ TARGET NEUTRALIZED! Watermark Erased.")
        st.video(out_path)
        with open(out_path, "rb") as f:
            st.download_button("📥 DOWNLOAD CLEAN VIDEO", f, file_name="Mayo_Precision_Clean.mp4")

# WhatsApp Channel Link
st.markdown('<center><a href="https://whatsapp.com/channel/0029VbBzlMlIt5rzSeMBE922" style="background:#25D366; color:white; padding:15px; border-radius:50px; text-decoration:none; font-weight:bold;">🟢 JOIN MY WHATSAPP CHANNEL</a></center>', unsafe_allow_html=True)

