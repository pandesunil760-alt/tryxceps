import streamlit as st

st.markdown("""<style>
.stApp { background: linear-gradient(135deg, #00c6ff, #ffffff); }
</style>""", unsafe_allow_html=True)

st.title("📄 Document Q&A")

file = st.file_uploader("Upload text file", type=["txt"])

if file:
    text = file.read().decode()
    st.write("Document Loaded")

    q = st.text_input("Ask something")

    if q:
        if q.lower() in text.lower():
            st.write("Answer found in document")
        else:
            st.write("Demo answer based on document")