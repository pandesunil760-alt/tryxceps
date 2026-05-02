import streamlit as st
import random

# CSS STYLE
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #00c6ff, #ffffff);
    color: black;
}

h1, h2, h3, p, label {
    color: black !important;
}

section[data-testid="stSidebar"] {
    background-color: #0f172a;
}

section[data-testid="stSidebar"] * {
    color: white !important;
}

.card {
    background: rgba(255,255,255,0.65);
    padding: 18px;
    border-radius: 14px;
    margin-bottom: 15px;
    box-shadow: 0px 4px 12px rgba(0,0,0,0.12);
}

.stTextInput>div>div>input,
.stNumberInput input,
.stSelectbox>div>div {
    border-radius: 10px;
    background-color: rgba(255,255,255,0.85);
    color: black;
}

.stButton>button {
    border-radius: 10px;
    background-color: #00aaff;
    color: white;
    border: none;
    padding: 10px 20px;
    font-weight: 600;
}
</style>
""", unsafe_allow_html=True)

st.title("🎮 Mini Games")

st.markdown(
    '<div class="card">Play simple mini games inside Arjun AI Suite. Because even projects deserve a personality.</div>',
    unsafe_allow_html=True
)

game = st.selectbox(
    "Choose a game",
    [
        "Guess the Number",
        "Rock Paper Scissors",
        "Dice Roller",
        "Coin Toss",
        "Quick Math Quiz"
    ]
)

st.write("---")

# GAME 1: Guess the Number
if game == "Guess the Number":
    st.subheader("🔢 Guess the Number")

    if "secret_number" not in st.session_state:
        st.session_state.secret_number = random.randint(1, 10)

    st.markdown(
        '<div class="card">I have selected a number between 1 and 10. Try to guess it.</div>',
        unsafe_allow_html=True
    )

    guess = st.number_input("Enter your guess", min_value=1, max_value=10, step=1)

    if st.button("Check Guess"):
        if guess == st.session_state.secret_number:
            st.success("Correct! 🎉 You guessed the number.")
            st.session_state.secret_number = random.randint(1, 10)
            st.info("New number generated. Play again.")
        elif guess < st.session_state.secret_number:
            st.warning("Too low. Try a bigger number.")
        else:
            st.warning("Too high. Try a smaller number.")

    if st.button("Reset Number"):
        st.session_state.secret_number = random.randint(1, 10)
        st.info("Number reset successfully.")

# GAME 2: Rock Paper Scissors
elif game == "Rock Paper Scissors":
    st.subheader("✊ Rock Paper Scissors")

    choices = ["Rock", "Paper", "Scissors"]
    user_choice = st.selectbox("Choose your move", choices)

    if st.button("Play"):
        computer_choice = random.choice(choices)

        st.markdown(
            f'<div class="card"><b>Your choice:</b> {user_choice}<br><b>Computer choice:</b> {computer_choice}</div>',
            unsafe_allow_html=True
        )

        if user_choice == computer_choice:
            st.info("It's a tie.")
        elif (
            (user_choice == "Rock" and computer_choice == "Scissors") or
            (user_choice == "Paper" and computer_choice == "Rock") or
            (user_choice == "Scissors" and computer_choice == "Paper")
        ):
            st.success("You win! 🎉")
        else:
            st.error("Computer wins. Tragic, but expected.")

# GAME 3: Dice Roller
elif game == "Dice Roller":
    st.subheader("🎲 Dice Roller")

    st.markdown(
        '<div class="card">Click the button to roll a dice.</div>',
        unsafe_allow_html=True
    )

    if st.button("Roll Dice"):
        dice = random.randint(1, 6)
        st.success(f"You rolled: {dice}")

# GAME 4: Coin Toss
elif game == "Coin Toss":
    st.subheader("🪙 Coin Toss")

    st.markdown(
        '<div class="card">Click the button to toss a coin.</div>',
        unsafe_allow_html=True
    )

    if st.button("Toss Coin"):
        result = random.choice(["Heads", "Tails"])
        st.success(f"Result: {result}")

# GAME 5: Quick Math Quiz
elif game == "Quick Math Quiz":
    st.subheader("🧮 Quick Math Quiz")

    if "math_a" not in st.session_state:
        st.session_state.math_a = random.randint(1, 20)
        st.session_state.math_b = random.randint(1, 20)

    a = st.session_state.math_a
    b = st.session_state.math_b
    correct_answer = a + b

    st.markdown(
        f'<div class="card">Solve this: <b>{a} + {b}</b></div>',
        unsafe_allow_html=True
    )

    answer = st.number_input("Your answer", step=1)

    if st.button("Submit Answer"):
        if answer == correct_answer:
            st.success("Correct! 🎉")
            st.session_state.math_a = random.randint(1, 20)
            st.session_state.math_b = random.randint(1, 20)
            st.info("New question generated.")
        else:
            st.error(f"Wrong. Correct answer is {correct_answer}. Painful, but educational.")

    if st.button("New Question"):
        st.session_state.math_a = random.randint(1, 20)
        st.session_state.math_b = random.randint(1, 20)
        st.info("New question generated.")