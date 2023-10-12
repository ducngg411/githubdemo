import tkinter as tk

def generate_receipt():
    name = name_entry.get()
    total_fee = 0
    selected_items = []

    for workshop, (var, fee) in workshop_vars.items():
        if var.get():
            total_fee += fee
            selected_items.append(workshop)

    receipt_label.config(text=f"Receipt for {name}\n\nSelected Workshops/Sessions:\n- " + "\n- ".join(selected_items) + f"\n\nTotal Fee: ${total_fee}")

# Create the main window
window = tk.Tk()
window.title("Event Registration")

# Create widgets
tk.Label(window, text="Event Registration").pack()

tk.Label(window, text="Name:").pack()
name_entry = tk.Entry(window)
name_entry.pack()

workshop_vars = {
    "Workshop A - Python Basics ($50)": (tk.BooleanVar(), 50),
    "Workshop B - Machine Learning ($100)": (tk.BooleanVar(), 100),
    "Workshop C - Web Development ($75)": (tk.BooleanVar(), 75),
    "Workshop D - Data Visualization ($60)": (tk.BooleanVar(), 60),
}

for workshop, (var, fee) in workshop_vars.items():
    tk.Checkbutton(window, text=workshop, variable=var).pack()

generate_button = tk.Button(window, text="Generate Receipt", command=generate_receipt)
generate_button.pack()

receipt_label = tk.Label(window, text="")
receipt_label.pack()

# Start the GUI event loop
window.mainloop()
