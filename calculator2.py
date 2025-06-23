import tkinter as tk
from tkinter import messagebox

# Define calculator functions
def calculate():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        operation = operation_var.get()

        if operation == "Add":
            result = num1 + num2
        elif operation == "Subtract":
            result = num1 - num2
        elif operation == "Multiply":
            result = num1 * num2
        elif operation == "Divide":
            if num2 == 0:
                messagebox.showerror("Error", "Cannot divide by zero!")
                return
            result = num1 / num2
        else:
            result = "Invalid operation"

        label_result.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers.")

# Create main window
app = tk.Tk()
app.title("Simple Calculator")

# First number input
tk.Label(app, text="Enter First Number").grid(row=0, column=0, padx=10, pady=5)
entry1 = tk.Entry(app)
entry1.grid(row=0, column=1, padx=10, pady=5)

# Second number input
tk.Label(app, text="Enter Second Number").grid(row=1, column=0, padx=10, pady=5)
entry2 = tk.Entry(app)
entry2.grid(row=1, column=1, padx=10, pady=5)

# Operation selection
tk.Label(app, text="Select Operation").grid(row=2, column=0, padx=10, pady=5)
operation_var = tk.StringVar()
operation_var.set("Add")
operations = ["Add", "Subtract", "Multiply", "Divide"]
tk.OptionMenu(app, operation_var, *operations).grid(row=2, column=1, padx=10, pady=5)

# Calculate button
tk.Button(app, text="Calculate", command=calculate).grid(row=3, column=0, columnspan=2, pady=10)

# Result display
label_result = tk.Label(app, text="Result: ", font=("Arial", 12))
label_result.grid(row=4, column=0, columnspan=2, pady=10)

# Start the GUI loop
app.mainloop()
