# 🧮 Calculator CLI App with Emojis
# ✍️ Author: [Your Name]
# 📄 Description: A user-friendly command-line calculator with emoji interface

# ➕ Addition
def add(a, b):
    return a + b

# ➖ Subtraction
def subtract(a, b):
    return a - b

# ✖️ Multiplication
def multiply(a, b):
    return a * b

# ➗ Division with error handling
def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "🚫 Error: Cannot divide by zero!"

# 🧠 Perform operation based on choice
def perform_operation(choice, num1, num2):
    if choice == '1':
        return f"✅ Result: {add(num1, num2)}"
    elif choice == '2':
        return f"✅ Result: {subtract(num1, num2)}"
    elif choice == '3':
        return f"✅ Result: {multiply(num1, num2)}"
    elif choice == '4':
        return f"✅ Result: {divide(num1, num2)}"
    else:
        return "⚠️ Invalid operation."

# 🔁 Main calculator loop
def calculator():
    print("🎉 Welcome to the Python CLI Calculator! 🧮")
    while True:
        print("\nChoose an operation:")
        print("1  Add ➕")
        print("2  Subtract ➖")
        print("3  Multiply ✖")
        print("4  Divide ➗")
        print("5  Exit  🚪")

        choice = input("👉 Enter your choice (1/2/3/4/5): ")

        if choice == '5':
            print("👋 Thanks for using the calculator. Goodbye! 🌟")
            break

        try:
            num1 = float(input("🔢 Enter the first number: "))
            num2 = float(input("🔢 Enter the second number: "))
        except ValueError:
            print("❌ Invalid input. Please enter numbers only.")
            continue

        print(perform_operation(choice, num1, num2))

# ▶️ Run the calculator
if __name__ == "__main__":
    calculator()
