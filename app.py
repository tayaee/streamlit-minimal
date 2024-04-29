import streamlit as st

def process(text):
    return "Hello " + text

if __name__ == "__main__":
    st.title("Demo app v5 from github cs")
    input_text = st.text_input("Prompt:")
    if st.button("Submit"):
        output_text = process(input_text)
        st.write("Response:", output_text)
