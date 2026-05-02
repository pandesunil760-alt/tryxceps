import streamlit as st
import random
import string

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
.stTextArea textarea,
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

st.title("✨ Magic Modes")

st.markdown(
    '<div class="card">A collection of fun and useful tools inside Arjun AI Suite.</div>',
    unsafe_allow_html=True
)

mode = st.selectbox(
    "Choose a Magic Mode",
    [
        "Password Generator",
        "Random Joke Generator",
        "Quote of the Day",
        "Mood-Based Song Suggestions",
        "Username Generator",
        "Fake Weather Generator",
        "Daily Study Planner",
        "GPA / Percentage Calculator",
        "Spin the Wheel",
        "Mini Quiz"
    ]
)

st.write("---")

# 1 PASSWORD GENERATOR
if mode == "Password Generator":
    st.subheader("🔐 Password Generator")

    length = st.slider("Password length", 6, 30, 12)
    use_symbols = st.checkbox("Include symbols", value=True)

    if st.button("Generate Password"):
        chars = string.ascii_letters + string.digits
        if use_symbols:
            chars += "!@#$%^&*"

        password = "".join(random.choice(chars) for _ in range(length))
        st.success(f"Generated Password: `{password}`")

# 2 JOKE GENERATOR
elif mode == "Random Joke Generator":
    st.subheader("🤣 Random Joke Generator")

    jokes = [
        "Why do programmers prefer dark mode? Because light attracts bugs.",
        "I told my computer I needed a break, and now it won’t stop sending me KitKat ads.",
        "Why did Python go to therapy? Too many unresolved imports.",
        "Debugging is like being a detective in a crime movie where you are also the murderer.",
        "My code works. I have no idea why. So naturally, I won’t touch it."
    ]

    if st.button("Tell me a joke"):
        st.info(random.choice(jokes))

# 3 QUOTE GENERATOR
elif mode == "Quote of the Day":
    st.subheader("💡 Quote of the Day")

    quotes = [
        "Small progress is still progress.",
        "Discipline beats motivation.",
        "The best way to learn is to build.",
        "Errors are proof that you are trying.",
        "A working project is better than a perfect idea."
    ]

    if st.button("Show Quote"):
        st.success(random.choice(quotes))

# 4 SONG SUGGESTIONS
elif mode == "Mood-Based Song Suggestions":
    st.subheader("🎧 Mood-Based Song Suggestions")

    mood = st.selectbox("Select your mood", ["Happy", "Sad", "Focus", "Gym", "Chill"])

    songs = {
        "Happy": ["Ilahi", "Uptown Funk", "On Top of the World"],
        "Sad": ["Channa Mereya", "Let Her Go", "Fix You"],
        "Focus": ["Lo-fi Beats", "Weightless", "Deep Focus Playlist"],
        "Gym": ["Believer", "Stronger", "Lose Yourself"],
        "Chill": ["Perfect", "Sunflower", "Night Changes"]
    }

    if st.button("Suggest Songs"):
        for song in songs[mood]:
            st.markdown(f'<div class="card">🎵 {song}</div>', unsafe_allow_html=True)

# 5 USERNAME GENERATOR
elif mode == "Username Generator":
    st.subheader("🆔 Username Generator")

    name = st.text_input("Enter your name or keyword")
    style = st.selectbox("Choose style", ["Cool", "Gaming", "Simple", "Tech"])

    if st.button("Generate Usernames") and name:
        base = name.lower().replace(" ", "")

        usernames = [
            f"{base}_{random.randint(10,999)}",
            f"{base}x{random.randint(100,999)}",
            f"the{base}",
            f"{base}_official",
            f"{base}verse"
        ]

        if style == "Gaming":
            usernames += [
                f"{base}ff",
                f"{base}op",
                f"{base}yt",
                f"x{base}x"
            ]

        if style == "Tech":
            usernames += [
                f"{base}dev",
                f"{base}ai",
                f"{base}tech",
                f"codewith{base}"
            ]

        for user in usernames:
            st.markdown(f'<div class="card">@{user}</div>', unsafe_allow_html=True)

# 6 FAKE WEATHER
elif mode == "Fake Weather Generator":
    st.subheader("🌤️ Fake Weather Generator")

    city = st.text_input("Enter city name")

    weather_types = ["Sunny", "Cloudy", "Rainy", "Windy", "Hot", "Cool"]
    temperatures = list(range(18, 42))

    if st.button("Generate Weather") and city:
        weather = random.choice(weather_types)
        temp = random.choice(temperatures)

        st.success(f"Weather in {city}: {weather}, {temp}°C")

# 7 STUDY PLANNER
elif mode == "Daily Study Planner":
    st.subheader("📅 Daily Study Planner")

    subject = st.text_input("Subject")
    hours = st.number_input("Study hours", min_value=1, max_value=12, step=1)
    task = st.text_area("Topics to study")

    if st.button("Create Plan"):
        st.markdown(
            f"""
            <div class="card">
            <b>Subject:</b> {subject}<br>
            <b>Study Time:</b> {hours} hours<br>
            <b>Topics:</b> {task}<br><br>
            ✅ Revise basics<br>
            ✅ Practice examples<br>
            ✅ Take short breaks<br>
            ✅ Review important points
            </div>
            """,
            unsafe_allow_html=True
        )

# 8 GPA / PERCENTAGE CALCULATOR
elif mode == "GPA / Percentage Calculator":
    st.subheader("📊 Percentage Calculator")

    obtained = st.number_input("Marks Obtained", min_value=0.0, step=1.0)
    total = st.number_input("Total Marks", min_value=0.0, step=1.0)

    if st.button("Calculate Percentage"):
        if total == 0:
            st.error("Total marks cannot be zero.")
        elif obtained > total:
            st.error("Obtained marks cannot be greater than total marks.")
        else:
            percentage = (obtained / total) * 100
            st.success(f"Percentage: {percentage:.2f}%")

# 9 SPIN THE WHEEL
elif mode == "Spin the Wheel":
    st.subheader("🎯 Spin the Wheel")

    options_text = st.text_area(
        "Enter options separated by commas",
        "Study, Gym, Sleep, Code, Chill"
    )

    if st.button("Spin"):
        options = [x.strip() for x in options_text.split(",") if x.strip()]
        if options:
            result = random.choice(options)
            st.success(f"Selected: {result}")
        else:
            st.error("Please enter at least one option.")

# 10 MINI QUIZ
elif mode == "Mini Quiz":
    st.subheader("🧩 Mini Quiz")

    questions = [
        {
            "q": "What does AI stand for?",
            "options": ["Artificial Intelligence", "Automatic Internet", "Advanced Input"],
            "answer": "Artificial Intelligence"
        },
        {
            "q": "Which language is used in this project?",
            "options": ["Python", "Java", "C++"],
            "answer": "Python"
        },
        {
            "q": "Which framework is used for the UI?",
            "options": ["Streamlit", "React", "Flutter"],
            "answer": "Streamlit"
        }
    ]

    score = 0

    for i, item in enumerate(questions):
        choice = st.radio(item["q"], item["options"], key=i)
        if choice == item["answer"]:
            score += 1

    if st.button("Submit Quiz"):
        st.success(f"Your Score: {score}/{len(questions)}")