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
    /* Style for the slider label */
    .stSlider label p { color: #00FF00 !important; }
    </style>
    """, unsafe_allow_html=True)

# --- INITIALIZE SESSION STATE ---
if 'step' not in st.session_state:
    st.session_state.step = 1
if 'evidence_logs' not in st.session_state:
    st.session_state.evidence_logs = ["I have a family.", "I earned qualifications.", "I have friends who care."]
if 'goal_history' not in st.session_state:
    st.session_state.goal_history = []
if 'meditation_reps' not in st.session_state:
    st.session_state.meditation_reps = 0

unhelpful_thoughts = [
    "I can't get a job", "I can't express myself", "People think I am a fool", "I am useless", 
    "I am hopeless", "I am horrible", "I am a failure", "I am ugly", "I am stupid", 
    "I am a disappointment", "I am not worth knowing", "I am worthless", "I am ridiculous", 
    "I am fucked", "People are looking at my oily nose", "People are judging me", 
    "People feel sorry for me", "People feel disappointed in me", "My kids hate me", 
    "I have hurt my kids from not working", "I am heartless", "I am irritating", "I will always fail"
]

# --- NAVIGATION ---
menu = st.sidebar.radio("CHOOSE TOOL:", ["The Truth Drill", "Setback Recovery", "Meditation Lab", "The Standard Shifter", "Evidence & Goals", "Goal History"])

if st.sidebar.button("🚨 PANIC: I'M SPIRALING"):
    st.session_state.step = "panic"

# --- TOOL 1: THE TRUTH DRILL (VALIDATION UPDATE) ---
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
        st.subheader("Contextual Reality Check")
        q1 = st.text_area(f"1. Describe what '{st.session_state.belief}' looks like considering the ups and downs of life.")
        q2 = st.text_input(f"2. By whose definition are you '{st.session_state.belief}'?")
        q3 = st.text_area("3. Neutral Observation: Describe the situation without the cruel labels.")
        
        st.write("---")
        st.subheader("Reality Validation")
        truth_rating = st.slider(f"How true is the belief '{st.session_state.belief}' in this specific context?", 1, 10, 5)
        reasoning = st.selectbox("What does this rating reveal?", [
            "Select an insight...",
            "This makes me human, not a failure.",
            "My bias is probably distorting the truth here.",
            "I can always get better; this isn't a permanent state.",
            "This shows how false this belief actually is.",
            "This is a legacy script from my past, not my present reality."
        ])
        
        if st.button("The Final Verdict →") and reasoning != "Select an insight...":
            st.session_state.neutral_view = q3
            st.session_state.truth_rating = truth_rating
            st.session_state.reasoning = reasoning
            st.session_state.step = 3
            st.rerun()

    elif st.session_state.step == 3:
        st.error("### THE PARENTAL SCRIPT")
        st.write(f"The label '{st.session_state.belief}' was rated by you as a **{st.session_state.truth_rating}/10**. You recognized that: **{st.session_state.reasoning}**")
        
        st.success("### THE ADULT REALITY")
        st.info(f"**Neutral Observation:** {st.session_state.neutral_view}")
        st.write("**The Untouchable Truths:**")
        for item in st.session_state.evidence_logs:
            st.write(f"✅ {item}")
        
        if st.button("Reset Drill"):
            st.session_state.step = 1
            st.rerun()

# --- TOOL 2: SETBACK RECOVERY ---
elif menu == "Setback Recovery":
    st.title("🔄 SETBACK RECOVERY")
    event = st.text_input("What went wrong?")
    if event:
        s1 = st.text_input(f"If it's true that '{event}', so what? What is the worst-case result?")
        s2 = st.text_input("Why does your brain say this means you are fundamentally broken?")
        s3 = st.selectbox("Which core belief is this triggering?", unhelpful_thoughts)
        if s1 and s2 and s3:
            st.warning(f"**IS THAT REALLY YOU?** Your brain is using a human mistake to fuel the '{s3}' script.")
            st.write("This mistake is just data. It doesn't overwrite your qualifications or your family.")

# --- TOOL 3: MEDITATION LAB ---
elif menu == "Meditation Lab":
    st.title("🧘 MEDITATION LAB")
    st.write("Ground yourself in your 54-year-old body. It is 2026. You are safe.")
    duration = st.slider("Set session length (minutes):", 1, 20, 5)
    if st.button("Start Meditation"):
        placeholder = st.empty()
        for t in range(duration * 60, 0, -1):
            m, s = divmod(t, 60)
            placeholder.metric("Present Moment Remaining:", f"{m:02d}:{s:02d}")
            time.sleep(1)
        st.success("Session complete.")
        st.session_state.meditation_reps += 1

# --- TOOL 4: THE STANDARD SHIFTER ---
elif menu == "The Standard Shifter":
    st.title("📏 THE STANDARD SHIFTER")
    col1, col2 = st.columns(2)
    with col1:
        st.header("Legacy Standard")
        st.write("❌ Worth = Paycheck")
    with col2:
        st.header("My Adult Standard")
        new_success = st.text_input("I define 'Success' as:")
    if st.button("Update Standards"):
        st.success("Standards updated.")

# --- TOOL 5: EVIDENCE & GOALS ---
elif menu == "Evidence & Goals":
    st.title("📖 REALITY & FUTURE")
    new_win = st.text_input("Record an adult win:")
    if st.button("Save Win") and new_win:
        st.session_state.evidence_logs.append(new_win)
    st.write("---")
    st.header("Tomorrow's Goals (Min 3)")
    g1, g2, g3 = st.text_input("Goal 1:"), st.text_input("Goal 2:"), st.text_input("Goal 3:")
    if st.button("Lock in Goals"):
        if g1 and g2 and g3:
            st.session_state.goal_history.append({"date": time.strftime("%Y-%m-%d"), "goals": [g1, g2, g3]})
            st.success("Goals locked.")

# --- TOOL 6: GOAL HISTORY ---
elif menu == "Goal History":
    st.title("📈 GOAL HISTORY")
    for entry in reversed(st.session_state.goal_history):
        with st.expander(f"Goals for {entry['date']}"):
            for g in entry['goals']:
                st.write(f"🎯 {g}")

# --- PANIC MODE ---
if st.session_state.step == "panic":
    st.title("🚨 REALITY CHECK")
    for item in st.session_state.evidence_logs:
        st.write(f"✅ {item}")
    if st.button("Resume"):
        st.session_state.step = 1
        st.rerun()
