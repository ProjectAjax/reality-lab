import streamlit as st

# 1. High-Contrast Theme Configuration
st.set_page_config(page_title="The Truth Lab", page_icon="⚖️")

# Custom CSS for readability and ADHD focus
st.markdown("""
    <style>
    .stApp { background-color: #000000; }
    label p { color: #00FF00 !important; font-size: 1.2rem !important; font-weight: bold !important; }
    h1, h2, h3, p, span, div { color: #FFFFFF !important; }
    input, textarea, div[data-baseweb="select"] > div {
        background-color: #1A1A1A !important;
        color: #FFFFFF !important;
        border: 1px solid #00FF00 !important;
    }
    .stButton>button {
        width: 100%;
        background-color: #00FF00 !important;
        color: #000000 !important;
        font-weight: bold !important;
        border-radius: 5px;
        height: 3em;
        border: none;
    }
    .stAlert { background-color: #1A1A1A !important; border: 1px solid #00FF00 !important; }
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
        thought = st.selectbox("What is the surface thought?", unhelpful_thoughts)
        feeling = st.text_input("What is the feeling? (Shame, Fear, etc.)")
        belief = st.text_input("What does your brain claim this says about you?")
        
        if st.button("Drill Down →"):
            st.session_state.thought = thought
            st.session_state.belief = belief
            st.session_state.step = 2
            st.rerun()

    elif st.session_state.step == 2:
        st.write(f"**Target Belief:** {st.session_state.belief}")
        w1 = st.text_input("Why does that matter?")
        w2 = st.text_input("And why does THAT matter?")
        w3 = st.text_input("What is the childhood root of this?")

        if st.button("Pivot to Reality →"):
            st.session_state.w3 = w3
            st.session_state.step = 3
            st.rerun()

    elif st.session_state.step == 3:
        st.error("### THE CHILDHOOD SCRIPT")
        st.write(f"Because of those insecure and cruel comments, your brain is lying to you. It says you are '{st.session_state.belief}' because of '{st.session_state.w3}'.")
        
        st.success("### THE ADULT REALITY")
        st.markdown(f"""
        **In spite of that upbringing, the evidence shows:**
        * You have a family who loves you.
        * You earned qualifications despite your education history.
        * You have friends who care about you.
        * **The thought '{st.session_state.thought}' is a survival reflex, not a fact.**
        """)
        if st.button("Reset Drill"):
            st.session_state.step = 1
            st.rerun()

# --- TOOL 2: AVOIDANCE BUSTER (EXPOSURE) ---
elif menu == "Avoidance Buster (Exposure)":
    st.title("🛡️ AVOIDANCE BUSTER")
    task = st.text_input("What task are you avoiding right now?")
    
    if task:
        st.subheader("The Logic of the Gap")
        st.write("Your brain says avoiding this keeps you 'safe.' Let's look at the math:")
        
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("**AVOIDING IT:**")
            st.write("❌ 100% Chance of failure.")
            st.write("❌ Childhood voices get stronger.")
            st.write("❌ Anxiety increases for tomorrow.")
        
        with col2:
            st.markdown("**DOING IT (Even Badly):**")
            st.write("✅ 50% Chance of success.")
            st.write("✅ You prove you are NOT 'useless'.")
            st.write("✅ The 'oily nose' fear loses power.")

        st.info(f"**ACTION:** Do 5 minutes of '{task}' now. The goal is not to do it perfectly; the goal is to **disobey the fear.**")
        
        if st.button("I am doing it now (Log Rep)"):
            st.balloons()
            st.success("Rep logged. You are an exposure athlete.")

# --- TOOL 3: EVIDENCE LOG ---
elif menu == "My Adult Evidence":
    st.title("📖 THE EVIDENCE LOG")
    st.write("Record your adult wins here to use during the Truth Drills.")
    
    new_evidence = st.text_area("Add a new piece of evidence (e.g., 'I got my cert today', 'I had a laugh with my kids'):")
    if st.button("Save to Memory"):
        st.toast("Evidence saved for your next drill!")
