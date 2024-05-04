import streamlit as st

def process(text):
    return text.upper()

if __name__ == "__main__":
    st.title("Echo Uppercase")
    input_text = st.text_input("Prompt:")
    if st.button("Submit"):
        output_text = process(input_text)
        st.write(output_text)
