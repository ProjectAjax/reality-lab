import streamlit as st

# 1. High-Contrast Theme Configuration
st.set_page_config(page_title="Reality Lab", page_icon="⚖️")

# Custom CSS for readability and ADHD focus
st.markdown("""
    <style>
    /* Force background to black */
    .stApp {
        background-color: #000000;
    }
    /* Labels (The questions) - Neon Green and Bold */
    label p {
        color: #00FF00 !important;
        font-size: 1.2rem !important;
        font-weight: bold !important;
    }
    /* Main text and headers - Stark White */
    h1, h2, h3, p, span, div {
        color: #FFFFFF !important;
    }
    /* Input Boxes - Dark grey background, white text */
    input, textarea, div[data-baseweb="select"] > div {
        background-color: #1A1A1A !important;
        color: #FFFFFF !important;
        border: 1px solid #00FF00 !important;
    }
    /* Buttons - High Contrast Neon */
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
    section[data-testid="stSidebar"] {
        background-color: #111111 !important;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("⚖️ THE REALITY LAB")

# Sidebar - Australian Logic
menu = st.sidebar.radio("CHOOSE TOOL:", ["The 5-Why Drill", "Exposure: Meter Reading", "Avoidance Buster", "Porn/Sabotage Circuit"])

if menu == "The 5-Why Drill":
    st.header("The 5-Why Evidence Audit")
    belief = st.selectbox("Current Core Belief:", ["I am a failure", "I am worthless", "I am stupid", "I am ugly"])
    
    st.write("---")
    w1 = st.text_input(f"1. What is the valid evidence that you are {belief}?")
    w2 = st.text_input("2. Even if that's true, why does it mean you're a failure (and not just human)?") if w1 else None
    w3 = st.text_input("3. What is the childhood 'root' of this feeling?") if w2 else None
    w4 = st.text_input("4. Is this belief helping you work, or just helping you hide?") if w3 else None
    w5 = st.text_input("5. THE 'SO WHAT?': If you are 'worthless' today, can you still do one useful thing?") if w4 else None
    
    if w5:
        st.success("LOGIC VERDICT:")
        st.write("**The Sceptic’s Truth:** Your brain says 'I am a failure' to protect you from trying. It’s a survival mechanism, not a fact.")
        st.write("**Management:** Accept the feeling of failure. Do the work anyway. The work doesn't care how you feel.")

elif menu == "Exposure: Meter Reading":
    st.header("HF-SET: Social Exposure")
    st.write("Current Job: Meter Reading.")
    st.write("**Reframing:** You aren't a 'meter reader.' You are a 'Social Exposure Athlete.' Each house is a rep.")
    
    shame = st.slider("Shame Intensity (0-10)", 0, 10, 5)
    houses = st.number_input("Number of Gates Opened", 0, 500, step=1)
    
    if st.button("Log Training Reps"):
        st.info(f"You faced {houses} potential judgements. You are still alive. The 'Worthless' narrative is losing its power through action.")

elif menu == "Avoidance Buster":
    st.header("The Avoidance Buster")
    task = st.text_input("What are you avoiding? (Work, church, business calls?)")
    
    if task:
        st.write("### THE SO-WHAT CHALLENGE:")
        st.write(f"1. If you do '{task}' and fail, you are exactly where you are now.")
        st.write(f"2. If you avoid it, you are GUARANTEEING failure.")
        st.write("**Logic:** The only way to lose is to avoid.")
        if st.button("Start 5-Minute Timer"):
            st.warning("Go. Do 5 minutes of it now. Stop thinking.")

elif menu == "Porn/Sabotage Circuit":
    st.header("Circuit Breaker")
    st.error("DANGER: SABOTAGE MODE DETECTED")
    st.write("You are likely triggered by a feeling of worthlessness. You want the AI generation to numb the pain.")
    
    if st.button("I am about to sabotage"):
        st.write("### READ THIS SLOWLY:")
        st.write("1. This is a dopamine hack for an ADHD brain. It’s not a moral fail, it’s a bad strategy.")
        st.write("2. In 30 minutes, you will feel 10x more 'ugly' and 'worthless' than you do now.")
        st.write("3. **ACTION:** Put the phone in another room. Drink a glass of water. Walk outside for 2 minutes.")
