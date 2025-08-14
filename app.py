import streamlit as st

st.title("Hello World App")

st.write("Hello, world!")

name = st.text_input("What's your name?")

if name:
    st.write(f"Hello, {name}!")
