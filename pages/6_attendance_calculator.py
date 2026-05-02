import streamlit as st

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

.stNumberInput input {
    border-radius: 10px;
    padding: 10px;
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

st.title("📊 Attendance Calculator")

st.markdown(
    '<div class="card">Calculate your attendance percentage using total lectures and lectures attended.</div>',
    unsafe_allow_html=True
)

total_lectures = st.number_input(
    "Total Lectures Conducted",
    min_value=0,
    step=1
)

attended_lectures = st.number_input(
    "Lectures Attended",
    min_value=0,
    step=1
)

if st.button("Calculate Attendance"):
    if total_lectures == 0:
        st.error("Total lectures cannot be zero.")
    elif attended_lectures > total_lectures:
        st.error("Lectures attended cannot be more than total lectures.")
    else:
        attendance = (attended_lectures / total_lectures) * 100

        st.success(f"Your Attendance is: {attendance:.2f}%")

        if attendance >= 75:
            st.info("Status: Safe ✅ Your attendance is above 75%.")
        else:
            required = ((0.75 * total_lectures) - attended_lectures) / 0.25
            required = int(required) + 1

            st.warning(
                f"Status: Low Attendance ⚠️ You need to attend approximately {required} more lectures continuously to reach 75%."
            )