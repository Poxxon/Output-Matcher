import tkinter as tk
from tkinter import messagebox

def match_strings():
    input_string = input_text.get()
    expected_string = expected_text.get()

    if input_string == expected_string:
        result_label.config(text="Match: ✅", fg="green")
    else:
        result_label.config(text="Mismatch: ❌", fg="red")

def reset_fields():
    input_text.delete(0, tk.END)
    expected_text.delete(0, tk.END)
    result_label.config(text="")

# Create the main window
root = tk.Tk()
root.title("String Matcher")
root.geometry("400x300")

# Input Label and Textbox
tk.Label(root, text="Input String:").pack(pady=5)
input_text = tk.Entry(root, width=50)
input_text.pack(pady=5)

# Expected Label and Textbox
tk.Label(root, text="Expected String:").pack(pady=5)
expected_text = tk.Entry(root, width=50)
expected_text.pack(pady=5)

# Match Button
match_button = tk.Button(root, text="Match", command=match_strings)
match_button.pack(pady=10)

# Reset Button
reset_button = tk.Button(root, text="Reset", command=reset_fields)
reset_button.pack(pady=5)

# Result Label
result_label = tk.Label(root, text="", font=("Arial", 14))
result_label.pack(pady=20)

# Run the application
root.mainloop()
