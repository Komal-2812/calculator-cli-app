import streamlit as st

# ➕ Basic operations
def add(a, b): return a + b
def subtract(a, b): return a - b
def multiply(a, b): return a * b
def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "🚫 Cannot divide by zero!"

# 🎉 Title
st.title("🧮 Streamlit Calculator")

# 🔢 Inputs
num1 = st.number_input("🔢 Enter the first number")
num2 = st.number_input("🔢 Enter the second number")

# 🧠 Choose operation
operation = st.selectbox("⚙️ Choose an operation", [
    "➕ Add",
    "➖ Subtract",
    "✖️ Multiply",
    "➗ Divide"
])

# 🧮 Perform calculation
if st.button("🧠 Calculate"):
    if operation == "➕ Add":
        result = add(num1, num2)
    elif operation == "➖ Subtract":
        result = subtract(num1, num2)
    elif operation == "✖️ Multiply":
        result = multiply(num1, num2)
    elif operation == "➗ Divide":
        result = divide(num1, num2)

    st.success(f"✅ Result: {result}")
