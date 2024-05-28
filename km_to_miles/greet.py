import tkinter as tk

def greet():
    name = name_entry.get()  # Get the text from the entry widget
    greeting_label.config(text=f"Hello, {name}!")  # Update the label with the greeting

# Create the main window
root = tk.Tk()
root.title("Greeting App")
root.geometry("500x500")

# Create a label for instructions
instruction_label = tk.Label(root, text="Enter your name:")
instruction_label.pack(pady=10)

# Create an entry widget for the name input
name_entry = tk.Entry(root, width=40)
name_entry.pack(pady=10)

# Create a button to trigger the greeting
greet_button = tk.Button(root, text="Greet", command=greet)
greet_button.pack(pady=10)

# Create a label to display the greeting
greeting_label = tk.Label(root, text="")
greeting_label.pack(pady=20)

# Start the Tkinter event loop
root.mainloop()
