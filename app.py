import streamlit as st

# Australian Context & Logic
st.set_page_config(page_title="Reality Lab", page_icon="⚖️")

st.markdown("""
    <style>
    .stApp { background-color: #0e1117; color: #ffffff; }
    .stButton>button { width: 100%; border-radius: 5px; height: 3em; background-color: #2e7d32; color: white; border: none; }
    .stTextArea>div>div>textarea { background-color: #262730; color: white; }
    </style>
    """, unsafe_allow_html=True)

st.title("⚖️ The Reality Lab")

# Logic: Sceptic-Proof CBT
menu = st.sidebar.radio("Select Tool", ["The 5-Why Drill", "Exposure: Meter Reading", "Avoidance Buster", "Porn/Sabotage Circuit"])

if menu == "The 5-Why Drill":
    st.header("The 5-Why Drill")
    belief = st.selectbox("Which core belief is active?", ["I am a failure", "I am worthless", "I am stupid", "I am ugly"])
    
    q1 = st.text_input(f"1. Why do you believe you are {belief} right now?")
    q2 = st.text_input("2. Why does that specifically prove your worthlessness?") if q1 else None
    q3 = st.text_input("3. Why is that 'evidence' actually a fact and not just a feeling?") if q2 else None
    q4 = st.text_input("4. Why did you learn to think this way as a child?") if q3 else None
    q5 = st.text_input("5. At the root, what is the 'So What?' (What happens if this is true?)") if q4 else None
    
    if q5:
        st.error("LOGIC CHECK:")
        st.write("Even if the evidence is 100% true (e.g., your business is struggling), **SO WHAT?**")
        st.write("Does a struggling business mean you cease to be a functioning human? No. It means you have a problem to solve. Solutions require logic, not shame.")

elif menu == "Exposure: Meter Reading":
    st.header("HF-SET: Social Exposure")
    st.info("Meter reading is your gym. You are being paid to let people see you while you feel ashamed. This is high-level training.")
    shame = st.slider("Shame Level (0-10)", 0, 10, 5)
    houses = st.number_input("Houses Visited", 0, 500, step=1)
    
    if st.button("Log Training Session"):
        st.success(f"Logged. You just did {houses} reps of social anxiety exposure. Your brain is rewiring even if you don't feel it yet.")

elif menu == "Avoidance Buster":
    st.header("The Avoidance Buster")
    task = st.text_input("What are you avoiding right now?")
    if task:
        st.write(f"**The Sceptic's Truth:** You are avoiding '{task}' because you are afraid of the 'Failure' label. But by avoiding it, you are **guaranteeing** the failure you fear.")
        if st.button("Commit to 5 Minutes"):
            st.warning("Action creates dopamine. Motivation is a myth. Start the timer.")

elif menu == "Porn/Sabotage Circuit":
    st.header("Circuit Breaker")
    st.write("You want to use porn or isolate because your brain is seeking a 'safe' dopamine hit to hide from shame.")
    if st.button("I am about to sabotage"):
        st.error("STOP.")
        st.write("1. You are not 'evil.' You are under-stimulated and over-stressed (ADHD).")
        st.write("2. This hit will last 10 minutes. The shame will last 3 days.")
        st.write("3. **The Counter-Move:** Go into a different room. Call one person. Do not explain why, just say hello.")
