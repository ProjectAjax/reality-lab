import streamlit as st
import time

# 1. High-Contrast Theme Configuration
st.set_page_config(page_title="The Truth Lab", page_icon="⚖️")

# --- CSS FOR HIGH CONTRAST & VISIBILITY ---
st.markdown("""
    <style>
    .stApp { background-color: #000000 !important; }
    label p { color: #00FF00 !important; font-size: 1.2rem !important; font-weight: bold !important; }
    h1, h2, h3, p, span, div, li { color: #FFFFFF !important; }
    div[data-baseweb="select"] > div, div[data-testid="stSelectbox"] div[role="button"] {
        background-color: #1A1A1A !important; color: #FFFFFF !important; border: 2px solid #00FF00 !important;
    }
    div[data-baseweb="popover"] ul { background-color: #1A1A1A !important; border: 2px solid #00FF00 !important; }
    div[data-baseweb="popover"] li { background-color: #1A1A1A !important; color: #FFFFFF !important; }
    div[data-baseweb="popover"] li:hover { background-color: #00FF00 !important; color: #000000 !important; }
    textarea, input { background-color: #1A1A1A !important; color: #FFFFFF !important; border: 2px solid #00FF00 !important; }
    .stButton>button { width: 100%; background-color: #00FF00 !important; color: #000000 !important; font-weight: bold !important; border: none; height: 3em; }
    section[data-testid="stSidebar"] { background-color: #111111 !important; }
    </style>
    """, unsafe_allow_html=True)

# --- INITIALIZE SESSION STATE (The Memory) ---
if 'step' not in st.session_state:
    st.session_state.step = 1
if 'evidence_logs' not in st.session_state:
    # Starting with your core truths
    st.session_state.evidence_logs = ["I have a family.", "I earned qualifications.", "I have friends who care."]
if 'exposure_task_done' not in st.session_state:
    st.session_state.exposure_task_done = False

unhelpful_thoughts = [
    "I can't get a job", "I can't express myself", "People think I am a fool",
    "I am useless", "I am hopeless", "I am horrible", "I am a failure",
    "I am ugly", "I am stupid", "I am a disappointment", "I am worthless",
    "I am ridiculous", "People are judging me", "My kids hate me",
    "I am heartless", "I will always fail", "I am irritating"
]

# --- NAVIGATION ---
menu = st.sidebar.radio("CHOOSE TOOL:", ["The Truth Drill", "Avoidance Buster (Exposure)", "My Adult Evidence"])

if st.sidebar.button("🚨 PANIC: I'M SPIRALING"):
    st.session_state.step = "panic"

# --- TOOL 1: THE TRUTH DRILL ---
if menu == "The Truth Drill" and st.session_state.step != "panic":
    st.title("⚖️ THE TRUTH DRILL")
    
    if st.session_state.step == 1:
        thought = st.selectbox("What is the surface thought?", ["Select a thought..."] + unhelpful_thoughts)
        feeling = st.text_input("What is the feeling?")
        belief = st.text_input("What does your brain claim this says about you?")
        if st.button("Drill Down →") and thought != "Select a thought...":
            st.session_state.thought, st.session_state.feeling, st.session_state.belief = thought, feeling, belief
            st.session_state.step = 2
            st.rerun()

    elif st.session_state.step == 2:
        st.write(f"**Target Belief:** {st.session_state.belief}")
        w1 = st.text_input(f"Why does it matter if you are '{st.session_state.belief}'?")
        w2 = st.text_input("And why does THAT matter?")
        w3 = st.text_input("What is the childhood root of this comment?")
        if st.button("Pivot to Reality →"):
            st.session_state.w3 = w3
            st.session_state.step = 3
            st.rerun()

    elif st.session_state.step == 3:
        st.error("### THE CHILDHOOD SCRIPT")
        st.write(f"Your brain is using an old, cruel script to say you are '{st.session_state.belief}'.")
        st.success("### THE ADULT REALITY")
        # Pulls from the Evidence Log automatically
        for item in st.session_state.evidence_logs:
            st.write(f"✅ {item}")
        if st.button("Reset Drill"):
            st.session_state.step = 1
            st.rerun()

# --- TOOL 2: AVOIDANCE BUSTER ---
elif menu == "Avoidance Buster (Exposure)":
    st.title("🛡️ AVOIDANCE BUSTER")
    
    if not st.session_state.exposure_task_done:
        task = st.text_input("What task are you avoiding?")
        if task:
            st.write("✅ **DOING IT (BADLY)** = You prove the voices wrong just by moving.")
            if st.button("Start 5-Minute Action Timer"):
                placeholder = st.empty()
                for t in range(300, 0, -1):
                    m, s = divmod(t, 60)
                    placeholder.metric("Move! Time Left:", f"{m:02d}:{s:02d}")
                    time.sleep(1)
                st.session_state.exposure_task_done = True
                st.rerun()
    else:
        st.success("REP COMPLETE. You defied the script.")
        if st.button("Reset to Start New Task"):
            st.session_state.exposure_task_done = False
            st.rerun()

# --- TOOL 3: EVIDENCE LOG ---
elif menu == "My Adult Evidence":
    st.title("📖 THE EVIDENCE LOG")
    new_win = st.text_area("Record a moment where you were NOT the old script:")
    if st.button("Save Win to Reality"):
        if new_win:
            st.session_state.evidence_logs.append(new_win)
            st.toast("Evidence Recorded Permanently for this session.")
    
    st.write("### CURRENT REALITY BANK:")
    for i, log in enumerate(st.session_state.evidence_logs):
        st.write(f"{i+1}. {log}")

# --- PANIC MODE ---
if st.session_state.step == "panic":
    st.title("🚨 REALITY CHECK")
    st.write("### THE FACTS:")
    for item in st.session_state.evidence_logs:
        st.write(f"✅ {item}")
    if st.button("I'm back. Resume."):
        st.session_state.step = 1
        st.rerun()
