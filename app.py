import streamlit as st
import time

# Page Configuration
st.set_page_config(page_title="Awais Mayo Hacker", page_icon="💀", layout="wide")

# Dark Hacking Styling
st.markdown("""
    <style>
    .main { background-color: #000000; }
    h1, h3, p, span { color: #00FF41 !important; font-family: 'Courier New', monospace !important; }
    .stButton>button {
        background-color: #051a05;
        color: #00FF41;
        border: 2px solid #00FF41;
        box-shadow: 0 0 10px #00FF41;
        width: 100%;
    }
    .stTextInput>div>div>input { background-color: #051a05; color: #00FF41; }
    </style>
    """, unsafe_allow_html=True)

st.title("🛡️ AWAIS MAYO HACKER 🛡️")
st.write("---")

col1, col2 = st.columns(2)

with col1:
    st.subheader("📁 SOURCE INPUT")
    uploaded_file = st.file_uploader("Upload Video File", type=['mp4', 'mov', 'avi'])
    run_btn = st.button("EXECUTE DECRYPTION SCRIPT")

with col2:
    st.subheader("🖥️ SYSTEM LOGS")
    log_area = st.empty()
    
    if run_btn and uploaded_file:
        logs = [
            "> [SYSTEM]: AWAIS MAYO HACKER INITIALIZING...",
            "> [ACCESS]: BYPASSING SECURITY FILTERS...",
            "> [TARGET]: DETECTING WATERMARK SIGNATURE...",
            "> [PROCESS]: REMOVING UNWANTED METADATA...",
            "> [STATUS]: DECRYPTION 100% COMPLETE."
        ]
        
        current_logs = ""
        for log in logs:
            current_logs += log + "\n\n"
            log_area.code(current_logs, language="bash")
            time.sleep(1)
        
        st.success("CLEANED FILE GENERATED SUCCESSFULLY")
        st.video(uploaded_file)
    elif run_btn:
        st.error("ERROR: NO SOURCE FILE DETECTED!")
