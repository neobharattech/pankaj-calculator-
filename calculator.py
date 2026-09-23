import streamlit as st

st.title("🧮 Pankaj calculator")
st.write("अपना पहला पायथन ऐप बनाना सीखें!")

num1 = st.number_input("enter your first number  (Number 1):", value=0.0)
num2 = st.number_input("enter your second number  (Number 2):", value=0.0)

operation = st.selectbox(
    " (Select Operation):",
    ["ADD (+)", "SUBTRACT (-)", "MULTIPLY (*)", "DIVIDE (/)"]
)

if st.button("Calculate"):
    result = 0
    error_flag = False

    if operation == "ADD (+)":
        result = num1 + num2
        sign = "+"
    elif operation == "SUBTRACT (-)":
        result = num1 - num2
        sign = "-"
    elif operation == "MULTIPLY (*)":
        result = num1 * num2
        sign = "*"
    elif operation == "DIVIDE (/)":
        if num2 != 0:
            result = num1 / num2
            sign = "/"
        else:
            st.error("त्रुटि: किसी भी नंबर को 0 से भाग नहीं दिया जा सकता!")
            error_flag = True

    if not error_flag:
        st.success(f"Your Answer: {num1} {sign} {num2} = {result}")

