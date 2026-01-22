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

# --- INITIALIZE SESSION STATE ---
if 'step' not in st.session_state:
    st.session_state.step = 1
if 'evidence_logs' not in st.session_state:
    st.session_state.evidence_logs = ["I have a family.", "I earned qualifications.", "I have friends who care."]
if 'goals' not in st.session_state:
    st.session_state.goals = []

unhelpful_thoughts = [
    "I can't get a job", "I can't express myself", "People think I am a fool", "I am useless", 
    "I am hopeless", "I am horrible", "I am a failure", "I am ugly", "I am stupid", 
    "I am a disappointment", "I am not worth knowing", "I am worthless", "I am ridiculous", 
    "I am fucked", "People are looking at my oily nose", "People are judging me", 
    "People feel sorry for me", "People feel disappointed in me", "My kids hate me", 
    "I have hurt my kids from not working", "I am heartless", "I am irritating", "I will always fail"
]

# --- NAVIGATION ---
menu = st.sidebar.radio("CHOOSE TOOL:", ["The Truth Drill", "Setback Recovery", "The Standard Shifter", "Evidence & Goals"])

if st.sidebar.button("🚨 PANIC: I'M SPIRALING"):
    st.session_state.step = "panic"

# --- TOOL 1: THE TRUTH DRILL ---
if menu == "The Truth Drill" and st.session_state.step != "panic":
    st.title("⚖️ THE TRUTH DRILL")
    
    if st.session_state.step == 1:
        thought = st.selectbox("What is the surface thought?", ["Select a thought..."] + unhelpful_thoughts)
        belief = st.text_input("What does your brain claim this says about you?")
        if st.button("Drill Down →") and thought != "Select a thought...":
            st.session_state.thought, st.session_state.belief = thought, belief
            st.session_state.step = 2
            st.rerun()

    elif st.session_state.step == 2:
        st.subheader("Challenging the Identity")
        q1 = st.text_area(f"1. Describe what '{st.session_state.belief}' means like you were telling a friend.")
        q2 = st.text_input(f"2. By whose definition are you '{st.session_state.belief}'?")
        q3 = st.text_input("3. Considering your upbringing, describe the SITUATION (not you) without bias:")
        if st.button("The Final Verdict →"):
            st.session_state.bias_free = q3
            st.session_state.step = 3
            st.rerun()

    elif st.session_state.step == 3:
        st.error("### THE PARENTAL SCRIPT")
        st.write(f"The belief '{st.session_state.belief}' is a legacy standard from your upbringing. It is not an adult fact.")
        st.success("### THE ADULT REALITY")
        st.write(f"**Objective Situation:** {st.session_state.bias_free}")
        st.write("**The Adult Truths:**")
        for item in st.session_state.evidence_logs:
            st.write(f"✅ {item}")
        if st.button("Reset Drill"):
            st.session_state.step = 1
            st.rerun()

# --- TOOL 2: SETBACK RECOVERY (SO WHAT?) ---
elif menu == "Setback Recovery":
    st.title("🔄 SETBACK RECOVERY")
    event = st.text_input("What went wrong?")
    if event:
        st.write("### THE 'SO WHAT?' DRILL")
        s1 = st.text_input(f"If it's true that {event}, so what? What does that mean?")
        s2 = st.text_input("And if that happens, so what?")
        s3 = st.selectbox("Which core belief is this trying to trigger?", unhelpful_thoughts)
        
        if s1 and s2 and s3:
            st.warning(f"**REALITY CHECK:** Your brain is using a mistake to prove you are '{s3}'.")
            st.info(f"Considering your childhood, is it possible you are just a human making a mistake, and the 'Failure' label is just an old voice?")
            if st.button("Is that really you?"):
                st.write("### NO. IT IS NOT.")
                st.write("You are a 54-year-old adult who survived. This setback is data, not a death sentence.")

# --- TOOL 3: THE STANDARD SHIFTER ---
elif menu == "The Standard Shifter":
    st.title("📏 THE STANDARD SHIFTER")
    st.write("Let's separate their rules from yours.")
    
    col1, col2 = st.columns(2)
    with col1:
        st.header("Legacy Standard")
        st.write("(What they told you)")
        st.write("1. Success is perfect.")
        st.write("2. Mistakes are shameful.")
        st.write("3. Worth is based on work.")
    
    with col2:
        st.header("My Adult Standard")
        st.write("(What YOU decide now)")
        goal = st.text_input("By MY definition, a 'good day' is:")
        worth = st.text_input("By MY definition, my worth is based on:")
    
    if st.button("Adopt My Standards"):
        st.success("New standards saved. You are the judge now.")

# --- TOOL 4: EVIDENCE & GOALS ---
elif menu == "Evidence & Goals":
    st.title("📖 REALITY & FUTURE")
    st.header("1. Evidence Log")
    new_win = st.text_input("Record an adult win:")
    if st.button("Save Win") and new_win:
        st.session_state.evidence_logs.append(new_win)
        st.toast("Evidence Recorded.")
    
    st.write("---")
    st.header("2. Tomorrow's Goals (Min 3)")
    g1 = st.text_input("Goal 1:")
    g2 = st.text_input("Goal 2:")
    g3 = st.text_input("Goal 3:")
    if st.button("Lock in Goals"):
        if g1 and g2 and g3:
            st.session_state.goals = [g1, g2, g3]
            st.success("Goals locked.")
        else:
            st.error("Please enter at least 3 goals.")

# --- PANIC MODE ---
if st.session_state.step == "panic":
    st.title("🚨 REALITY CHECK")
    st.write("### THE FACTS:")
    for item in st.session_state.evidence_logs:
        st.write(f"✅ {item}")
    if st.button("Resume"):
        st.session_state.step = 1
        st.rerun()
