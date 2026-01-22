import streamlit as st
import time

# 1. High-Contrast Theme Configuration
st.set_page_config(page_title="The Truth Lab", page_icon="⚖️")

# Custom CSS for readability, ADHD focus, and Fixing the White Boxes
st.markdown("""
    <style>
    /* Force background to black */
    .stApp { background-color: #000000; }
    
    /* Labels (The questions) - Neon Green */
    label p { color: #00FF00 !important; font-size: 1.2rem !important; font-weight: bold !important; }
    
    /* Main text and headers - White */
    h1, h2, h3, p, span, div { color: #FFFFFF !important; }
    
    /* FIX: Input Boxes and Selectbox Containers */
    div[data-baseweb="select"] > div, 
    div[data-baseweb="base-input"] > textarea, 
    div[data-baseweb="base-input"] > input {
        background-color: #1A1A1A !important;
        color: #FFFFFF !important;
        border: 2px solid #00FF00 !important;
    }

    /* FIX: The dropdown list itself (the popover) */
    ul[role="listbox"] {
        background-color: #1A1A1A !important;
        color: #FFFFFF !important;
        border: 1px solid #00FF00 !important;
    }
    
    /* Buttons - Neon High Contrast */
    .stButton>button {
        width: 100%;
        background-color: #00FF00 !important;
        color: #000000 !important;
        font-weight: bold !important;
        border-radius: 5px;
        height: 3em;
        border: none;
    }

    /* Sidebar styling */
    section[data-testid="stSidebar"] { background-color: #111111 !important; }
    </style>
    """, unsafe_allow_html=True)

# --- APP LOGIC & STATE ---
if 'step' not in st.session_state:
    st.session_state.step = 1

unhelpful_thoughts = [
    "I can't get a job", "I can't express myself", "People think I am a fool",
    "I am useless", "I am hopeless", "I am horrible", "I am a failure",
    "I am ugly", "I am stupid", "I am a disappointment", "I am worthless",
    "I am ridiculous", "People are judging me", "My kids hate me",
    "I am heartless", "I will always fail", "I am irritating"
]

# --- SIDEBAR NAVIGATION ---
st.sidebar.title("🎛️ CONTROL PANEL")
menu = st.sidebar.radio("CHOOSE TOOL:", ["The Truth Drill", "Avoidance Buster (Exposure)", "My Adult Evidence"])

# --- TOOL 1: THE TRUTH DRILL ---
if menu == "The Truth Drill":
    st.title("⚖️ THE TRUTH DRILL")
    
    if st.session_state.step == 1:
        thought = st.selectbox("What is the surface thought?", [""] + unhelpful_thoughts)
        feeling = st.text_input("What is the feeling? (Shame, Fear, etc.)")
        belief = st.text_input("What does your brain claim this says about you?")
        
        if st.button("Drill Down →") and thought != "":
            st.session_state.thought = thought
            st.session_state.feeling = feeling
            st.session_state.belief = belief
            st.session_state.step = 2
            st.rerun()

    elif st.session_state.step == 2:
        st.write(f"**Target Belief:** {st.session_state.belief}")
        w1 = st.text_input(f"Why does it matter if you are {st.session_state.belief}?")
        w2 = st.text_input("And why does THAT matter?")
        w3 = st.text_input("What is the childhood root of this comment?")

        if st.button("Pivot to Reality →"):
            st.session_state.w3 = w3
            st.session_state.step = 3
            st.rerun()

    elif st.session_state.step == 3:
        st.error("### THE CHILDHOOD SCRIPT")
        st.write(f"Because of a childhood riddled with insecure and cruel comments, your brain is lying to you. It tries to prove you are '{st.session_state.belief}' using the thought '{st.session_state.thought}'.")
        
        st.success("### THE ADULT REALITY")
        st.markdown(f"""
        **In spite of that troubled upbringing, the truth is:**
        * You have a family who loves you.
        * You earned qualifications despite your education history.
        * You have friends who care about you.
        * **Conclusion:** You are a survivor, not the script your parents wrote.
        """)
        if st.button("Reset Drill"):
            st.session_state.step = 1
            st.rerun()

# --- TOOL 2: AVOIDANCE BUSTER (EXPOSURE) ---
elif menu == "Avoidance Buster (Exposure)":
    st.title("🛡️ AVOIDANCE BUSTER")
    task = st.text_input("What task are you avoiding right now?")
    
    if task:
        st.subheader("The Exposure Math")
        col1, col2 = st.columns(2)
        with col1:
            st.write("**IF YOU AVOID:**")
            st.write("❌ Guaranteed Failure")
            st.write("❌ Shame gets louder")
        with col2:
            st.write("**IF YOU TRY (Even Badly):**")
            st.write("✅ 50% Success Chance")
            st.write("✅ Fear loses its grip")

        if st.button("Start 5-Minute Action Timer"):
            st.warning(f"ACTION: Go do '{task}' now. Don't think. Don't aim for perfect. Just move.")
            placeholder = st.empty()
            for t in range(300, 0, -1):
                mins, secs = divmod(t, 60)
                placeholder.metric("Time Remaining", f"{mins:02d}:{secs:02d}")
                time.sleep(1)
            st.success("TIME UP. Rep complete. You beat the avoidance.")

# --- TOOL 3: EVIDENCE LOG ---
elif menu == "My Adult Evidence":
    st.title("📖 THE EVIDENCE LOG")
    st.write("Record your adult wins to override the old scripts.")
    
    new_evidence = st.text_area("Record a win (e.g., 'Completed a work task', 'Spoke up for myself'):")
    if st.button("Save Win"):
        st.toast("Win logged. This is your new reality.")
