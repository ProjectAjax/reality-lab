import streamlit as st
import time

# 1. High-Contrast Theme Configuration
st.set_page_config(page_title="The Truth Lab", page_icon="⚖️")

# Custom CSS targeting the "White Box" problem specifically
st.markdown("""
    <style>
    /* Force main background */
    .stApp { background-color: #000000 !important; }
    
    /* Neon Green Labels */
    label p { color: #00FF00 !important; font-size: 1.2rem !important; font-weight: bold !important; }
    
    /* White Text for everything else */
    h1, h2, h3, p, span, div, li { color: #FFFFFF !important; }

    /* --- THE FIX FOR WHITE BOXES --- */
    /* Targets the Selectbox container */
    div[data-baseweb="select"] > div {
        background-color: #1A1A1A !important;
        color: #FFFFFF !important;
        border: 2px solid #00FF00 !important;
    }

    /* Targets the actual text inside the collapsed selectbox */
    div[data-testid="stSelectbox"] div[role="button"] {
        color: #FFFFFF !important;
        background-color: #1A1A1A !important;
    }

    /* Targets the dropdown menu when it opens */
    div[data-baseweb="popover"] ul {
        background-color: #1A1A1A !important;
        border: 2px solid #00FF00 !important;
    }

    /* Targets individual items in the dropdown list */
    div[data-baseweb="popover"] li {
        background-color: #1A1A1A !important;
        color: #FFFFFF !important;
    }

    /* Highlight color when hovering over list items */
    div[data-baseweb="popover"] li:hover {
        background-color: #00FF00 !important;
        color: #000000 !important;
    }

    /* Text areas and inputs */
    textarea, input {
        background-color: #1A1A1A !important;
        color: #FFFFFF !important;
        border: 2px solid #00FF00 !important;
    }

    /* Buttons */
    .stButton>button {
        width: 100%;
        background-color: #00FF00 !important;
        color: #000000 !important;
        font-weight: bold !important;
        border: none;
        height: 3em;
    }
    
    /* Sidebar */
    section[data-testid="stSidebar"] { background-color: #111111 !important; }
    </style>
    """, unsafe_allow_html=True)

# --- DATA & STATE ---
unhelpful_thoughts = [
    "I can't get a job", "I can't express myself", "People think I am a fool",
    "I am useless", "I am hopeless", "I am horrible", "I am a failure",
    "I am ugly", "I am stupid", "I am a disappointment", "I am worthless",
    "I am ridiculous", "People are judging me", "My kids hate me",
    "I am heartless", "I will always fail", "I am irritating"
]

if 'step' not in st.session_state:
    st.session_state.step = 1

# --- NAVIGATION ---
menu = st.sidebar.radio("CHOOSE TOOL:", ["The Truth Drill", "Avoidance Buster (Exposure)", "My Adult Evidence"])

if st.sidebar.button("🚨 PANIC: I'M SPIRALING"):
    st.session_state.step = "panic"

# --- TOOL 1: THE TRUTH DRILL ---
if menu == "The Truth Drill" and st.session_state.step != "panic":
    st.title("⚖️ THE TRUTH DRILL")
    
    if st.session_state.step == 1:
        thought = st.selectbox("What is the surface thought?", ["Select a thought..."] + unhelpful_thoughts)
        feeling = st.text_input("What is the feeling? (Shame, Fear, etc.)")
        belief = st.text_input("What does your brain claim this says about you?")
        
        if st.button("Drill Down →") and thought != "Select a thought...":
            st.session_state.thought = thought
            st.session_state.feeling = feeling
            st.session_state.belief = belief
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
        st.write(f"Because of a childhood riddled with insecure and cruel comments, your brain tries to convince you that you are '{st.session_state.belief}'.")
        
        st.success("### THE ADULT REALITY")
        st.markdown(f"""
        **In spite of that troubled upbringing, the truth is:**
        * **You have a family** who is in your life today.
        * **You earned qualifications** despite your education history.
        * **You have friends** who care about you.
        * **Conclusion:** You are a survivor of your past, not a victim of your thoughts.
        """)
        if st.button("Reset Drill"):
            st.session_state.step = 1
            st.rerun()

# --- TOOL 2: AVOIDANCE BUSTER ---
elif menu == "Avoidance Buster (Exposure)":
    st.title("🛡️ AVOIDANCE BUSTER")
    task = st.text_input("What task are you avoiding right now?")
    
    if task:
        st.subheader("The Reality of Avoiding")
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("⚠️ **AVOIDING**")
            st.write("Failure is 100% guaranteed. The voices win.")
        with col2:
            st.markdown("✅ **DOING IT (BADLY)**")
            st.write("Failure is only a possibility. You prove the voices wrong just by moving.")

        if st.button("Start 5-Minute Action Timer"):
            placeholder = st.empty()
            for t in range(300, 0, -1):
                mins, secs = divmod(t, 60)
                placeholder.metric("Move! Time Left:", f"{mins:02d}:{secs:02d}")
                time.sleep(1)
            st.success("Rep Complete. You defied the script.")

# --- TOOL 3: EVIDENCE LOG ---
elif menu == "My Adult Evidence":
    st.title("📖 THE EVIDENCE LOG")
    new_win = st.text_area("Record a moment where you were NOT the old script:")
    if st.button("Log Win"):
        st.toast("Evidence Recorded.")

# --- PANIC MODE ---
if st.session_state.step == "panic":
    st.title("🚨 REALITY CHECK")
    st.warning("You are in a spiral. Your brain is using a 20-year-old map to navigate today.")
    st.write("### THE FACTS:")
    st.write("1. You have a family.")
    st.write("2. You have qualifications.")
    st.write("3. You are a different person than the one your parents described.")
    if st.button("I'm back. Resume."):
        st.session_state.step = 1
        st.rerun()
