import streamlit as st

# App title
st.title("Regina's Simple Calculator")

# Input numbers
num1 = st.number_input("Enter the first number")
num2 = st.number_input("Enter the second number")

# Select operation
operation = st.selectbox("Select an operation", ["Add", "Subtract", "Multiply", "Divide"])

# Calculate result
if st.button("Calculate"):
    if operation == "Add":
        result = num1 + num2
    elif operation == "Subtract":
        result = num1 - num2
    elif operation == "Multiply":
        result = num1 * num2
    elif operation == "Divide":
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Error: Cannot divide by zero"
    st.write("Result:", result)
