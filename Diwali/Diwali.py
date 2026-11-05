import streamlit as st
import time
import os
import base64

st.set_page_config(page_title="Happy Diwali Wishes", page_icon="🪔", layout="centered")

st.markdown("""
    <style>
    .stApp {
        background-color: #0b0f19;
        color: #ffffff;
    }
    .diwali-card {
        background: linear-gradient(135deg, #1e1e2f 0%, #3a0ca3 100%);
        padding: 35px;
        border-radius: 20px;
        border: 2px solid #FFD700;
        box-shadow: 0px 0px 25px rgba(255, 215, 0, 0.5);
        text-align: center;
        margin-top: 20px;
    }
    .diwali-card h1 {
        color: #FFD700;
        font-size: 2.2rem;
        margin-bottom: 15px;
    }
    .diwali-card p {
        font-size: 1.2rem;
        color: #f1f1f1;
        line-height: 1.6;
    }
    .signature {
        margin-top: 30px;
        font-weight: bold;
        color: #00ffcc;
        font-size: 1.2rem;
        letter-spacing: 1px;
    }
    .circle-video-container {
        display: flex;
        justify-content: center;
        align-items: center;
        gap: 25px;
        flex-wrap: wrap;
        margin-top: 20px;
        margin-bottom: 20px;
    }
    .circle-video {
        width: 300px;
        height: 300px;
        border-radius: 50%;
        object-fit: cover;
        border: 4px solid #FFD700;
        box-shadow: 0px 0px 25px rgba(255, 215, 0, 0.7);
    }
    </style>
""", unsafe_allow_html=True)

if 'step' not in st.session_state:
    st.session_state.step = 'loading'

if 'unmuted' not in st.session_state:
    st.session_state.unmuted = False

# Step 1: Super Fast Loading Screen
if st.session_state.step == 'loading':
    st.markdown("<h2 style='text-align: center; color: #FFD700;'>🪔 Initializing Diwali Celebration... 🪔</h2>",
                unsafe_allow_html=True)

    progress_bar = st.progress(0)
    status_text = st.empty()

    for percent in range(100):
        time.sleep(0.001)  # Bahut fast loading taaki delay na ho
        progress_bar.progress(percent + 1)
        status_text.markdown(
            f"<p style='text-align: center; color: #00ffcc;'>Loading festive modules... {percent + 1}%</p>",
            unsafe_allow_html=True)

    time.sleep(0.1)
    st.session_state.step = 'video'
    st.rerun()

# Step 2: Three Circular Videos Screen (Instant Play)
elif st.session_state.step == 'video':
    st.markdown("<h2 style='text-align: center; color: #FFD700;'>✨ Special Diwali Celebration ✨</h2>",
                unsafe_allow_html=True)


    def get_base64_video(file_path):
        if os.path.exists(file_path):
            with open(file_path, "rb") as f:
                data = f.read()
            encoded = base64.b64encode(data).decode()
            return f"data:video/mp4;base64,{encoded}"
        return ""


    v0 = get_base64_video("Video.mp4")
    v1 = get_base64_video("Video1.mp4")
    v2 = get_base64_video("Video2.mp4")

    muted_attr = "" if st.session_state.unmuted else "muted"

    st.markdown(f"""
        <div class="circle-video-container">
            <div>
                <video class="circle-video" autoplay {muted_attr} loop playsinline>
                    <source src="{v0}" type="video/mp4">
                </video>
            </div>
            <div>
                <video class="circle-video" autoplay muted loop playsinline>
                    <source src="{v1}" type="video/mp4">
                </video>
            </div>
            <div>
                <video class="circle-video" autoplay muted loop playsinline>
                    <source src="{v2}" type="video/mp4">
                </video>
            </div>
        </div>
    """, unsafe_allow_html=True)

    st.write("")
    c1, c2, c3 = st.columns([1, 2, 1])
    with c2:
        if not st.session_state.unmuted:
            if st.button("🔊 Unmute Video.mp4 Sound", use_container_width=True):
                st.session_state.unmuted = True
                st.rerun()

        if st.button("🎁 Click for Best Wishes", use_container_width=True):
            st.session_state.step = 'message'
            st.rerun()

# Step 3: Sweet Diwali Wishes Screen
elif st.session_state.step == 'message':
    st.markdown("""
        <div class='diwali-card'>
            <h1>🪔 Happy Diwali! 🪔</h1>
            <p>May the divine festival of lights illuminate your life with boundless joy, good health, peace, and endless success. Wishing you and your loved ones a wonderful celebration filled with light and laughter!</p>
        </div>
    """, unsafe_allow_html=True)

    st.write("")
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("✨ Continue...", use_container_width=True):
            st.session_state.step = 'final'
            st.rerun()

# Step 4: Once Again Happy Diwali & Signature Screen with Handshake
elif st.session_state.step == 'final':
    st.markdown("""
        <div class='diwali-card'>
            <h1>🪔 Once Again, Happy Diwali! 🤝</h1>
            <p>Wishing you continuous growth, prosperity, and great success ahead. Let's celebrate this festival with joy, warmth, and togetherness!</p>
            <div class='signature'>
                Best Regards,<br>
                <span>Bikash Kumar Kushwaha</span>
            </div>
        </div>
    """, unsafe_allow_html=True)

    st.write("")
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("🔄 Play Again", use_container_width=True):
            st.session_state.step = 'loading'
            st.session_state.unmuted = False
            st.rerun()
