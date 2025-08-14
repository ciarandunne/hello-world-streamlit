import streamlit as st

# --- App Title ---
st.markdown("<h1 style='text-align: center; color: #4CAF50;'>Regina's Calculator</h1>", unsafe_allow_html=True)

# --- Session state ---
if 'display' not in st.session_state:
    st.session_state.display = ""
if 'result' not in st.session_state:
    st.session_state.result = ""

# --- Functions ---
def press(key):
    st.session_state.display += str(key)

def clear():
    st.session_state.display = ""
    st.session_state.result = ""

def calculate():
    try:
        st.session_state.result = str(eval(st.session_state.display))
    except Exception:
        st.session_state.result = "Error"

# --- Display ---
st.text_input("Input", value=st.session_state.display, key="display_box", disabled=True)
st.markdown(f"<h3 style='text-align: right; color: blue;'>{st.session_state.result}</h3>", unsafe_allow_html=True)

# --- Buttons ---
buttons = [
    ['7','8','9','/'],
    ['4','5','6','*'],
    ['1','2','3','-'],
    ['0','.','=','+']
]

for row in buttons:
    cols = st.columns([1,1,1,1])
    for i, button in enumerate(row):
        # Bigger button style using markdown hack
        if cols[i].button(f"**{button}**", key=f"{row[i]}"):
            if button == "=":
                calculate()
            else:
                press(button)

# Clear button (full width)
if st.button("C"):
    clear()
