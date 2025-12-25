import streamlit as st

# Page Setup & Matrix Effect
st.set_page_config(page_title="AWAIS MAYO HACKER - AI HUB", layout="wide")

st.markdown("""
    <style>
    /* Full Screen Matrix Rain */
    .stApp {
        background: black url('https://media.giphy.com/media/o0vwzuFwCGAFO/giphy.gif');
        background-size: cover;
        background-attachment: fixed;
    }

    /* Floating Branding */
    .hacker-brand {
        position: fixed; top: 10px; right: 10px;
        color: #00FF41; font-family: 'Courier New', monospace;
        font-weight: bold; text-shadow: 0 0 15px #00FF41;
        z-index: 9999; background: rgba(0,20,0,0.8);
        padding: 10px; border: 1px solid #00FF41;
    }

    /* Professional Buttons */
    .main-btn {
        display: block; width: 100%; padding: 20px;
        margin: 10px 0; text-align: center;
        background: rgba(0, 50, 0, 0.9);
        color: #00FF41 !important;
        border: 2px solid #00FF41;
        border-radius: 10px;
        font-size: 20px; font-weight: bold;
        text-decoration: none;
        transition: 0.3s;
    }
    .main-btn:hover { background: #00FF41; color: black !important; box-shadow: 0 0 30px #00FF41; }

    .wa-btn {
        display: block; width: 100%; padding: 15px;
        background-color: #25D366; color: white !important;
        text-align: center; border-radius: 50px;
        font-weight: bold; text-decoration: none;
        margin-top: 30px; box-shadow: 0 0 20px #25D366;
    }
    h1, h3 { color: #00FF41 !important; text-shadow: 0 0 10px #00FF41; text-align: center; }
    </style>
    
    <div class="hacker-brand">AWAIS MAYO HACKER<br>+923295533214</div>
    """, unsafe_allow_html=True)

st.title("🛡️ AWAIS MAYO - AI WATERMARK REMOVER HUB 🛡️")
st.write("### [ SYSTEM STATUS: ALL AI TOOLS CONNECTED ]")

col1, col2 = st.columns(2)

with col1:
    st.markdown("### 🤖 AUTO AI REMOVERS")
    st.write("In buttons par click karein aur apni video upload karke 100% watermark remove karein:")
    
    # AI Website URLs Integration
    st.markdown("""
        <a href="https://www.hitpaw.com/online-video-watermark-remover.html" target="_blank" class="main-btn">
            🚀 HITPAW AI REMOVER (Best)
        </a>
        <a href="https://online-video-cutter.com/remove-logo" target="_blank" class="main-btn">
            🎯 123APPS LOGO REMOVER
        </a>
        <a href="https://www.media.io/video-watermark-remover.html" target="_blank" class="main-btn">
            ⚡ MEDIA.IO AI TOOL
        </a>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("### 📢 OWNER CHANNEL")
    st.write("Latest hacking tools aur updates ke liye niche click karein:")
    
    st.markdown("""
        <a href="https://whatsapp.com/channel/0029VbBzlMlIt5rzSeMBE922" target="_blank" class="wa-btn">
            🟢 JOIN OFFICIAL WHATSAPP CHANNEL
        </a>
    """, unsafe_allow_html=True)
    
    st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNHJueW9ueXp0bm9ueXp0bm9ueXp0bm9ueXp0bm9ueXp0JmVwPXYxX2ludGVybmFsX2dpZl9ieV9pZCZjdD1n/o0vwzuFwCGAFO/giphy.gif")

st.markdown("---")
st.markdown("<p style='text-align:center;'>BYPASSING SECURITY PROTOCOLS... LOADED BY 923295533214</p>", unsafe_allow_html=True)
