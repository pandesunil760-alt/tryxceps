import streamlit as st

st.markdown("""<style>
.stApp { background: linear-gradient(135deg, #00c6ff, #ffffff); }
</style>""", unsafe_allow_html=True)

st.title("🧠 AI Agent (Math Solver)")

q = st.text_input("Enter math problem")

if st.button("Solve"):
    try:
        result = eval(q)
        st.write("Answer:", result)
    except:
        st.write("Invalid input")