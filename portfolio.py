import mimetypes
from pathlib import Path

import streamlit as st

st.set_page_config(page_title="Ankit Yadav | Portfolio", page_icon="🪄", layout="wide")

# 2. Navigation State & Query Params
if st.query_params.get("view") == "cinematic":
    st.session_state.page = 'cinematic_editing'
elif 'page' not in st.session_state: 
    st.session_state.page = 'home'

def go_home():
    st.query_params.clear()
    st.session_state.page = 'home'

def go_cinematic():
    st.query_params["view"] = "cinematic"
    st.session_state.page = 'cinematic_editing'

# 3. Load every supported video from the local videos folder.
VIDEO_DIR = Path(__file__).parent / "videos"
VIDEO_EXTENSIONS = {".mp4", ".m4v", ".mov", ".webm"}
VIDEO_EDITING_PROJECTS = [
    {
        "id": video_path.stem,
        "title": video_path.stem.replace("_", " ").replace("-", " ").title(),
        "description": "",
        "video_path": video_path,
        "video_format": mimetypes.guess_type(video_path.name)[0] or "video/mp4",
    }
    for video_path in sorted(VIDEO_DIR.glob("*"))
    if video_path.is_file() and video_path.suffix.lower() in VIDEO_EXTENSIONS
]


@st.cache_data(show_spinner=False)
def load_video(video_path: str) -> bytes:
    return Path(video_path).read_bytes()

# 4. FontAwesome & Animation Library
st.markdown("""
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/animate.css/4.1.1/animate.min.css">
""", unsafe_allow_html=True)

# 5. Theme Logic
if 'theme' not in st.session_state: st.session_state.theme = 'light'
def toggle_theme(): st.session_state.theme = 'dark' if st.session_state.theme == 'light' else 'light'

t = st.session_state.theme
bg, card_bg, txt, sub_txt, border = ("#0B0E11", "#15191C", "#FFFFFF", "#A1A1A6", "#2D3135") if t == 'dark' else ("#F0F2F5", "#FFFFFF", "#1A1D23", "#6C757D", "#E9ECEF")

