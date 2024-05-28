import tkinter as tk


def calculate():
    try:
        km = float(km_entry.get())
    except ValueError:
        miles_label.config(text="Enter a number")
    else:
        miles = round((km / 1.60934), 3)
        miles_label.config(text=f"{miles} miles")


root = tk.Tk()
root.title("Kilometers to Miles")
root.geometry("500x250")

km_entry_label = tk.Label(root, text="Enter kilometers to convert:")
km_entry_label.pack(pady=10)

km_entry = tk.Entry(root, width=10, justify=tk.CENTER)
km_entry.pack()

calculate_button = tk.Button(root, text="Convert", command=calculate)
calculate_button.pack(pady=10)

miles_label = tk.Label(root, text="")
miles_label.pack(pady=20)

root.mainloop()
