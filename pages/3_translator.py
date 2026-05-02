import streamlit as st

st.markdown("""<style>
.stApp { background: linear-gradient(135deg, #00c6ff, #ffffff); }
</style>""", unsafe_allow_html=True)

st.title("🌍 Translator")

text = st.text_area("Enter text")

lang = st.selectbox("Translate to", ["Hindi", "French"])

if st.button("Translate"):
    if lang == "Hindi":
        st.write("नमस्ते (demo)")
    else:
        st.write("Bonjour (demo)")