# 6. CSS Styling
st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;600;800&family=Space+Grotesk:wght@500;600;700&display=swap');
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
        background: {card_bg}; border: 1px solid {border}; border-radius: 20px; padding: 30px;
        transition: all 0.5s cubic-bezier(0.175, 0.885, 0.32, 1.275); margin-bottom: 20px;
        animation: fadeInUp 0.8s ease-out forwards;
    }}
    .bento-card:hover {{ transform: translateY(-8px); box-shadow: 0 20px 40px rgba(0,0,0,0.15); border-color: #FF4B4B; }}

    .grid-container {{ display: grid; grid-template-columns: 1fr 1fr; gap: 15px; margin-top: 15px; }}
    
    .item-card {{ 
        background: {bg}; padding: 20px; border-radius: 14px; border: 1px solid {border};
        transition: 0.4s ease; height: 100%; box-sizing: border-box;
    }}
    .item-card:hover {{ 
        background: {card_bg}; transform: scale(1.04); border-color: #4FACFE; 
        box-shadow: 0 10px 25px rgba(0,0,0,0.1);
    }}

    .item-card-link {{
        text-decoration: none !important;
        color: inherit !important;
        display: block !important;
        cursor: pointer !important;
    }}

    .cinematic-link .item-card {{
        border-color: rgba(79, 172, 254, 0.65);
        animation: cinematicGlow 2.4s ease-in-out infinite alternate;
    }}
    @keyframes cinematicGlow {{
        from {{ box-shadow: 0 0 8px rgba(79, 172, 254, 0.2); }}
        to {{ box-shadow: 0 0 22px rgba(79, 172, 254, 0.55); }}
    }}

    /* Remove link logo/icon on hover globally */
    a.anchor-link, [data-testid="stHeaderActionElements"],
    h1 a, h2 a, h3 a, h4 a, h5 a, h6 a,
    .css-1544g2n, [data-testid="stMarkdownContainer"] a.anchor-link {{
        display: none !important;
        visibility: hidden !important;
        opacity: 0 !important;
    }}

    /* Video Card */
    .god-video-card {{
        background: {card_bg}; border: 1px solid {border}; border-radius: 16px; padding: 20px;
        margin-bottom: 15px; transition: all 0.4s ease;
    }}
    .god-video-card:hover {{
        border-color: #FF4B4B; box-shadow: 0 12px 30px rgba(255, 75, 75, 0.15);
    }}

    .client-work-header {{
        position: relative; margin: 14px 0 30px; padding-bottom: 16px;
        border-bottom: 1px solid {border};
    }}
    .client-work-header::after {{
        content: ""; position: absolute; bottom: -1px; left: 0;
        width: 68px; height: 3px; border-radius: 2px; background: #FF4B4B;
    }}
    .client-work-eyebrow {{
        margin: 0 0 7px !important; color: #FF4B4B !important;
        font-size: 0.72rem; font-weight: 800; line-height: 1.2;
    }}
    h2.client-work-heading {{
        display: block !important; width: 100%; margin: 0 !important; padding: 0 !important;
        border: 0 !important; color: {txt} !important;
        font-family: 'Space Grotesk', sans-serif !important; font-size: 2.75rem !important;
        font-weight: 700 !important; line-height: 1.08 !important; letter-spacing: 0 !important;
    }}
    .client-work-heading .heading-accent {{ color: #FF4B4B !important; }}
    .selected-work-heading {{
        margin: 28px 0 16px; padding-bottom: 10px; border-bottom: 1px solid {border};
        color: {txt}; font-family: 'Space Grotesk', sans-serif !important;
        font-size: 1.8rem; font-weight: 700;
    }}
    .view-more-link {{
        display: flex; align-items: center; justify-content: center; min-height: 44px;
        padding: 10px 16px; border: 1px solid {border}; border-radius: 12px;
        background: {card_bg}; color: {txt} !important; font-weight: 700;
        text-decoration: none !important; transition: 0.2s ease;
    }}
    .view-more-link:hover {{
        background: #FF4B4B; border-color: #FF4B4B; color: #FFFFFF !important;
    }}
    @media (max-width: 900px) {{
        .bento-card, .edu-card {{ padding: 22px; }}
        .grid-container {{ grid-template-columns: minmax(0, 1fr); gap: 12px; }}
    }}
    @media (max-width: 640px) {{
        h2.client-work-heading {{ font-size: 2rem !important; }}
        .shiny-name {{ font-size: 2.4rem !important; }}
        .bento-card, .edu-card {{ padding: 18px; border-radius: 16px; }}
        .item-card {{ padding: 16px; }}
        .selected-work-heading {{ font-size: 1.5rem; }}
        .item-card:hover {{ transform: none; }}
    }}

    video[data-testid="stVideo"] {{
        display: block; width: 100% !important; height: auto !important;
        object-fit: contain; background: #080A0C;
        border: 1px solid {border}; border-radius: 18px;
        box-shadow: 0 14px 32px rgba(0, 0, 0, 0.32), 0 0 0 1px rgba(79, 172, 254, 0.18);
    }}

    .tool-tag {{
        background: {bg}; color: {txt}; padding: 4px 10px; border-radius: 10px;
        font-size: 0.75em; font-weight: 700; border: 1px solid {border}; display: inline-block; margin: 3px;
    }}

    .edu-card {{
        background: #1A1D23 !important; color: #FFFFFF !important;
        border-radius: 20px; padding: 30px; border: none !important;
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


# ========================================================
# PAGE 1: HOME PORTFOLIO VIEW
# ========================================================
if st.session_state.page == 'home':

    # --- Theme Toggle ---
    c1, c2 = st.columns([0.9, 0.1])
    with c2: 
        if st.button("🌓", key="theme_toggle_home"): toggle_theme(); st.rerun()

    # --- Main Layout ---
    col_left, col_right = st.columns([1.8, 1.2], gap="large")

    with col_left:
        # 1. PROFILE CARD
        st.markdown(f"""
            <div class="bento-card">
                <p class="shiny-name">Ankit Yadav</p>
                <p style="color: {sub_txt}; font-size: 1.2em; font-weight: 600;">BCA Student @ Galgotias | AI/ML | Professional Dev & Editor</p>
                <div style="display: flex; flex-wrap: wrap; gap: 15px; margin-top: 20px;">
                    <a href="https://www.linkedin.com/in/ankit-yadav-9655aa3a6" class="ios-icon"><i class="fa-brands fa-linkedin-in"></i></a>
                    <a href="https://www.instagram.com/aany1code" class="ios-icon"><i class="fa-brands fa-instagram"></i></a>
                    <a href="https://github.com/theankityadav-io" class="ios-icon"><i class="fa-brands fa-github"></i></a>
                    <a href="https://discord.com/users/1233492840613543960" class="ios-icon" target="_blank" rel="noopener noreferrer" aria-label="Discord" title="Discord"><i class="fa-brands fa-discord"></i></a>
                    <a href="mailto:Akyadav1404@gmail.com" class="ios-icon"><i class="fa-regular fa-envelope"></i></a>
                </div>
            </div>
        """, unsafe_allow_html=True)

        if VIDEO_EDITING_PROJECTS:
            st.markdown("<h3 class='selected-work-heading'>Featured edits</h3>", unsafe_allow_html=True)
            featured_projects = VIDEO_EDITING_PROJECTS[:2]
            featured_columns = st.columns(len(featured_projects), gap="medium")
            for project, featured_column in zip(featured_projects, featured_columns):
                with featured_column:
                    st.video(
                        load_video(str(project["video_path"])),
                        format=project["video_format"],
                        muted=True,
                        width="stretch",
                    )
            view_more_columns = st.columns([1, 1, 1])
            with view_more_columns[1]:
                st.markdown(
                    '<a class="view-more-link" href="?view=cinematic" target="_self">View more edits &rarr;</a>',
                    unsafe_allow_html=True,
                )

        # 2. CLIENT WORK & SERVICES
        st.markdown(f"""
            <div class="bento-card">
                <h2 style="font-weight: 800; margin-bottom: 5px;">⚡ Client work and services</h2>
                <div class="grid-container">
                    <div class="item-card">
                        <i class="fa-solid fa-cart-shopping" style="color:#FF4B4B; margin-bottom:10px;"></i>
                        <h4 style="margin:0;">E-commerce Dev</h4>
                        <p style="font-size: 0.9em; color: {sub_txt}; margin-top:5px;">Full-stack store solutions.</p>
                    </div>
                    <a href="?view=cinematic" target="_self" class="item-card-link cinematic-link">
                        <div class="item-card">
                            <i class="fa-solid fa-clapperboard" style="color:#4FACFE; margin-bottom:10px;"></i>
                            <h4 style="margin:0;">Editing work</h4>
                            <p style="font-size: 0.9em; color: {sub_txt}; margin-top:5px;">Visual storytelling with DaVinci.</p>
                        </div>
                    </a>
                    <div class="item-card">
                        <i class="fa-solid fa-robot" style="color:#00F2FE; margin-bottom:10px;"></i>
                        <h4 style="margin:0;">Python Automation</h4>
                        <p style="font-size: 0.9em; color: {sub_txt}; margin-top:5px;">Custom AI & Task automation.</p>
                    </div>
                    <div class="item-card">
                        <i class="fa-solid fa-code" style="color:#FF8E8E; margin-bottom:10px;"></i>
                        <h4 style="margin:0;">Full-Stack Web</h4>
                        <p style="font-size: 0.9em; color: {sub_txt}; margin-top:5px;">Modern responsive applications.</p>
                    </div>
                </div>
            </div>
        """, unsafe_allow_html=True)

        # 3. ACTIVE PROJECTS
        st.markdown(f"""
            <div class="bento-card" style="margin-top: 20px;">
                <h2 style="font-weight: 800; margin-bottom: 5px;">🚀 Active Projects</h2>
                <div class="grid-container">
                    <div class="item-card">
                        <h4 style="margin:0;">🔐 VaultPro</h4>
                        <p style="font-size: 0.9em; color: {sub_txt}; margin-top:5px;">Secure password management.</p>
                        <a href="https://vault-pro.streamlit.app/" style="color:#FF4B4B; font-weight:700; font-size:0.8em; text-decoration:none;">View Live ↗</a>
                    </div>
                    <div class="item-card">
                        <h4 style="margin:0;">📥 Media DL AI</h4>
                        <p style="font-size: 0.9em; color: {sub_txt}; margin-top:5px;">Automated HQ extraction.</p>
                        <a href="https://yt-downloader-ai.streamlit.app" style="color:#FF4B4B; font-weight:700; font-size:0.8em; text-decoration:none;">View Live ↗</a>
                    </div>
                    <div class="item-card">
                        <h4 style="margin:0;">🎮 Python Games</h4>
                        <p style="font-size: 0.9em; color: {sub_txt}; margin-top:5px;">Logic-driven game mechanics.</p>
                    </div>
                    <div class="item-card">
                        <h4 style="margin:0;">💻 Logic Vault</h4>
                        <p style="font-size: 0.9em; color: {sub_txt}; margin-top:5px;">C & Python logic collection.</p>
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


# ========================================================
# PAGE 2: CLEAN VIDEO SHOWCASE (ONLY VIDEOS & BACK BUTTON)
# ========================================================
elif st.session_state.page == 'cinematic_editing':

    # Top Bar: Back to Main Page Button & Theme Toggle
    nav_c1, nav_c2 = st.columns([0.85, 0.15])
    with nav_c1:
        if st.button("← Back to Main Page", key="back_to_home"):
            go_home()
            st.rerun()
    with nav_c2:
        if st.button("🌓", key="theme_toggle_video"):
            toggle_theme()
            st.rerun()

    st.markdown("""
        <div class="client-work-header">
            <p class="client-work-eyebrow">VIDEO PORTFOLIO</p>
            <h2 class="client-work-heading"><span class="heading-accent">Client</span> Work</h2>
        </div>
    """, unsafe_allow_html=True)

    # Render Videos Grid (2 Columns)
    for i in range(0, len(VIDEO_EDITING_PROJECTS), 2):
        v_col1, v_col2 = st.columns(2, gap="large")
        cols = [v_col1, v_col2]

        for idx, col in enumerate(cols):
            p_index = i + idx
            if p_index < len(VIDEO_EDITING_PROJECTS):
                proj = VIDEO_EDITING_PROJECTS[p_index]
                with col:
                    st.video(
                        load_video(str(proj["video_path"])),
                        format=proj["video_format"],
                        autoplay=True,
                        muted=True,
                    )