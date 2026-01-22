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

    /* Selectbox Styling */
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
    
    /* Slider */
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

# --- NAVIGATION ---
menu = st.sidebar.radio("CHOOSE TOOL:", ["The Truth Drill", "Setback Recovery", "Meditation Lab", "The Standard Shifter", "Evidence & Goals", "Goal History"])

if st.sidebar.button("🚨 PANIC: I'M SPIRALING"):
    st.session_state.step = "panic"

# --- TOOL 1: THE TRUTH DRILL (REVISED: WRITE-IN BOX) ---
if menu == "The Truth Drill" and st.session_state.step != "panic":
    st.title("⚖️ THE TRUTH DRILL")
    
    if st.session_state.step == 1:
        # User can now write the thought directly
        thought = st.text_input("What is the surface thought?", placeholder="e.g., I am a failure / I can't get a job")
        belief = st.text_input("What does your brain claim this says about you?", placeholder="e.g., I am worthless")
        if st.button("Drill Down →") and thought != "":
            st.session_state.thought, st.session_state.belief = thought, belief
            st.session_state.step = 2
            st.rerun()

    elif st.session_state.step == 2:
        st.subheader("Contextual Reality Check")
        st.write(f"**Current Label:** {st.session_state.belief}")
        
        q1 = st.text_area(f"1. Describe what '{st.session_state.belief}' looks like considering the ups and downs of life.")
        q2 = st.text_input(f"2. By whose definition are you '{st.session_state.belief}'?")
        q3 = st.text_area("3. Neutral Observation: Describe the situation without the cruel labels (like a journalist).")
        
        st.write("---")
        st.subheader("The Truth Test")
        truth_rating = st.slider(f"On a scale of 1-10, how true is the label '{st.session_state.belief}' in this context?", 1, 10, 5)
        reasoning = st.selectbox("What does this reveal?", [
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
        st.write(f"You identified that the label '{st.session_state.belief}' is a **{st.session_state.truth_rating}/10** truth. You recognized: **{st.session_state.reasoning}**")
        
        st.success("### THE ADULT REALITY")
        st.info(f"**Neutral Observation:** {st.session_state.neutral_view}")
        st.write("**Your Evidence Bank:**")
        for item in st.session_state.evidence_logs:
            st.write(f"✅ {item}")
        
        if st.button("Reset Drill"):
            st.session_state.step = 1
            st.rerun()

# --- TOOL 2: SETBACK RECOVERY (WITH PHYSICAL REP) ---
elif menu == "Setback Recovery":
    st.title("🔄 SETBACK RECOVERY")
    event = st.text_input("What went wrong?")
    if event:
        st.write("### THE 'SO WHAT?' DRILL")
        s1 = st.text_input(f"If it's true that '{event}', so what? What is the worst-case result?")
        s2 = st.text_area("Considering your upbringing, describe this situation without bias:")
        
        st.write("---")
        st.subheader("Is that really you?")
        st.write("Is it possible you are a 54-year-old human making a mistake, or are you the 'broken' child your parents described?")
        
        if st.button("I am a human making a mistake"):
            st.balloons()
            st.success("Correct. The old script is lying.")
            st.info("**PHYSICAL RECOVERY REP:** Break the cycle. Do 10 deep breaths, a 2-minute walk, or 5 pushups right now. Then come back.")

# --- TOOL 3: MEDITATION LAB ---
elif menu == "Meditation Lab":
    st.title("🧘 MEDITATION LAB")
    st.write("Ground yourself. It is 2026. You are in control.")
    duration = st.slider("Set session length (minutes):", 1, 20, 5)
    if st.button("Start Meditation"):
        placeholder = st.empty()
        for t in range(duration * 60, 0, -1):
            m, s = divmod(t, 60)
            placeholder.metric("Time Remaining:", f"{m:02d}:{s:02d}")
            time.sleep(1)
        st.session_state.meditation_reps += 1
        st.success("Session complete. Evidence added.")

# --- TOOL 4: THE STANDARD SHIFTER ---
elif menu == "The Standard Shifter":
    st.title("📏 THE STANDARD SHIFTER")
    col1, col2 = st.columns(2)
    with col1:
        st.header("Legacy Rules")
        st.write("❌ Never fail.")
        st.write("❌ Always provide.")
    with col2:
        st.header("My Adult Rules")
        new_success = st.text_input("My new definition of a 'Good Day' is:")
    if st.button("Update Standards"):
        st.success("New standards locked in.")

# --- TOOL 5: EVIDENCE & GOALS ---
elif menu == "Evidence & Goals":
    st.title("📖 REALITY & FUTURE")
    new_win = st.text_input("Record an adult win:")
    if st.button("Save Win") and new_win:
        st.session_state.evidence_logs.append(new_win)
    st.write("---")
    st.header("Tomorrow's Goals (Min 3)")
    g1, g2, g3 = st.text_input("Goal 1:"), st.text_input("Goal_2:"), st.text_input("Goal_3:")
    if st.button("Lock in Goals"):
        if g1 and g2 and g3:
            st.session_state.goal_history.append({"date": time.strftime("%Y-%m-%d"), "goals": [g1, g2, g3]})
            st.success("Goals locked.")

# --- TOOL 6: GOAL HISTORY ---
elif menu == "Goal History":
    st.title("📈 GOAL HISTORY")
    st.write(f"Total Meditation Sessions: {st.session_state.meditation_reps}")
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
