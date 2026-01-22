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
    
    /* Input Boxes & Text Areas */
    textarea, input, div[data-baseweb="base-input"] {
        background-color: #1A1A1A !important; 
        color: #FFFFFF !important; 
        border: 2px solid #00FF00 !important;
    }

    /* Selectbox Styling - Ensuring Visibility */
    div[data-baseweb="select"] > div, div[data-testid="stSelectbox"] div[role="button"] {
        background-color: #1A1A1A !important; color: #FFFFFF !important; border: 2px solid #00FF00 !important;
    }
    div[data-baseweb="popover"] ul { background-color: #1A1A1A !important; border: 2px solid #00FF00 !important; }
    div[data-baseweb="popover"] li { background-color: #1A1A1A !important; color: #FFFFFF !important; }
    div[data-baseweb="popover"] li:hover { background-color: #00FF00 !important; color: #000000 !important; }
    
    /* Buttons */
    .stButton>button { width: 100%; background-color: #00FF00 !important; color: #000000 !important; font-weight: bold !important; border: none; height: 3em; }
    
    /* Sidebar */
    section[data-testid="stSidebar"] { background-color: #111111 !important; }
    </style>
    """, unsafe_allow_html=True)

# --- INITIALIZE SESSION STATE ---
if 'step' not in st.session_state:
    st.session_state.step = 1
if 'evidence_logs' not in st.session_state:
    st.session_state.evidence_logs = [
        "I have a family who is in my life.", 
        "I earned qualifications despite my education history.", 
        "I have friends who care about me."
    ]
if 'goal_history' not in st.session_state:
    st.session_state.goal_history = []
if 'meditation_reps' not in st.session_state:
    st.session_state.meditation_reps = 0

# Your provided unhelpful thoughts list
unhelpful_list = [
    "I can't get a job", "I can't speak up and express myself", "People think I am a fool",
    "I am useless", "I am hopeless", "I am horrible", "I am a failure", "I am ugly",
    "I am stupid", "I am a disappointment", "I am not worth knowing", "I am worthless",
    "I am ridiculous", "I am fucked", "People are looking at my oily nose",
    "People are judging me", "People feel sorry for me", "People feel disappointed in me",
    "My kids hate me", "I have hurt my kids from not working", "I am heartless",
    "I am irritating", "I will always fail"
]

# --- NAVIGATION ---
menu = st.sidebar.radio("CHOOSE TOOL:", ["The Truth Drill", "Setback Recovery", "Meditation Lab", "The Standard Shifter", "Evidence & Goals", "Goal History"])

if st.sidebar.button("🚨 PANIC: I'M SPIRALING"):
    st.session_state.step = "panic"

# --- TOOL 1: THE TRUTH DRILL ---
if menu == "The Truth Drill" and st.session_state.step != "panic":
    st.title("⚖️ THE TRUTH DRILL")
    
    if st.session_state.step == 1:
        st.subheader("1. What are you thinking?")
        selection = st.selectbox("Choose a thought or select 'Other' to type:", ["Select one..."] + unhelpful_list + ["Other..."])
        
        if selection == "Other...":
            thought = st.text_input("Type your thought here:")
        else:
            thought = selection
            
        st.subheader("2. What are you feeling?")
        feeling = st.text_input("e.g., Shame, Fear, Inadequacy")
        
        st.subheader("3. What do you think this says about you?")
        belief = st.text_input("e.g., That I am a disappointment")
        
        if st.button("Drill Down →") and thought != "Select one..." and belief != "":
            st.session_state.thought, st.session_state.feeling, st.session_state.belief = thought, feeling, belief
            st.session_state.step = 2
            st.rerun()

    elif st.session_state.step == 2:
        st.subheader("Identity Audit")
        st.write(f"**Target Belief:** {st.session_state.belief}")
        
        q1 = st.text_area("What does this label mean? Describe it like you were describing it to a friend:")
        q2 = st.text_input("By whose definition are you this? (e.g., My father's, My mother's, Society's)")
        q3 = st.text_area("Neutral Observation: Considering the ups and downs of life, describe the situation without bias:")
        
        st.write("---")
        truth_rating = st.slider(f"How true is '{st.session_state.belief}' (1 = Not at all, 10 = Absolutely)?", 1, 10, 5)
        reasoning = st.selectbox("Reasoning:", [
            "Select an insight...",
            "This makes me human, not a failure.",
            "My bias is distorting the truth here.",
            "I can always get better; this isn't permanent.",
            "This shows how false this belief is.",
            "This is a legacy script from my past, not my reality today."
        ])

        if st.button("The Final Verdict →") and reasoning != "Select an insight...":
            st.session_state.neutral_view = q3
            st.session_state.truth_rating = truth_rating
            st.session_state.reasoning = reasoning
            st.session_state.step = 3
            st.rerun()

    elif st.session_state.step == 3:
        st.error("### THE PARENTAL SCRIPT")
        st.write(f"In spite of a childhood riddled with insecure and cruel comments, your brain tries to tell you that you are '{st.session_state.belief}'.")
        st.write(f"You rated this as a **{st.session_state.truth_rating}/10** truth and noted: **{st.session_state.reasoning}**")
        
        st.success("### THE ADULT TRUTH")
        st.info(f"**Reality:** {st.session_state.neutral_view}")
        st.write("**The Untouchable Evidence of Your Life:**")
        for item in st.session_state.evidence_logs:
            st.write(f"✅ {item}")
        
        if st.button("Reset Drill"):
            st.session_state.step = 1
            st.rerun()

# --- TOOL 2: SETBACK RECOVERY (SO WHAT?) ---
elif menu == "Setback Recovery":
    st.title("🔄 SETBACK RECOVERY")
    event = st.text_input("What went wrong today?")
    if event:
        st.write("### THE 'SO WHAT?' DRILL")
        s1 = st.text_input(f"1. If it's true that {event}, so what? Why does that matter?")
        s2 = st.text_input("2. And why does *that* matter?")
        s3 = st.selectbox("3. Which core belief is this trying to trigger?", unhelpful_list)
        
        if st.button("Is that really you?"):
            st.warning(f"**REALITY:** You are a 54-year-old survivor. Your brain is trying to use a mistake to prove you are '{s3}'.")
            st.write("Mistakes are data. They do not overwrite your life as a father and a qualified adult.")

# --- TOOL 3: MEDITATION LAB ---
elif menu == "Meditation Lab":
    st.title("🧘 MEDITATION LAB")
    st.write("It is 2026. You are 54. You are safe. Ground yourself in the present.")
    duration = st.slider("Session length (minutes):", 1, 20, 5)
    if st.button("Start Timer"):
        placeholder = st.empty()
        for t in range(duration * 60, 0, -1):
            m, s = divmod(t, 60)
            placeholder.metric("Breathe... Time Left:", f"{m:02d}:{s:02d}")
            time.sleep(1)
        st.session_state.meditation_reps += 1
        st.success("Rep complete. You maintained control.")

# --- TOOL 4: THE STANDARD SHIFTER ---
elif menu == "The Standard Shifter":
    st.title("📏 THE STANDARD SHIFTER")
    st.write("Let's redefine 'Success' and 'Providing' on your terms, not theirs.")
    col1, col2 = st.columns(2)
    with col1:
        st.header("Legacy Rules")
        st.write("❌ Worth is a Paycheck.")
        st.write("❌ Errors are Shameful.")
    with col2:
        st.header("My Adult Rules")
        s1 = st.text_input("I define 'Success' as:")
        s2 = st.text_input("I define 'Providing' as:")
    if st.button("Adopt My Standards"):
        st.success("Standards updated. You are the judge now.")

# --- TOOL 5: EVIDENCE & GOALS ---
elif menu == "Evidence & Goals":
    st.title("📖 REALITY & FUTURE")
    st.header("1. Evidence Log")
    new_win = st.text_input("Record an adult win (Evidence of your truth):")
    if st.button("Save Win") and new_win:
        st.session_state.evidence_logs.append(new_win)
    
    st.write("---")
    st.header("2. Tomorrow's Goals")
    st.write("Set a **minimum of 3** things you will strive to achieve tomorrow:")
    g1 = st.text_input("Goal 1:")
    g2 = st.text_input("Goal 2:")
    g3 = st.text_input("Goal 3:")
    g4 = st.text_input("Goal 4 (Optional):")

    if st.button("Lock in Goals"):
        if g1 and g2 and g3:
            st.session_state.goal_history.append({"date": time.strftime("%Y-%m-%d"), "goals": [g1, g2, g3, g4]})
            st.success("Goals locked in for tomorrow.")
        else:
            st.error("Please enter a minimum of 3 goals to continue.")

# --- TOOL 6: GOAL HISTORY ---
elif menu == "Goal History":
    st.title("📈 GOAL HISTORY")
    st.write(f"Total Meditation Sessions: {st.session_state.meditation_reps}")
    for entry in reversed(st.session_state.goal_history):
        with st.expander(f"Goals for {entry['date']}"):
            for g in entry['goals']:
                if g: st.write(f"🎯 {g}")

# --- PANIC MODE ---
if st.session_state.step == "panic":
    st.title("🚨 REALITY CHECK")
    st.warning("You are in a legacy script trigger. Ground yourself.")
    for item in st.session_state.evidence_logs:
        st.write(f"✅ {item}")
    st.info("You are a 54-year-old adult in 2026. Your parents' comments are echoes, not facts.")
    if st.button("Resume"):
        st.session_state.step = 1
        st.rerun()
