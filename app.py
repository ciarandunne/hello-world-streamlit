import streamlit as st

# App title
st.title("Regina's Modern Streamlit Calculator")

# Initialize session state for display and result
if 'display' not in st.session_state:
    st.session_state.display = ""
if 'result' not in st.session_state:
    st.session_state.result = ""

# Function to update display
def press(key):
    st.session_state.display += str(key)

# Function to clear display
def clear():
    st.session_state.display = ""
    st.session_state.result = ""

# Function to calculate result
def calculate():
    try:
        st.session_state.result = str(eval(st.session_state.display))
    except Exception:
        st.session_state.result = "Error"

# Display current input and result
st.text_input("Input", value=st.session_state.display, key="display_box", disabled=True)
st.text("Result: " + st.session_state.result)

# Calculator buttons
cols = st.columns(4)

buttons = [
    ['7','8','9','/'],
    ['4','5','6','*'],
    ['1','2','3','-'],
    ['0]()
