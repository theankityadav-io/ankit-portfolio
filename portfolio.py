import streamlit as st

# 1. Page Config
st.set_page_config(page_title="Ankit Yadav | Portfolio", page_icon="🪄", layout="wide")

# 2. FontAwesome & Animation Library
st.markdown("""
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/animate.css/4.1.1/animate.min.css">
""", unsafe_allow_html=True)

# 3. Theme Logic
if 'theme' not in st.session_state: st.session_state.theme = 'light'
def toggle_theme(): st.session_state.theme = 'dark' if st.session_state.theme == 'light' else 'light'

t = st.session_state.theme
bg, card_bg, txt, sub_txt, border = ("#0B0E11", "#15191C", "#FFFFFF", "#A1A1A6", "#2D3135") if t == 'dark' else ("#F0F2F5", "#FFFFFF", "#1A1D23", "#6C757D", "#E9ECEF")

# 4. Professional CSS with Animation Keyframes
st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;600;800&display=swap');
    html, body, [class*="st-"] {{ font-family: 'Plus Jakarta Sans', sans-serif; background-color: {bg}; color: {txt}; scroll-behavior: smooth; }}
    
    @keyframes fadeInUp {{
        from {{ opacity: 0; transform: translateY(30px); }}
        to {{ opacity: 1; transform: translateY(0); }}
    }}

    /* Hire Me Pulsing Animation */
    @keyframes hirePulse {{
        0% {{ transform: scale(1); box-shadow: 0 0 0 0 rgba(255, 75, 75, 0.4); }}
        70% {{ transform: scale(1.05); box-shadow: 0 0 0 15px rgba(255, 75, 75, 0); }}
        100% {{ transform: scale(1); box-shadow: 0 0 0 0 rgba(255, 75, 75, 0); }}
    }}

    .shiny-name {{
        background: linear-gradient(to right, #FF4B4B, #4FACFE, #00F2FE, #FF4B4B);
        background-size: 200% auto; -webkit-background-clip: text; -webkit-text-fill-color: transparent;
        animation: shine 3s linear infinite; font-weight: 800; font-size: 3.5em; margin: 0;
    }}
    @keyframes shine {{ to {{ background-position: 200% center; }} }}

    .bento-card {{
        background: {card_bg}; border: 1px solid {border}; border-radius: 32px; padding: 30px;
        transition: all 0.5s cubic-bezier(0.175, 0.885, 0.32, 1.275); margin-bottom: 20px;
        animation: fadeInUp 0.8s ease-out forwards;
    }}
    .bento-card:hover {{ transform: translateY(-10px); box-shadow: 0 20px 40px rgba(0,0,0,0.15); border-color: #FF4B4B; }}

    .grid-container {{ display: grid; grid-template-columns: 1fr 1fr; gap: 15px; margin-top: 15px; }}
    
    .item-card {{ 
        background: {bg}; padding: 20px; border-radius: 22px; border: 1px solid {border};
        transition: 0.4s ease;
    }}
    .item-card:hover {{ 
        background: {card_bg}; transform: scale(1.05); border-color: #4FACFE; 
        box-shadow: 0 10px 25px rgba(0,0,0,0.1);
    }}

    .edu-card {{
        background: #1A1D23 !important; color: #FFFFFF !important;
        border-radius: 32px; padding: 30px; border: none !important;
    }}
    .edu-card * {{ background: transparent !important; color: white !important; }}

    /* Modern Hire Me Button */
    .hire-btn-animated {{
        background: linear-gradient(135deg, #FF4B4B 0%, #FF6B6B 100%);
        color: white !important; padding: 20px; border-radius: 24px;
        text-align: center; display: block; font-weight: 800; font-size: 1.1em;
        text-decoration: none !important; margin-top: 25px;
        animation: hirePulse 2s infinite;
        transition: 0.3s;
    }}
    .hire-btn-animated:hover {{ transform: scale(1.08); filter: brightness(1.1); }}

    .ios-icon {{
        width: 55px; height: 55px; background: {bg}; border: 1px solid {border};
        border-radius: 16px; display: flex; align-items: center; justify-content: center;
        transition: 0.3s; color: {txt} !important;
    }}
    .ios-icon:hover {{ background: #FF4B4B; color: white !important; transform: rotate(8deg) scale(1.1); }}

    .tag {{ background: {bg}; padding: 6px 14px; border-radius: 12px; font-size: 0.85em; font-weight: 700; border: 1px solid {border}; display: inline-block; margin: 4px; transition: 0.3s; }}
    .tag:hover {{ background: #FF4B4B; color: white; border-color: #FF4B4B; }}

    header, footer {{ visibility: hidden; }}
    </style>
    """, unsafe_allow_html=True)

# --- Theme Toggle ---
c1, c2 = st.columns([0.9, 0.1])
with c2: 
    if st.button("🌓"): toggle_theme(); st.rerun()

# --- Main Layout ---
col_left, col_right = st.columns([1.8, 1.2], gap="large")

with col_left:
    # 1. PROFILE CARD
    st.markdown(f"""
        <div class="bento-card">
            <p class="shiny-name">Ankit Yadav</p>
            <p style="color: {sub_txt}; font-size: 1.2em; font-weight: 600;">BCA Student @ Galgotias | AI/ML | Professional Dev & Editor</p>
            <div style="display: flex; gap: 15px; margin-top: 20px;">
                <a href="https://www.linkedin.com/in/ankit-yadav-9655aa3a6" class="ios-icon"><i class="fa-brands fa-linkedin-in"></i></a>
                <a href="https://www.instagram.com/aany1code" class="ios-icon"><i class="fa-brands fa-instagram"></i></a>
                <a href="https://github.com/theankityadav-io" class="ios-icon"><i class="fa-brands fa-github"></i></a>
                <a href="mailto:Akyadav1404@gmail.com" class="ios-icon"><i class="fa-regular fa-envelope"></i></a>
            </div>
        </div>
    """, unsafe_allow_html=True)

    # 2. EXPERTISE & SERVICES
    st.markdown(f"""
        <div class="bento-card">
            <h2 style="font-weight: 800; margin-bottom: 5px;">⚡ Expertise & Services</h2>
            <div class="grid-container">
                <div class="item-card">
                    <i class="fa-solid fa-cart-shopping" style="color:#FF4B4B; margin-bottom:10px;"></i>
                    <h4 style="margin:0;">E-commerce Dev</h4>
                    <p style="font-size: 0.75em; color: {sub_txt}; margin-top:5px;">Full-stack store solutions.</p>
                </div>
                <div class="item-card">
                    <i class="fa-solid fa-clapperboard" style="color:#4FACFE; margin-bottom:10px;"></i>
                    <h4 style="margin:0;">Cinematic Editing</h4>
                    <p style="font-size: 0.75em; color: {sub_txt}; margin-top:5px;">Visual storytelling with DaVinci.</p>
                </div>
                <div class="item-card">
                    <i class="fa-solid fa-robot" style="color:#00F2FE; margin-bottom:10px;"></i>
                    <h4 style="margin:0;">Python Automation</h4>
                    <p style="font-size: 0.75em; color: {sub_txt}; margin-top:5px;">Custom AI & Task automation.</p>
                </div>
                <div class="item-card">
                    <i class="fa-solid fa-code" style="color:#FF8E8E; margin-bottom:10px;"></i>
                    <h4 style="margin:0;">Full-Stack Web</h4>
                    <p style="font-size: 0.75em; color: {sub_txt}; margin-top:5px;">Modern responsive applications.</p>
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)

    # 3. ACTIVE PROJECTS
    st.markdown(f"""
        <div class="bento-card">
            <h2 style="font-weight: 800; margin-bottom: 5px;">🚀 Active Projects</h2>
            <div class="grid-container">
                <div class="item-card">
                    <h4 style="margin:0;">🔐 VaultPro</h4>
                    <p style="font-size: 0.75em; color: {sub_txt}; margin-top:5px;">Secure password management.</p>
                    <a href="https://vault-pro.streamlit.app/" style="color:#FF4B4B; font-weight:700; font-size:0.8em; text-decoration:none;">View Live ↗</a>
                </div>
                <div class="item-card">
                    <h4 style="margin:0;">📥 Media DL AI</h4>
                    <p style="font-size: 0.75em; color: {sub_txt}; margin-top:5px;">Automated HQ extraction.</p>
                    <a href="https://yt-downloader-ai.streamlit.app" style="color:#FF4B4B; font-weight:700; font-size:0.8em; text-decoration:none;">View Live ↗</a>
                </div>
                <div class="item-card">
                    <h4 style="margin:0;">🎮 Python Games</h4>
                    <p style="font-size: 0.75em; color: {sub_txt}; margin-top:5px;">Logic-driven game mechanics.</p>
                </div>
                <div class="item-card">
                    <h4 style="margin:0;">💻 Logic Vault</h4>
                    <p style="font-size: 0.75em; color: {sub_txt}; margin-top:5px;">C & Python logic collection.</p>
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)

with col_right:
    # 4. ACADEMIC JOURNEY
    st.markdown(f"""
        <div class="edu-card">
            <i class="fa-solid fa-graduation-cap" style="font-size: 2.2em; color: #FF4B4B !important;"></i>
            <h3 style="font-weight: 800; margin-top: 15px;">Academic Journey</h3>
            <div style="margin-top: 25px; border-left: 2px solid #FF4B4B; padding-left: 15px; margin-bottom: 25px;">
                <p style="font-weight: 800; font-size: 1.1em; color: #FF4B4B !important;">BCA (AI & ML)</p>
                <p style="font-size: 0.8em; opacity: 0.8;">Galgotias University | 2025 - Present</p>
            </div>
            <div style="border-left: 2px solid #555; padding-left: 15px;">
                <p style="font-weight: 700; font-size: 1em;">10th & 12th Passout</p>
                <p style="font-size: 0.8em; opacity: 0.7;">Govt. School, Delhi</p>
            </div>
        </div>
    """, unsafe_allow_html=True)

    # 5. SKILLS
    st.markdown(f"""
        <div class="bento-card">
            <h3 style="font-weight: 800; margin-bottom: 20px;">🛠️ Tech Stack</h3>
            <div style="display: flex; flex-wrap: wrap; gap: 8px;">
                <span class="tag">Python</span><span class="tag">DaVinci Resolve</span>
                <span class="tag">C Language</span><span class="tag">Streamlit</span>
                <span class="tag">Pandas</span><span class="tag">SQL</span>
            </div>
            <a href="https://wa.link/0jksj5" class="hire-btn-animated">Hire Me</a>
        </div>
    """, unsafe_allow_html=True)