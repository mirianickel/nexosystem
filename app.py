"""
EcoNexo's System — v2.0
Full-featured productivity platform with AI, SQL persistence,
bilingual support, accessibility, dark mode, and innovative design.
"""

import streamlit as st
import random
import sys
import os

sys.path.insert(0, os.path.dirname(__file__))

try:
    import database as db
    from i18n import t, QUESTIONS, TASKS, PROFILE_INFO
    DB_AVAILABLE = True
except Exception:
    DB_AVAILABLE = False

# ─────────────────────────────────────────────
# PAGE CONFIG
# ─────────────────────────────────────────────
st.set_page_config(
    page_title="EcoNexo's System",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ─────────────────────────────────────────────
# SESSION STATE DEFAULTS
# ─────────────────────────────────────────────
DEFAULTS = {
    "logged_in": False,
    "user_id": None,
    "user_name": "",
    "user_email": "",
    "lang": "pt",
    "theme": "light",
    "font_size": "md",
    "page": "landing",          # landing | features | login | about | lgpd | contact | app
    "step": "questionnaire",    # questionnaire | tasks | iap | profile | chat | user_page | settings
    "q_index": 0,
    "answers": {},
    "tasks_completed": 0,
    "completed_tasks": set(),
    "selected_task": None,
    "iap_score": None,
    "profile": None,
    "messages": [],
    "show_floating_menu": False,
    "float_menu_open": False,
}
for k, v in DEFAULTS.items():
    if k not in st.session_state:
        st.session_state[k] = v

L = st.session_state.lang

# ─────────────────────────────────────────────
# FONT SIZES
# ─────────────────────────────────────────────
FONT_SIZES = {"sm": "13px", "md": "16px", "lg": "20px"}
BASE_FONT = FONT_SIZES.get(st.session_state.font_size, "16px")

# ─────────────────────────────────────────────
# THEME
# ─────────────────────────────────────────────
IS_DARK = st.session_state.theme == "dark"

if IS_DARK:
    BG       = "#0f1117"
    SURFACE  = "#1a1d27"
    SURFACE2 = "#242838"
    TEXT     = "#e8ecf4"
    TEXT2    = "#8b93a8"
    BORDER   = "#2e3347"
    ACCENT   = "#4f8ef7"
    ACCENT2  = "#00d9b4"
    BADGE    = "#1e2a45"
    BADGE_T  = "#4f8ef7"
    HERO_BG  = "linear-gradient(135deg, #0f1117 0%, #1a1d27 100%)"
    CARD_SH  = "0 4px 24px rgba(0,0,0,0.4)"
    BTN_BG   = "#4f8ef7"
    BTN_TEXT = "#ffffff"
    ERR_BG   = "#2d1515"
    SUC_BG   = "#0d2a1f"
    INFO_BG  = "#0d1a2e"
else:
    BG       = "#f5f7ff"
    SURFACE  = "#ffffff"
    SURFACE2 = "#f0f4ff"
    TEXT     = "#1a1f36"
    TEXT2    = "#64748b"
    BORDER   = "#e2e8f0"
    ACCENT   = "#2d5bff"
    ACCENT2  = "#00d9b4"
    BADGE    = "#eff4ff"
    BADGE_T  = "#2d5bff"
    HERO_BG  = "linear-gradient(135deg, #f5f7ff 0%, #e8f0ff 100%)"
    CARD_SH  = "0 4px 24px rgba(45,91,255,0.08)"
    BTN_BG   = "#2d5bff"
    BTN_TEXT = "#ffffff"
    ERR_BG   = "#fff1f2"
    SUC_BG   = "#f0fdf4"
    INFO_BG  = "#eff6ff"

# ─────────────────────────────────────────────
# GLOBAL CSS
# ─────────────────────────────────────────────
st.markdown(f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;600;700;800&family=DM+Sans:ital,wght@0,300;0,400;0,500;0,600;1,400&display=swap');

:root {{
    --bg:       {BG};
    --surface:  {SURFACE};
    --surface2: {SURFACE2};
    --text:     {TEXT};
    --text2:    {TEXT2};
    --border:   {BORDER};
    --accent:   {ACCENT};
    --accent2:  {ACCENT2};
    --badge-bg: {BADGE};
    --badge-t:  {BADGE_T};
    --card-sh:  {CARD_SH};
    --btn-bg:   {BTN_BG};
    --btn-t:    {BTN_TEXT};
    --err-bg:   {ERR_BG};
    --suc-bg:   {SUC_BG};
    --info-bg:  {INFO_BG};
    --fs-base:  {BASE_FONT};
}}

/* Reset & base */
html, body {{
    font-size: var(--fs-base) !important;
    background: var(--bg) !important;
    color: var(--text) !important;
}}

*, *::before, *::after {{
    font-family: 'DM Sans', sans-serif !important;
    box-sizing: border-box;
}}

h1,h2,h3,h4,h5,h6,.syne {{
    font-family: 'Syne', sans-serif !important;
    color: var(--text) !important;
}}

/* Streamlit overrides */
.stApp {{ background: var(--bg) !important; }}
.block-container {{ padding: 1.5rem 2rem 3rem 2rem !important; max-width: 1200px !important; margin: 0 auto; }}
#MainMenu, footer, header {{ visibility: hidden !important; }}
section[data-testid="stSidebar"] {{ background: var(--surface) !important; border-right: 1px solid var(--border) !important; }}
.stMarkdown p, .stMarkdown li {{ color: var(--text) !important; font-size: var(--fs-base) !important; }}

/* Buttons */
.stButton > button {{
    font-family: 'DM Sans', sans-serif !important;
    font-weight: 600 !important;
    font-size: calc(var(--fs-base) * 0.95) !important;
    border-radius: 10px !important;
    padding: 0.6rem 1.4rem !important;
    transition: all 0.22s cubic-bezier(.4,0,.2,1) !important;
    border: 1.5px solid transparent !important;
}}
.stButton > button[kind="primary"] {{
    background: var(--btn-bg) !important;
    color: var(--btn-t) !important;
    box-shadow: 0 2px 12px rgba(45,91,255,0.25) !important;
}}
.stButton > button[kind="primary"]:hover {{
    transform: translateY(-2px) !important;
    box-shadow: 0 6px 20px rgba(45,91,255,0.35) !important;
}}
.stButton > button[kind="secondary"] {{
    background: var(--surface) !important;
    color: var(--accent) !important;
    border-color: var(--accent) !important;
}}
.stButton > button[kind="secondary"]:hover {{
    background: var(--badge-bg) !important;
    transform: translateY(-1px) !important;
}}

/* Inputs */
.stTextInput input, .stTextArea textarea, .stSelectbox select {{
    background: var(--surface) !important;
    color: var(--text) !important;
    border: 1.5px solid var(--border) !important;
    border-radius: 10px !important;
    font-family: 'DM Sans', sans-serif !important;
    font-size: var(--fs-base) !important;
    padding: 0.55rem 0.9rem !important;
    transition: border 0.2s;
}}
.stTextInput input:focus, .stTextArea textarea:focus {{
    border-color: var(--accent) !important;
    box-shadow: 0 0 0 3px rgba(45,91,255,0.12) !important;
}}
label {{ color: var(--text2) !important; font-size: calc(var(--fs-base) * 0.88) !important; font-weight: 500 !important; }}

/* Radio */
.stRadio > label {{ color: var(--text) !important; font-weight: 600 !important; }}
.stRadio [data-testid="stMarkdownContainer"] p {{ color: var(--text) !important; }}

/* Tabs */
.stTabs [data-baseweb="tab-list"] {{
    background: var(--surface2) !important;
    border-radius: 10px !important;
    padding: 4px !important;
    gap: 4px !important;
    border-bottom: none !important;
}}
.stTabs [data-baseweb="tab"] {{
    background: transparent !important;
    border-radius: 8px !important;
    color: var(--text2) !important;
    font-weight: 600 !important;
    border: none !important;
    padding: 0.45rem 1.2rem !important;
}}
.stTabs [aria-selected="true"] {{
    background: var(--surface) !important;
    color: var(--accent) !important;
    box-shadow: 0 1px 6px rgba(0,0,0,0.1) !important;
}}

/* Progress */
.stProgress > div > div {{ background: var(--accent) !important; border-radius: 99px !important; }}
.stProgress > div {{ background: var(--border) !important; border-radius: 99px !important; height: 8px !important; }}

/* Metrics */
[data-testid="metric-container"] {{
    background: var(--surface) !important;
    border: 1px solid var(--border) !important;
    border-radius: 14px !important;
    padding: 1.2rem !important;
}}
[data-testid="metric-container"] label {{ color: var(--text2) !important; }}
[data-testid="stMetricValue"] {{ color: var(--accent) !important; font-family: 'Syne', sans-serif !important; }}

/* Alerts */
.stAlert {{
    border-radius: 12px !important;
    border-left: 4px solid !important;
}}

/* Chat */
.stChatMessage {{
    background: var(--surface) !important;
    border: 1px solid var(--border) !important;
    border-radius: 14px !important;
    padding: 1rem !important;
}}
.stChatInputContainer {{ border-top: 1px solid var(--border) !important; }}
.stChatInputContainer textarea {{
    background: var(--surface) !important;
    color: var(--text) !important;
    border-radius: 12px !important;
}}

/* Expander */
.streamlit-expanderHeader {{
    background: var(--surface) !important;
    border-radius: 10px !important;
    color: var(--text) !important;
    font-weight: 600 !important;
}}
.streamlit-expanderContent {{
    background: var(--surface2) !important;
    border-radius: 0 0 10px 10px !important;
    color: var(--text) !important;
}}

/* Checkbox */
.stCheckbox label {{ color: var(--text) !important; }}

/* Divider */
hr {{ border-color: var(--border) !important; margin: 1.5rem 0 !important; }}

/* Scrollbar */
::-webkit-scrollbar {{ width: 6px; height: 6px; }}
::-webkit-scrollbar-track {{ background: var(--bg); }}
::-webkit-scrollbar-thumb {{ background: var(--border); border-radius: 99px; }}
::-webkit-scrollbar-thumb:hover {{ background: var(--accent); }}

/* ── Custom Components ── */
.eco-card {{
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 18px;
    padding: 1.5rem;
    box-shadow: var(--card-sh);
    transition: transform 0.2s, box-shadow 0.2s;
}}
.eco-card:hover {{ transform: translateY(-3px); box-shadow: 0 8px 32px rgba(45,91,255,0.12); }}

.eco-badge {{
    display: inline-block;
    background: var(--badge-bg);
    color: var(--badge-t);
    font-size: 0.75rem;
    font-weight: 700;
    letter-spacing: 0.04em;
    padding: 0.25rem 0.75rem;
    border-radius: 99px;
    text-transform: uppercase;
}}

.eco-pill {{
    display: inline-flex;
    align-items: center;
    gap: 0.4rem;
    background: var(--surface2);
    color: var(--text2);
    font-size: 0.82rem;
    padding: 0.3rem 0.8rem;
    border-radius: 99px;
    border: 1px solid var(--border);
}}

.hero-headline {{
    font-family: 'Syne', sans-serif !important;
    font-size: clamp(2.2rem, 5vw, 4rem);
    font-weight: 800;
    line-height: 1.1;
    color: var(--text) !important;
    margin: 0 0 1rem 0;
}}

.hero-sub {{
    font-size: clamp(1rem, 2vw, 1.2rem);
    color: var(--text2) !important;
    line-height: 1.7;
    margin-bottom: 2rem;
}}

.gradient-text {{
    background: linear-gradient(135deg, {ACCENT}, {ACCENT2});
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}}

.section-label {{
    font-size: 0.75rem;
    font-weight: 700;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    color: var(--accent) !important;
    margin-bottom: 0.5rem;
}}

.stat-ring {{
    width: 120px; height: 120px;
    border-radius: 50%;
    border: 8px solid var(--accent);
    display: flex; align-items: center; justify-content: center;
    font-family: 'Syne', sans-serif;
    font-size: 1.8rem; font-weight: 800;
    color: var(--accent);
    background: var(--surface);
    box-shadow: 0 0 0 4px var(--badge-bg);
    margin: 0 auto;
}}

.persona-card {{
    background: var(--surface);
    border: 2px solid var(--border);
    border-radius: 20px;
    padding: 2rem;
    text-align: center;
    transition: all 0.25s;
    cursor: pointer;
}}
.persona-card:hover {{
    border-color: var(--accent);
    transform: translateY(-4px);
    box-shadow: 0 12px 40px rgba(45,91,255,0.15);
}}
.persona-card.active {{
    border-color: var(--accent);
    background: var(--badge-bg);
}}

.task-item {{
    background: var(--surface);
    border: 1.5px solid var(--border);
    border-radius: 14px;
    padding: 1rem 1.25rem;
    margin-bottom: 0.75rem;
    transition: all 0.2s;
}}
.task-item.selected {{
    border-color: var(--accent);
    background: var(--badge-bg);
    box-shadow: 0 0 0 3px rgba(45,91,255,0.12);
}}
.task-item.done {{
    opacity: 0.55;
    background: var(--suc-bg);
    border-color: #86efac;
}}

.nav-top {{
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 1rem 0 1.5rem 0;
    border-bottom: 1px solid var(--border);
    margin-bottom: 2rem;
    flex-wrap: wrap;
    gap: 0.75rem;
}}
.nav-logo {{
    font-family: 'Syne', sans-serif;
    font-size: 1.4rem;
    font-weight: 800;
    color: var(--accent) !important;
    text-decoration: none;
}}
.nav-links {{
    display: flex;
    gap: 1.5rem;
    flex-wrap: wrap;
    align-items: center;
}}
.nav-link {{
    font-size: 0.9rem;
    font-weight: 500;
    color: var(--text2) !important;
    text-decoration: none;
    transition: color 0.15s;
    cursor: pointer;
}}
.nav-link:hover {{ color: var(--accent) !important; }}

.footer-grid {{
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(160px, 1fr));
    gap: 2rem;
    padding: 2.5rem 0 1.5rem 0;
    border-top: 1px solid var(--border);
    margin-top: 3rem;
}}
.footer-col h4 {{
    font-family: 'Syne', sans-serif !important;
    font-size: 0.85rem;
    font-weight: 700;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    color: var(--text2) !important;
    margin-bottom: 0.75rem;
}}
.footer-link {{
    display: block;
    font-size: 0.88rem;
    color: var(--text2) !important;
    text-decoration: none;
    margin-bottom: 0.4rem;
    transition: color 0.15s;
    cursor: pointer;
}}
.footer-link:hover {{ color: var(--accent) !important; }}

.float-fab {{
    position: fixed;
    bottom: 2rem;
    right: 2rem;
    width: 56px; height: 56px;
    background: var(--accent);
    color: white;
    border-radius: 50%;
    display: flex; align-items: center; justify-content: center;
    font-size: 1.5rem;
    box-shadow: 0 4px 20px rgba(45,91,255,0.4);
    cursor: pointer;
    z-index: 9999;
    border: none;
    transition: all 0.2s;
}}
.float-fab:hover {{ transform: scale(1.1); box-shadow: 0 6px 28px rgba(45,91,255,0.5); }}

.kbd {{
    display: inline-block;
    background: var(--surface2);
    border: 1px solid var(--border);
    border-radius: 5px;
    padding: 0.15rem 0.45rem;
    font-size: 0.78rem;
    font-family: monospace !important;
    color: var(--text2) !important;
    box-shadow: 0 1px 0 var(--border);
}}

@keyframes fadeInUp {{
    from {{ opacity: 0; transform: translateY(18px); }}
    to   {{ opacity: 1; transform: translateY(0); }}
}}
.animate-in {{ animation: fadeInUp 0.45s ease both; }}
.delay-1 {{ animation-delay: 0.1s; }}
.delay-2 {{ animation-delay: 0.2s; }}
.delay-3 {{ animation-delay: 0.3s; }}

@media (max-width: 768px) {{
    .block-container {{ padding: 1rem !important; }}
    .hero-headline {{ font-size: 2rem; }}
    .nav-links {{ gap: 0.75rem; }}
}}
</style>
""", unsafe_allow_html=True)


# ─────────────────────────────────────────────
# HELPERS
# ─────────────────────────────────────────────
def tx(key): return t(key, st.session_state.lang)

AFFINITY_WEIGHTS = {tx("aff_1"): 2, tx("aff_2"): 1, tx("aff_3"): 0, tx("aff_4"): -1}
# also map en keys just in case
_AW_MAP = {
    "Me identifico totalmente":2,"Me identifico parcialmente":1,
    "Não me identifico muito":0,"Não me identifico":-1,
    "Fully identify":2,"Partially identify":1,"Barely identify":0,"Do not identify":-1,
}

def compute_profile():
    scores = {"Executor":0, "Organizador":0, "Criativo":0,
              "Organizer":0, "Creative":0}
    for q_idx, q_ans in st.session_state.answers.items():
        for profile_key, affinity in q_ans.items():
            w = _AW_MAP.get(affinity, 0)
            scores[profile_key] = scores.get(profile_key, 0) + w
    # merge en->pt keys
    scores["Executor"]    = scores.get("Executor", 0)
    scores["Organizador"] = scores.get("Organizador", 0) + scores.get("Organizer", 0)
    scores["Criativo"]    = scores.get("Criativo", 0) + scores.get("Creative", 0)
    best_pt = max(["Executor","Organizador","Criativo"], key=lambda k: scores[k])
    icons = {"Executor":"🎯","Organizador":"📋","Criativo":"💡"}
    return f"{icons[best_pt]} {best_pt}"

def get_profile_key():
    if not st.session_state.profile:
        return "Executor"
    for k in ["Executor","Organizador","Criativo"]:
        if k in st.session_state.profile:
            return k
    return "Executor"

def navigate(page, step=None):
    st.session_state.page = page
    if step:
        st.session_state.step = step
    st.rerun()

def clear_journey():
    for k in ["step","q_index","answers","tasks_completed","completed_tasks",
              "selected_task","iap_score","profile","messages"]:
        st.session_state[k] = DEFAULTS[k]

# ─────────────────────────────────────────────
# TOP NAVBAR
# ─────────────────────────────────────────────
def show_navbar(show_app_links=False):
    lang_icon = "🇧🇷" if st.session_state.lang == "pt" else "🇺🇸"
    is_logged = st.session_state.logged_in

    st.markdown(f"""
    <div class="nav-top animate-in">
        <span class="nav-logo">⬡ EcoNexo</span>
        <div class="nav-links" id="nav-links">
            <span class="eco-pill">{lang_icon} {st.session_state.lang.upper()}</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Nav buttons row
    nav_cols = st.columns([2, 1, 1, 1, 1, 1, 1, 1])
    with nav_cols[1]:
        if st.button(tx("nav_home"), use_container_width=True, key="nav_home_btn"):
            navigate("landing")
    with nav_cols[2]:
        if st.button(tx("nav_features"), use_container_width=True, key="nav_feat_btn"):
            navigate("features")
    with nav_cols[3]:
        if st.button(tx("nav_about"), use_container_width=True, key="nav_about_btn"):
            navigate("about")
    with nav_cols[4]:
        if st.button(tx("nav_contact"), use_container_width=True, key="nav_contact_btn"):
            navigate("contact")
    with nav_cols[5]:
        new_lang = "en" if st.session_state.lang == "pt" else "pt"
        lbl = "🇺🇸 EN" if st.session_state.lang == "pt" else "🇧🇷 PT"
        if st.button(lbl, use_container_width=True, key="nav_lang_btn"):
            st.session_state.lang = new_lang
            st.rerun()
    with nav_cols[6]:
        if is_logged:
            if st.button(tx("nav_logout"), use_container_width=True, key="nav_logout_btn"):
                for k in list(st.session_state.keys()):
                    del st.session_state[k]
                st.rerun()
        else:
            if st.button(tx("nav_login"), use_container_width=True, key="nav_login_btn", type="primary"):
                navigate("login")
    with nav_cols[7]:
        # Theme toggle
        theme_lbl = "🌙" if not IS_DARK else "☀️"
        if st.button(theme_lbl, use_container_width=True, key="nav_theme_btn"):
            st.session_state.theme = "dark" if not IS_DARK else "light"
            st.rerun()


# ─────────────────────────────────────────────
# FOOTER
# ─────────────────────────────────────────────
def show_footer():
    st.markdown(f"""
    <div class="footer-grid animate-in">
        <div class="footer-col">
            <h4>⬡ EcoNexo</h4>
            <p style="font-size:0.83rem;color:var(--text2);line-height:1.6;">
                Produtividade guiada por IA para o seu crescimento real.
            </p>
        </div>
        <div class="footer-col">
            <h4>{tx("nav_home")}</h4>
            <a class="footer-link" href="#" onclick="void(0)">Landing Page</a>
            <a class="footer-link" href="#" onclick="void(0)">{tx("nav_features")}</a>
            <a class="footer-link" href="#" onclick="void(0)">{tx("nav_about")}</a>
        </div>
        <div class="footer-col">
            <h4>App</h4>
            <a class="footer-link" href="#" onclick="void(0)">Questionário</a>
            <a class="footer-link" href="#" onclick="void(0)">Vitrine de Tarefas</a>
            <a class="footer-link" href="#" onclick="void(0)">IAP & Perfil</a>
            <a class="footer-link" href="#" onclick="void(0)">Assistente IA</a>
        </div>
        <div class="footer-col">
            <h4>Suporte</h4>
            <a class="footer-link" href="#" onclick="void(0)">{tx("nav_contact")}</a>
            <a class="footer-link" href="#" onclick="void(0)">{tx("nav_lgpd")}</a>
            <a class="footer-link" href="#" onclick="void(0)">Preferências</a>
        </div>
        <div class="footer-col">
            <h4>Redes</h4>
            <a class="footer-link" href="#" onclick="void(0)">LinkedIn</a>
            <a class="footer-link" href="#" onclick="void(0)">Instagram</a>
            <a class="footer-link" href="#" onclick="void(0)">GitHub</a>
        </div>
    </div>
    <div style="text-align:center;padding:1rem 0;color:var(--text2);font-size:0.82rem;border-top:1px solid var(--border);">
        {tx("footer_rights")}
    </div>
    """, unsafe_allow_html=True)

    # Footer nav buttons (Streamlit)
    fc1, fc2, fc3, fc4, fc5, fc6 = st.columns(6)
    with fc1:
        if st.button("🏠 Home", key="f_home", use_container_width=True):
            navigate("landing")
    with fc2:
        if st.button("📖 Features", key="f_feat", use_container_width=True):
            navigate("features")
    with fc3:
        if st.button("👥 Sobre", key="f_about", use_container_width=True):
            navigate("about")
    with fc4:
        if st.button("📬 Contato", key="f_contact", use_container_width=True):
            navigate("contact")
    with fc5:
        if st.button("🔒 LGPD", key="f_lgpd", use_container_width=True):
            navigate("lgpd")
    with fc6:
        if st.button("⚙️ Prefs", key="f_prefs", use_container_width=True):
            if st.session_state.logged_in:
                st.session_state.step = "settings"
                navigate("app")
            else:
                navigate("login")


# ─────────────────────────────────────────────
# FLOATING ACTION BUTTON
# ─────────────────────────────────────────────
def show_floating_menu():
    st.markdown("""
    <style>
    .fab-container {
        position: fixed; bottom: 2rem; right: 2rem; z-index: 9999;
        display: flex; flex-direction: column-reverse; align-items: flex-end; gap: 0.6rem;
    }
    .fab-main {
        width:56px;height:56px;border-radius:50%;
        background:var(--accent);color:#fff;font-size:1.5rem;
        display:flex;align-items:center;justify-content:center;
        box-shadow:0 4px 20px rgba(45,91,255,0.4);cursor:pointer;
        border:none; transition:all 0.2s;
    }
    .fab-main:hover{transform:scale(1.1);}
    </style>
    <div class="fab-container">
        <div class="fab-main" title="Menu rápido">⚡</div>
    </div>
    """, unsafe_allow_html=True)

    with st.expander("⚡ Menu Rápido", expanded=False):
        c1, c2 = st.columns(2)
        with c1:
            if st.button("🏠 Home", key="fab_home", use_container_width=True):
                navigate("landing")
            if st.button("📬 Contato", key="fab_contact", use_container_width=True):
                navigate("contact")
            if st.button("🌙 Tema", key="fab_theme", use_container_width=True):
                st.session_state.theme = "dark" if not IS_DARK else "light"
                st.rerun()
        with c2:
            if st.session_state.logged_in:
                if st.button("🤖 IA Chat", key="fab_chat", use_container_width=True):
                    st.session_state.step = "chat"
                    navigate("app")
                if st.button("👤 Perfil", key="fab_profile", use_container_width=True):
                    st.session_state.step = "user_page"
                    navigate("app")
            new_lang = "en" if st.session_state.lang == "pt" else "pt"
            lbl2 = "🇺🇸 EN" if st.session_state.lang == "pt" else "🇧🇷 PT"
            if st.button(lbl2, key="fab_lang", use_container_width=True):
                st.session_state.lang = new_lang
                st.rerun()


# ─────────────────────────────────────────────
# ══════ PAGES ══════
# ─────────────────────────────────────────────

# ── LANDING PAGE ──────────────────────────────
def page_landing():
    show_navbar()

    # Hero
    col1, col2 = st.columns([1.1, 0.9], gap="large")
    with col1:
        st.markdown(f"""
        <div class="animate-in" style="padding: 1rem 0 2rem 0;">
            <div class="section-label">v2.0 — IA + SQL + Bilíngue</div>
            <h1 class="hero-headline">
                {tx("hero_title_1")}
                <span class="gradient-text"> {tx("hero_title_2")}</span><br>
                {tx("hero_title_3")}
            </h1>
            <p class="hero-sub">{tx("hero_sub")}</p>
            <div style="display:flex;gap:0.5rem;flex-wrap:wrap;margin-bottom:1.5rem;">
                <span class="eco-badge">🤖 IA Integrada</span>
                <span class="eco-badge">📊 IAP Score</span>
                <span class="eco-badge">💾 SQL Persistente</span>
                <span class="eco-badge">🌐 PT | EN</span>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        btn_c1, btn_c2 = st.columns(2)
        with btn_c1:
            if st.button(tx("btn_start"), key="land_start", use_container_width=True, type="primary"):
                navigate("login")
        with btn_c2:
            if st.button(tx("btn_learn"), key="land_learn", use_container_width=True):
                navigate("features")

    with col2:
        for icon, name_key, desc_key in [
            ("🎯", "executor_name", "executor_desc"),
            ("📋", "organizer_name", "organizer_desc"),
            ("💡", "creative_name", "creative_desc"),
        ]:
            st.markdown(f"""
            <div class="eco-card animate-in" style="margin-bottom:1rem;">
                <div style="display:flex;align-items:center;gap:0.75rem;margin-bottom:0.5rem;">
                    <span style="font-size:1.8rem;">{icon}</span>
                    <strong style="font-family:'Syne',sans-serif;font-size:1.05rem;color:var(--accent);">{tx(name_key)}</strong>
                </div>
                <p style="color:var(--text2);margin:0;font-size:0.92rem;">{tx(desc_key)}</p>
            </div>
            """, unsafe_allow_html=True)

    # Stats row
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("---")
    sc1, sc2, sc3, sc4 = st.columns(4)
    for col, val, label in [
        (sc1, "2.4k+", "Usuários ativos"),
        (sc2, "91%", "Taxa de conclusão"),
        (sc3, "7", "Perguntas de perfil"),
        (sc4, "8", "Tarefas disponíveis"),
    ]:
        with col:
            st.markdown(f"""
            <div style="text-align:center;padding:1.5rem 1rem;">
                <div style="font-family:'Syne',sans-serif;font-size:2.2rem;font-weight:800;color:var(--accent);">{val}</div>
                <div style="color:var(--text2);font-size:0.88rem;margin-top:0.25rem;">{label}</div>
            </div>
            """, unsafe_allow_html=True)

    show_footer()
    show_floating_menu()


# ── FEATURES PAGE ─────────────────────────────
def page_features():
    show_navbar()
    st.markdown(f"<div class='section-label animate-in'>Plataforma</div>", unsafe_allow_html=True)
    st.markdown(f"<h1 class='hero-headline animate-in'>Como Funciona</h1>", unsafe_allow_html=True)
    st.markdown("---")

    feats = [
        ("📊","Análise de Perfil","7 perguntas com escala de afinidade identificam se você é Executor, Organizador ou Criativo — com lógica de pontuação real."),
        ("🎯","Vitrine de Tarefas","Escolha as tarefas que quer executar. Tarefas recomendadas para o seu perfil são destacadas com badge ⭐."),
        ("📈","IAP Score","Índice de Autonomia Produtiva com detalhamento por Iniciativa, Execução e Conclusão."),
        ("🤖","Assistente IA","Chat personalizado com IA (Anthropic Claude) integrado ao seu perfil e histórico."),
        ("💾","Memória SQL","Histórico de sessões, tarefas e conversas persistido em banco de dados."),
        ("🌐","Bilíngue PT|EN","Interface completa em Português e Inglês, alternável a qualquer momento."),
        ("🌙","Modo Claro|Escuro","Tema alternável com um clique, preservado por sessão."),
        ("♿","Acessibilidade","Três tamanhos de fonte, contraste adequado e navegação por teclado."),
    ]
    
    c1, c2 = st.columns(2)
    for i, (icon, title, desc) in enumerate(feats):
        with (c1 if i % 2 == 0 else c2):
            st.markdown(f"""
            <div class="eco-card animate-in" style="margin-bottom:1rem;">
                <div style="display:flex;align-items:flex-start;gap:1rem;">
                    <span style="font-size:2rem;line-height:1;">{icon}</span>
                    <div>
                        <strong style="font-family:'Syne',sans-serif;color:var(--text);display:block;margin-bottom:0.3rem;">{title}</strong>
                        <span style="color:var(--text2);font-size:0.9rem;line-height:1.5;">{desc}</span>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    b1, b2, b3 = st.columns([1, 1, 4])
    with b1:
        if st.button("← Voltar", use_container_width=True):
            navigate("landing")
    with b2:
        if st.button("Começar →", use_container_width=True, type="primary"):
            navigate("login")
    show_footer()
    show_floating_menu()


# ── LOGIN PAGE ────────────────────────────────
def page_login():
    show_navbar()
    _, mid, _ = st.columns([1, 1.4, 1])
    with mid:
        st.markdown(f"""
        <div class="eco-card animate-in" style="padding:2.5rem;">
            <h2 style="font-family:'Syne',sans-serif;margin-bottom:1.5rem;text-align:center;">
                {tx("login_title")}
            </h2>
        </div>
        """, unsafe_allow_html=True)

        tab1, tab2 = st.tabs([tx("tab_login"), tx("tab_signup")])

        with tab1:
            with st.form("login_form", clear_on_submit=False):
                email = st.text_input(tx("field_email"), placeholder="seu@email.com")
                password = st.text_input(tx("field_password"), type="password", placeholder="••••••••")
                c1, c2 = st.columns(2)
                with c1:
                    sub = st.form_submit_button(tx("btn_login"), use_container_width=True, type="primary")
                with c2:
                    clr = st.form_submit_button("🗑️ Limpar", use_container_width=True)
                if sub:
                    if not email or not password:
                        st.error(tx("err_fill"))
                    else:
                        user = None
                        if DB_AVAILABLE:
                            user = db.authenticate_user(email, password)
                        else:
                            user = {"id": "demo", "name": email.split('@')[0].title(), "email": email,
                                    "lang": "pt", "theme": "light", "font_size": "md"}
                        if user:
                            st.session_state.logged_in = True
                            st.session_state.user_id = user["id"]
                            st.session_state.user_name = user["name"]
                            st.session_state.user_email = user["email"]
                            st.session_state.lang = user.get("lang", "pt")
                            st.session_state.theme = user.get("theme", "light")
                            st.session_state.font_size = user.get("font_size", "md")
                            if DB_AVAILABLE:
                                msgs = db.load_chat_history(user["id"])
                                st.session_state.messages = msgs
                            st.success(tx("login_success"))
                            navigate("app", "questionnaire")
                        else:
                            st.error(tx("err_credentials"))

        with tab2:
            with st.form("signup_form", clear_on_submit=False):
                name = st.text_input(tx("field_name"), placeholder="Seu nome completo")
                email_s = st.text_input(tx("field_email"), placeholder="seu@email.com", key="em_s")
                pw_s = st.text_input(tx("field_password"), type="password", placeholder="Mín. 8 caracteres", key="pw_s")
                agree = st.checkbox(tx("lgpd_agree"))
                cs1, cs2 = st.columns(2)
                with cs1:
                    sub_s = st.form_submit_button(tx("btn_signup"), use_container_width=True, type="primary")
                with cs2:
                    clr_s = st.form_submit_button("🗑️ Limpar", use_container_width=True)
                if sub_s:
                    if not all([name, email_s, pw_s]):
                        st.error(tx("err_fill"))
                    elif not agree:
                        st.error(tx("err_lgpd"))
                    elif len(pw_s) < 8:
                        st.error(tx("err_pw_len"))
                    else:
                        user = None
                        if DB_AVAILABLE:
                            user = db.create_user(name, email_s, pw_s)
                        else:
                            user = {"id": "demo", "name": name.split()[0].title(), "email": email_s}
                        if user:
                            st.session_state.logged_in = True
                            st.session_state.user_id = user["id"]
                            st.session_state.user_name = user["name"]
                            st.session_state.user_email = email_s
                            st.success(tx("signup_success"))
                            navigate("app", "questionnaire")
                        else:
                            st.error(tx("err_email_exists"))

        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("← Voltar", use_container_width=True, key="login_back"):
            navigate("landing")
    show_floating_menu()


# ── ABOUT PAGE ────────────────────────────────
def page_about():
    show_navbar()
    st.markdown(f"<div class='section-label animate-in'>A Empresa</div>", unsafe_allow_html=True)
    st.markdown(f"<h1 class='hero-headline animate-in'>{tx('about_title')}</h1>", unsafe_allow_html=True)
    st.markdown("---")

    c1, c2 = st.columns([1.2, 0.8])
    with c1:
        st.markdown(f"""
        <div class="eco-card animate-in">
            <h3>Sobre o EcoNexo's System</h3>
            <p style="color:var(--text2);line-height:1.8;">
                O <strong>EcoNexo's System</strong> nasceu da observação de um problema comum:
                muitas pessoas sabem o que precisam fazer, mas não sabem <em>como</em> começar
                ou manter a consistência.
            </p>
            <p style="color:var(--text2);line-height:1.8;margin-top:1rem;">
                Criamos uma plataforma que identifica seu perfil de trabalho natural
                (Executor, Organizador ou Criativo) e oferece <strong>execução guiada por IA</strong>
                — transformando intenção em ação real e mensurável.
            </p>
            <h3 style="margin-top:1.5rem;">{tx("about_mission")}</h3>
            <p style="color:var(--text2);line-height:1.8;">
                Desenvolver <strong>autonomia produtiva real</strong> através de tecnologia
                acessível, personalizada e baseada em ciência comportamental.
            </p>
        </div>
        """, unsafe_allow_html=True)
    with c2:
        st.markdown(f"<h3>{tx('about_values')}</h3>", unsafe_allow_html=True)
        for icon, title, desc in [
            ("🎯","Foco no Resultado","Medimos sucesso por tarefas concluídas, não por tempo gasto."),
            ("🤝","Personalização","Cada perfil recebe uma experiência única e adaptada."),
            ("🔐","Transparência","Dados protegidos. Conformidade total com a LGPD."),
            ("♿","Acessibilidade","Plataforma inclusiva, adaptada para todos os usuários."),
        ]:
            st.markdown(f"""
            <div class="eco-card animate-in" style="margin-bottom:0.75rem;">
                <div style="display:flex;gap:0.75rem;align-items:flex-start;">
                    <span style="font-size:1.4rem;">{icon}</span>
                    <div>
                        <strong style="color:var(--accent);">{title}</strong><br>
                        <span style="color:var(--text2);font-size:0.88rem;">{desc}</span>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)

    if st.button("← Voltar", key="about_back"):
        navigate("landing")
    show_footer()
    show_floating_menu()


# ── LGPD PAGE ─────────────────────────────────
def page_lgpd():
    show_navbar()
    st.markdown("<div class='section-label'>Legal</div>", unsafe_allow_html=True)
    st.markdown("<h1 class='hero-headline'>Privacidade & LGPD</h1>", unsafe_allow_html=True)
    st.markdown("---")

    sections = [
        ("📋 Dados Coletados", """Coletamos apenas as informações essenciais:
- **Cadastro:** nome, e-mail, senha (hash bcrypt)
- **Perfil:** respostas ao questionário
- **Uso:** histórico de tarefas e IAP
- **Técnico:** IP e navegador (segurança)"""),
        ("🎯 Como Usamos", """- Acesso personalizado à plataforma
- Identificação de perfil (Executor, Organizador, Criativo)
- Sugestões de tarefas via IA
- Cálculo do IAP
- Melhoria contínua da experiência"""),
        ("✅ Seus Direitos", """Você pode a qualquer momento:
- ✓ **Acessar** todos os dados armazenados
- ✓ **Corrigir** informações desatualizadas
- ✓ **Deletar** sua conta permanentemente
- ✓ **Exportar** seus dados
- ✓ **Revogar** o consentimento"""),
        ("🔐 Segurança", """- SSL/TLS em todas as conexões
- Senhas com bcrypt (salt + hash)
- Backups diários criptografados
- Acesso restrito com MFA"""),
    ]

    for title, content in sections:
        with st.expander(title, expanded=True):
            st.markdown(content)

    st.info("📧 **DPO:** privacidade@econexo.com | Resposta em até 5 dias úteis")
    if st.button("← Voltar", key="lgpd_back"):
        navigate("landing")
    show_footer()
    show_floating_menu()


# ── CONTACT PAGE ──────────────────────────────
def page_contact():
    show_navbar()
    st.markdown("<div class='section-label animate-in'>Suporte</div>", unsafe_allow_html=True)
    st.markdown(f"<h1 class='hero-headline animate-in'>{tx('contact_title')}</h1>", unsafe_allow_html=True)
    st.markdown("---")

    c1, c2 = st.columns([1.3, 0.7])
    with c1:
        with st.form("contact_form", clear_on_submit=True):
            n = st.text_input(tx("contact_name"), placeholder="Seu nome")
            e = st.text_input(tx("contact_email"), placeholder="seu@email.com")
            s = st.text_input(tx("contact_subject"), placeholder="Assunto da mensagem")
            m = st.text_area(tx("contact_message"), placeholder="Escreva sua mensagem aqui...", height=140)
            fc1, fc2, fc3 = st.columns(3)
            with fc1:
                send = st.form_submit_button(tx("btn_send"), use_container_width=True, type="primary")
            with fc2:
                clr = st.form_submit_button("🗑️ Limpar", use_container_width=True)

            if send:
                if all([n, e, m]):
                    if DB_AVAILABLE:
                        db.save_contact_message(n, e, s, m)
                    st.success(tx("contact_sent"))
                else:
                    st.error(tx("err_fill"))

    with c2:
        st.markdown(f"""
        <div class="eco-card animate-in">
            <h3>Canais de Atendimento</h3>
            <div style="margin-top:1rem;">
                <div style="margin-bottom:1rem;">
                    <span style="font-size:1.3rem;">📧</span>
                    <strong style="display:block;margin-top:0.25rem;color:var(--accent);">E-mail</strong>
                    <span style="color:var(--text2);font-size:0.88rem;">suporte@econexo.com</span>
                </div>
                <div style="margin-bottom:1rem;">
                    <span style="font-size:1.3rem;">💬</span>
                    <strong style="display:block;margin-top:0.25rem;color:var(--accent);">Resposta</strong>
                    <span style="color:var(--text2);font-size:0.88rem;">Até 2 dias úteis</span>
                </div>
                <div style="margin-bottom:1rem;">
                    <span style="font-size:1.3rem;">🌐</span>
                    <strong style="display:block;margin-top:0.25rem;color:var(--accent);">LinkedIn</strong>
                    <span style="color:var(--text2);font-size:0.88rem;">@econexo</span>
                </div>
                <div>
                    <span style="font-size:1.3rem;">🔒</span>
                    <strong style="display:block;margin-top:0.25rem;color:var(--accent);">DPO / LGPD</strong>
                    <span style="color:var(--text2);font-size:0.88rem;">privacidade@econexo.com</span>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    if st.button("← Voltar", key="contact_back"):
        navigate("landing")
    show_footer()
    show_floating_menu()


# ─────────────────────────────────────────────
# APP SHELL (logged in)
# ─────────────────────────────────────────────
def show_app():
    with st.sidebar:
        st.markdown(f"""
        <div style="padding:1rem 0;">
            <div style="font-family:'Syne',sans-serif;font-size:1.3rem;font-weight:800;color:var(--accent);">⬡ EcoNexo</div>
            <div style="color:var(--text2);font-size:0.85rem;margin-top:0.25rem;">👋 {st.session_state.user_name}</div>
        </div>
        """, unsafe_allow_html=True)
        st.markdown("---")

        # Progress
        st.markdown("<strong>📊 Progresso</strong>", unsafe_allow_html=True)
        done = st.session_state.tasks_completed
        st.progress(min(done / 3, 1.0))
        st.caption(f"{done}/3 {tx('tasks_done')}")
        if st.session_state.iap_score:
            st.metric("IAP", f"{st.session_state.iap_score}%", "↑")
        if st.session_state.profile:
            st.markdown(f"<div class='eco-badge'>{st.session_state.profile}</div>", unsafe_allow_html=True)

        st.markdown("---")
        st.markdown("<strong>🗺️ Jornada</strong>", unsafe_allow_html=True)

        steps = [
            ("questionnaire", "📋 Questionário"),
            ("tasks", "🎯 Tarefas"),
            ("iap", "📊 IAP"),
            ("profile", "👤 Perfil"),
            ("chat", "🤖 IA Chat"),
        ]
        for skey, slabel in steps:
            btn_type = "primary" if st.session_state.step == skey else "secondary"
            if st.button(slabel, key=f"sb_{skey}", use_container_width=True, type=btn_type):
                st.session_state.step = skey
                st.rerun()

        st.markdown("---")
        st.markdown("<strong>⚙️ Conta</strong>", unsafe_allow_html=True)

        if st.button("👤 Minha Página", use_container_width=True, key="sb_user"):
            st.session_state.step = "user_page"
            st.rerun()
        if st.button("⚙️ Preferências", use_container_width=True, key="sb_settings"):
            st.session_state.step = "settings"
            st.rerun()
        if st.button("🚪 Sair", use_container_width=True, key="sb_logout"):
            for k in list(st.session_state.keys()):
                del st.session_state[k]
            st.rerun()

    # Main area
    step_router = {
        "questionnaire": step_questionnaire,
        "tasks":         step_tasks,
        "iap":           step_iap,
        "profile":       step_profile,
        "chat":          step_chat,
        "user_page":     step_user_page,
        "settings":      step_settings,
    }
    step_router.get(st.session_state.step, step_questionnaire)()
    show_floating_menu()


# ─────────────────────────────────────────────
# STEP: QUESTIONNAIRE
# ─────────────────────────────────────────────
def step_questionnaire():
    qs = QUESTIONS[st.session_state.lang]
    total = len(qs)
    idx = st.session_state.q_index
    lang_affinity = [tx("aff_1"), tx("aff_2"), tx("aff_3"), tx("aff_4")]

    st.markdown(f"<div class='section-label animate-in'>{tx('q_title')}</div>", unsafe_allow_html=True)

    # Progress
    prog_pct = (idx + 1) / total
    st.progress(prog_pct)
    st.caption(f"{tx('q_question')} {idx+1} {tx('q_of')} {total}")

    q = qs[idx]
    st.markdown(f"""
    <div class="eco-card animate-in" style="margin:1.5rem 0;">
        <h2 style="font-family:'Syne',sans-serif;font-size:1.4rem;margin-bottom:0.5rem;">{q['q']}</h2>
        <p style="color:var(--text2);font-size:0.9rem;margin:0;">{tx('q_identify')}</p>
    </div>
    """, unsafe_allow_html=True)

    saved = st.session_state.answers.get(idx, {})
    current_answers = {}

    for profile_key, opt_text in q["opts"]:
        st.markdown(f"""
        <div class="task-item" style="margin-bottom:0.5rem;">
            <strong>{opt_text}</strong>
        </div>
        """, unsafe_allow_html=True)
        default_idx = lang_affinity.index(saved.get(profile_key, lang_affinity[1]))
        answer = st.radio(
            "›",
            lang_affinity,
            index=default_idx,
            key=f"q{idx}_{profile_key}",
            horizontal=True,
            label_visibility="collapsed",
        )
        current_answers[profile_key] = answer
        st.markdown("<div style='height:0.25rem;'></div>", unsafe_allow_html=True)

    # Navigation
    st.markdown("<br>", unsafe_allow_html=True)
    nc1, nc2, nc3, nc4, nc5 = st.columns([1, 1, 2, 1, 1])
    with nc1:
        if st.button("⏮ Início", use_container_width=True, key="q_first", disabled=idx==0):
            st.session_state.answers[idx] = current_answers
            st.session_state.q_index = 0
            st.rerun()
    with nc2:
        if st.button(tx("btn_prev"), use_container_width=True, key="q_prev", disabled=idx==0):
            st.session_state.answers[idx] = current_answers
            st.session_state.q_index -= 1
            st.rerun()
    with nc4:
        # Save progress
        if st.button("💾 Salvar", use_container_width=True, key="q_save"):
            st.session_state.answers[idx] = current_answers
            st.success("Progresso salvo!")
    with nc5:
        is_last = idx == total - 1
        lbl = tx("btn_finish") if is_last else tx("btn_next")
        if st.button(lbl, use_container_width=True, key="q_next", type="primary"):
            st.session_state.answers[idx] = current_answers
            if is_last:
                st.session_state.profile = compute_profile()
                if DB_AVAILABLE and st.session_state.user_id:
                    db.save_profile(st.session_state.user_id, st.session_state.profile, 0,
                                    {str(k): v for k, v in st.session_state.answers.items()})
                st.session_state.step = "tasks"
                st.rerun()
            else:
                st.session_state.q_index += 1
                st.rerun()

    # Keyboard hint
    st.markdown(f"""
    <div style="text-align:center;margin-top:1rem;color:var(--text2);font-size:0.8rem;">
        Dica: use <span class="kbd">←</span> <span class="kbd">→</span> para navegar
    </div>
    """, unsafe_allow_html=True)


# ─────────────────────────────────────────────
# STEP: TASKS
# ─────────────────────────────────────────────
def step_tasks():
    tasks = TASKS[st.session_state.lang]
    pk = get_profile_key()
    # Map en/pt profile names
    pk_map = {"Executor":"Executor","Organizador":"Organizador","Organizer":"Organizador","Criativo":"Criativo","Creative":"Criativo"}
    pk_norm = pk_map.get(pk, pk)

    st.markdown(f"<div class='section-label animate-in'>{tx('tasks_title')}</div>", unsafe_allow_html=True)
    st.markdown(f"<h2 class='hero-headline animate-in' style='font-size:1.8rem;'>{tx('tasks_title')}</h2>", unsafe_allow_html=True)

    done_count = st.session_state.tasks_completed
    st.progress(min(done_count / 3, 1.0))
    col_prog, col_info = st.columns([3, 1])
    with col_prog:
        st.caption(f"**{done_count}/3** {tx('tasks_done')}")
    with col_info:
        if st.session_state.profile:
            st.markdown(f"<div class='eco-badge'>{st.session_state.profile}</div>", unsafe_allow_html=True)

    if st.session_state.profile:
        st.info(f"⭐ Tarefas marcadas são recomendadas para o perfil **{st.session_state.profile}**")

    st.markdown("<br>", unsafe_allow_html=True)

    # Task grid
    tc1, tc2 = st.columns(2)
    for i, task in enumerate(tasks):
        tid = task["id"]
        is_done = tid in st.session_state.completed_tasks
        is_sel = st.session_state.selected_task == tid
        task_profile_norm = pk_map.get(task["profile"], task["profile"])
        is_rec = task_profile_norm == pk_norm

        col = tc1 if i % 2 == 0 else tc2
        with col:
            card_class = "task-item done" if is_done else ("task-item selected" if is_sel else "task-item")
            rec_tag = f'<span class="eco-badge" style="float:right;">{tx("task_recommended")}</span>' if is_rec else ""
            done_tag = f'<span style="color:#16a34a;font-weight:600;">{tx("task_done_label")}</span>' if is_done else ""

            st.markdown(f"""
            <div class="{card_class} animate-in">
                <div style="display:flex;justify-content:space-between;align-items:flex-start;margin-bottom:0.4rem;">
                    <span style="font-size:1.5rem;">{task['icon']}</span>
                    {rec_tag}
                </div>
                <strong style="font-size:0.97rem;">{task['name']}</strong><br>
                <span style="color:var(--text2);font-size:0.84rem;">{task['desc']}</span><br>
                {done_tag}
            </div>
            """, unsafe_allow_html=True)

            if not is_done:
                if is_sel:
                    b1, b2 = st.columns(2)
                    with b1:
                        if st.button(f"▶ {tx('btn_start_task')}", key=f"start_{tid}", use_container_width=True, type="primary"):
                            st.session_state.completed_tasks.add(tid)
                            st.session_state.tasks_completed = len(st.session_state.completed_tasks)
                            st.session_state.selected_task = None
                            if DB_AVAILABLE and st.session_state.user_id:
                                db.save_task_completion(st.session_state.user_id, tid, task["name"])
                            if st.session_state.tasks_completed >= 3:
                                st.session_state.step = "iap"
                            st.rerun()
                    with b2:
                        if st.button(tx("btn_cancel"), key=f"cancel_{tid}", use_container_width=True):
                            st.session_state.selected_task = None
                            st.rerun()
                else:
                    if st.button(tx("btn_select"), key=f"sel_{tid}", use_container_width=True):
                        st.session_state.selected_task = tid
                        st.rerun()

    if done_count >= 3:
        st.success(tx("tasks_all_done"))
        if st.button(tx("btn_see_iap"), use_container_width=True, type="primary", key="tasks_to_iap"):
            st.session_state.step = "iap"
            st.rerun()

    # Nav buttons
    st.markdown("---")
    nv1, nv2 = st.columns([1, 5])
    with nv1:
        if st.button("← Questionário", use_container_width=True, key="tasks_back"):
            st.session_state.step = "questionnaire"
            st.rerun()


# ─────────────────────────────────────────────
# STEP: IAP
# ─────────────────────────────────────────────
def step_iap():
    if not st.session_state.iap_score:
        base = 70 + (st.session_state.tasks_completed * 5)
        st.session_state.iap_score = min(random.randint(base, base + 15), 99)
        if DB_AVAILABLE and st.session_state.user_id and st.session_state.profile:
            db.save_profile(st.session_state.user_id, st.session_state.profile,
                            st.session_state.iap_score,
                            {str(k): v for k, v in st.session_state.answers.items()})

    score = st.session_state.iap_score
    init = random.randint(74, 94)
    exec_ = random.randint(78, 96)
    conc = random.randint(80, 98)

    st.markdown(f"<div class='section-label animate-in'>Resultado</div>", unsafe_allow_html=True)
    st.markdown(f"<h2 class='hero-headline animate-in'>{tx('iap_title')}</h2>", unsafe_allow_html=True)
    st.markdown("---")

    # Score ring
    _, ring_col, _ = st.columns([1, 1, 1])
    with ring_col:
        st.markdown(f"""
        <div style="text-align:center;margin:1.5rem 0;">
            <div class="stat-ring animate-in">{score}%</div>
            <div style="color:var(--accent);font-weight:600;margin-top:0.75rem;">{tx('iap_above')}</div>
        </div>
        """, unsafe_allow_html=True)

    # Detail metrics
    st.markdown(f"### 📈 {tx('iap_detail')}")
    mc1, mc2, mc3 = st.columns(3)
    with mc1:
        st.metric(tx("iap_initiative"), f"{init}%")
        st.progress(init/100)
    with mc2:
        st.metric(tx("iap_execution"), f"{exec_}%")
        st.progress(exec_/100)
    with mc3:
        st.metric(tx("iap_conclusion"), f"{conc}%")
        st.progress(conc/100)

    with st.expander(f"ℹ️ {tx('iap_what')}"):
        st.markdown(tx("iap_desc"))

    st.markdown("<br>", unsafe_allow_html=True)
    nc1, nc2 = st.columns([1, 4])
    with nc1:
        if st.button("← Tarefas", use_container_width=True, key="iap_back"):
            st.session_state.step = "tasks"
            st.rerun()
    with nc2:
        if st.button(tx("btn_see_profile"), use_container_width=True, type="primary", key="iap_next"):
            st.session_state.step = "profile"
            st.rerun()


# ─────────────────────────────────────────────
# STEP: PROFILE
# ─────────────────────────────────────────────
def step_profile():
    if not st.session_state.profile:
        st.session_state.profile = compute_profile()

    profile = st.session_state.profile
    pk = get_profile_key()
    lang_key = "en" if st.session_state.lang == "en" else "pt"
    # Map pt->pt, en->en profile keys
    en_pk_map = {"Executor":"Executor","Organizador":"Organizer","Criativo":"Creative"}
    info_key = en_pk_map.get(pk, pk) if lang_key == "en" else pk
    info = PROFILE_INFO[lang_key].get(info_key, PROFILE_INFO["pt"]["Executor"])

    st.markdown(f"<div class='section-label animate-in'>{tx('profile_title')}</div>", unsafe_allow_html=True)
    st.markdown(f"<h1 class='hero-headline animate-in'>{info['icon']} {profile.split(' ', 1)[-1]}</h1>", unsafe_allow_html=True)
    st.balloons()

    st.markdown(f"""
    <div class="eco-card animate-in delay-1" style="margin:1.5rem 0;">
        <p style="color:var(--text);font-size:1.05rem;line-height:1.8;font-style:italic;">
            "{info['desc']}"
        </p>
    </div>
    """, unsafe_allow_html=True)

    c1, c2 = st.columns(2)
    with c1:
        st.markdown(f"### {tx('profile_strengths')}")
        for s in info["strengths"]:
            st.markdown(f"""
            <div class="eco-card animate-in delay-1" style="margin-bottom:0.6rem;padding:0.9rem 1.1rem;border-left:3px solid var(--accent2);">
                {s}
            </div>
            """, unsafe_allow_html=True)
    with c2:
        st.markdown(f"### {tx('profile_tips')}")
        for i, tip in enumerate(info["tips"]):
            st.markdown(f"""
            <div class="eco-card animate-in delay-{i%3+1}" style="margin-bottom:0.6rem;padding:0.9rem 1.1rem;border-left:3px solid var(--accent);">
                <span style="color:var(--accent);font-weight:700;margin-right:0.5rem;">{i+1}.</span>{tip}
            </div>
            """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    nc1, nc2, nc3 = st.columns([1, 1, 2])
    with nc1:
        if st.button("← IAP", use_container_width=True, key="prof_back"):
            st.session_state.step = "iap"
            st.rerun()
    with nc2:
        if st.button("👤 Minha Página", use_container_width=True, key="prof_user"):
            st.session_state.step = "user_page"
            st.rerun()
    with nc3:
        if st.button(tx("btn_chat"), use_container_width=True, type="primary", key="prof_chat"):
            st.session_state.step = "chat"
            st.rerun()


# ─────────────────────────────────────────────
# STEP: CHAT
# ─────────────────────────────────────────────
def step_chat():
    pk = get_profile_key()
    score = st.session_state.iap_score or "N/A"

    st.markdown(f"<div class='section-label animate-in'>{tx('chat_title')}</div>", unsafe_allow_html=True)
    st.markdown(f"<h2 class='hero-headline animate-in' style='font-size:1.8rem;'>🤖 {tx('chat_title')}</h2>", unsafe_allow_html=True)
    st.markdown(f"""
    <div class="eco-pill animate-in" style="margin-bottom:1.5rem;">
        {tx('chat_context')} <strong>{st.session_state.profile}</strong> · IAP {score}%
    </div>
    """, unsafe_allow_html=True)

    # Show messages
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    # Input
    if prompt := st.chat_input(tx("chat_placeholder")):
        st.session_state.messages.append({"role": "user", "content": prompt})
        if DB_AVAILABLE and st.session_state.user_id:
            db.save_chat_message(st.session_state.user_id, "user", prompt)

        system = f"""Você é o assistente de produtividade EcoNexo. 
O usuário tem perfil {st.session_state.profile} e IAP de {score}%.
Responda em {st.session_state.lang}. Seja direto, prático e motivador. 
Máximo 4 parágrafos curtos. Use emojis com moderação."""

        if DB_AVAILABLE:
            history = [{"role": m["role"], "content": m["content"]} for m in st.session_state.messages]
            reply = db.call_ai(history, system_prompt=system, max_tokens=512)
        else:
            tips = {
                "Executor": ["Comece pela tarefa mais simples para ganhar momentum.", "Use timer de 25min — foco total, sem distração."],
                "Organizador": ["Crie um checklist antes de começar qualquer coisa.", "Bloqueie seu calendário para tarefas importantes."],
                "Criativo": ["Faça um brainstorm de 5min antes de decidir como agir.", "Experimente uma abordagem completamente diferente."],
            }
            tip = random.choice(tips.get(pk, ["Mantenha o foco no que importa."]))
            reply = f"💡 Para o perfil **{st.session_state.profile}**: {tip}\n\nSobre sua pergunta — *\"{prompt}\"* — a chave é agir de forma consistente, mesmo em pequenos passos diários."

        st.session_state.messages.append({"role": "assistant", "content": reply})
        if DB_AVAILABLE and st.session_state.user_id:
            db.save_chat_message(st.session_state.user_id, "assistant", reply)
        st.rerun()

    # Actions
    st.markdown("---")
    ac1, ac2, ac3 = st.columns(3)
    with ac1:
        if st.button(tx("btn_clear_chat"), use_container_width=True, key="chat_clear"):
            st.session_state.messages = []
            if DB_AVAILABLE and st.session_state.user_id:
                db.clear_chat_history(st.session_state.user_id)
            st.rerun()
    with ac2:
        if st.button(tx("btn_restart"), use_container_width=True, key="chat_restart"):
            clear_journey()
            st.rerun()
    with ac3:
        if st.button(tx("btn_see_profile_again"), use_container_width=True, key="chat_profile"):
            st.session_state.step = "profile"
            st.rerun()


# ─────────────────────────────────────────────
# STEP: USER PAGE (Persona)
# ─────────────────────────────────────────────
def step_user_page():
    pk = get_profile_key()
    lang_key = "en" if st.session_state.lang == "en" else "pt"
    en_pk_map = {"Executor":"Executor","Organizador":"Organizer","Criativo":"Creative"}
    info_key = en_pk_map.get(pk, pk) if lang_key == "en" else pk
    info = PROFILE_INFO[lang_key].get(info_key, PROFILE_INFO["pt"]["Executor"])
    score = st.session_state.iap_score or "—"

    st.markdown(f"<div class='section-label animate-in'>Conta</div>", unsafe_allow_html=True)
    st.markdown(f"<h2 class='hero-headline animate-in'>👤 {st.session_state.user_name}</h2>", unsafe_allow_html=True)
    st.markdown("---")

    # User card
    uc1, uc2 = st.columns([1.5, 1])
    with uc1:
        st.markdown(f"""
        <div class="eco-card animate-in">
            <div style="display:flex;align-items:center;gap:1.25rem;margin-bottom:1.5rem;">
                <div style="width:72px;height:72px;border-radius:50%;background:linear-gradient(135deg,{ACCENT},{ACCENT2});
                            display:flex;align-items:center;justify-content:center;font-size:2rem;font-family:'Syne',sans-serif;font-weight:800;color:#fff;">
                    {st.session_state.user_name[0].upper()}
                </div>
                <div>
                    <div style="font-family:'Syne',sans-serif;font-size:1.3rem;font-weight:700;">{st.session_state.user_name}</div>
                    <div style="color:var(--text2);font-size:0.88rem;">{st.session_state.user_email}</div>
                    <div style="margin-top:0.4rem;"><span class="eco-badge">{st.session_state.profile or 'Sem perfil'}</span></div>
                </div>
            </div>
            <div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:1rem;text-align:center;">
                <div>
                    <div style="font-family:'Syne',sans-serif;font-size:2rem;font-weight:800;color:var(--accent);">{score}%</div>
                    <div style="color:var(--text2);font-size:0.8rem;">IAP Score</div>
                </div>
                <div>
                    <div style="font-family:'Syne',sans-serif;font-size:2rem;font-weight:800;color:var(--accent2);">{st.session_state.tasks_completed}</div>
                    <div style="color:var(--text2);font-size:0.8rem;">Tarefas</div>
                </div>
                <div>
                    <div style="font-family:'Syne',sans-serif;font-size:2rem;font-weight:800;color:var(--accent);">{len(st.session_state.answers)}</div>
                    <div style="color:var(--text2);font-size:0.8rem;">Respostas</div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    with uc2:
        # Persona cards
        st.markdown("<h3>Personas Disponíveis</h3>", unsafe_allow_html=True)
        personas = [
            ("🎯","Executor","Executor","Ação rápida e resultados imediatos"),
            ("📋","Organizador","Organizer","Estrutura e processos claros"),
            ("💡","Criativo","Creative","Inovação e novas possibilidades"),
        ]
        for icon, name_pt, name_en, desc in personas:
            is_active = pk == name_pt or pk == name_en
            active_class = "persona-card active" if is_active else "persona-card"
            active_badge = '<span class="eco-badge" style="margin-top:0.5rem;display:inline-block;">Seu perfil ✓</span>' if is_active else ""
            st.markdown(f"""
            <div class="{active_class}" style="margin-bottom:0.75rem;">
                <div style="font-size:2rem;">{icon}</div>
                <strong style="font-family:'Syne',sans-serif;color:var(--text);">{name_pt}</strong>
                <p style="color:var(--text2);font-size:0.82rem;margin:0.25rem 0 0;">{desc}</p>
                {active_badge}
            </div>
            """, unsafe_allow_html=True)

    # Strengths & Tips from profile
    if st.session_state.profile:
        st.markdown("---")
        st.markdown(f"### 💪 Forças & Dicas — Perfil {st.session_state.profile}")
        pc1, pc2 = st.columns(2)
        with pc1:
            for s in info["strengths"]:
                st.success(s)
        with pc2:
            for tip in info["tips"]:
                st.info(tip)

    # Task history
    if DB_AVAILABLE and st.session_state.user_id:
        history = db.get_task_history(st.session_state.user_id)
        if history:
            st.markdown("---")
            st.markdown("### 📜 Histórico de Tarefas")
            for h in history[:10]:
                st.markdown(f"""
                <div class="task-item done" style="display:flex;justify-content:space-between;padding:0.7rem 1rem;">
                    <span>✅ {h['task_name']}</span>
                    <span style="color:var(--text2);font-size:0.82rem;">{h['completed_at'][:16]}</span>
                </div>
                """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    nav1, nav2 = st.columns([1, 5])
    with nav1:
        if st.button("← Voltar", use_container_width=True, key="user_back"):
            st.session_state.step = "profile" if st.session_state.profile else "questionnaire"
            st.rerun()


# ─────────────────────────────────────────────
# STEP: SETTINGS
# ─────────────────────────────────────────────
def step_settings():
    st.markdown(f"<div class='section-label animate-in'>Conta</div>", unsafe_allow_html=True)
    st.markdown(f"<h2 class='hero-headline animate-in'>⚙️ {tx('settings_title')}</h2>", unsafe_allow_html=True)
    st.markdown("---")

    sc1, sc2 = st.columns(2)

    with sc1:
        st.markdown("### 🎨 Aparência")
        theme_opt = st.radio(
            tx("settings_theme"),
            [tx("settings_theme_light"), tx("settings_theme_dark")],
            index=1 if IS_DARK else 0,
            horizontal=True,
            key="sett_theme_radio",
        )

        font_opt = st.radio(
            tx("settings_font"),
            [tx("settings_font_sm"), tx("settings_font_md"), tx("settings_font_lg")],
            index=["sm","md","lg"].index(st.session_state.font_size),
            horizontal=True,
            key="sett_font_radio",
        )

        lang_opt = st.radio(
            tx("settings_lang"),
            ["🇧🇷 Português", "🇺🇸 English"],
            index=0 if st.session_state.lang == "pt" else 1,
            horizontal=True,
            key="sett_lang_radio",
        )

    with sc2:
        st.markdown("### 🔑 Conta")
        new_name = st.text_input("Nome de exibição", value=st.session_state.user_name)
        st.text_input("E-mail", value=st.session_state.user_email, disabled=True)

        st.markdown("### 🗑️ Dados")
        if st.button("🗑️ Limpar histórico de chat", use_container_width=True, key="sett_clear_chat"):
            st.session_state.messages = []
            if DB_AVAILABLE and st.session_state.user_id:
                db.clear_chat_history(st.session_state.user_id)
            st.success("Chat limpo!")

        if st.button("🔄 Reiniciar jornada", use_container_width=True, key="sett_restart"):
            clear_journey()
            st.success("Jornada reiniciada!")
            st.rerun()

    st.markdown("<br>", unsafe_allow_html=True)
    sv1, sv2 = st.columns([1, 5])
    with sv1:
        if st.button(tx("btn_save_settings"), use_container_width=True, type="primary", key="sett_save"):
            # Apply theme
            new_theme = "dark" if tx("settings_theme_dark") in theme_opt else "light"
            # Apply font
            font_map = {
                tx("settings_font_sm"): "sm",
                tx("settings_font_md"): "md",
                tx("settings_font_lg"): "lg",
            }
            new_font = font_map.get(font_opt, "md")
            new_lang = "en" if "English" in lang_opt else "pt"
            if new_name:
                st.session_state.user_name = new_name

            st.session_state.theme = new_theme
            st.session_state.font_size = new_font
            st.session_state.lang = new_lang

            if DB_AVAILABLE and st.session_state.user_id:
                db.update_user_prefs(st.session_state.user_id, new_theme, new_font, new_lang)

            st.success(tx("settings_saved"))
            st.rerun()
    with sv2:
        if st.button("← Voltar", use_container_width=True, key="sett_back"):
            st.session_state.step = "user_page"
            st.rerun()


# ─────────────────────────────────────────────
# MAIN ROUTER
# ─────────────────────────────────────────────
PAGE_MAP = {
    "landing":  page_landing,
    "features": page_features,
    "login":    page_login,
    "about":    page_about,
    "lgpd":     page_lgpd,
    "contact":  page_contact,
}

if not st.session_state.logged_in:
    PAGE_MAP.get(st.session_state.page, page_landing)()
else:
    show_app()
