import tkinter as tk
from tkinter import messagebox

def calculate_total_cost():
    try:
        bulb_cost = float(bulb_cost_entry.get())
        energy_cost = float(energy_cost_entry.get())
        total_cost = bulb_cost + energy_cost
        result_label.config(text=f"Total Cost: ${total_cost:.2f}")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numeric values for costs.")

# Create the main application window
root = tk.Tk()
root.title("Lightbulb Cost Calculator")
root.geometry("300x200")

# Create and place widgets
bulb_cost_label = tk.Label(root, text="Cost of Lightbulb ($):")
bulb_cost_label.pack(pady=5)

bulb_cost_entry = tk.Entry(root)
bulb_cost_entry.pack(pady=5)

energy_cost_label = tk.Label(root, text="Cost of Energy ($):")
energy_cost_label.pack(pady=5)

energy_cost_entry = tk.Entry(root)
energy_cost_entry.pack(pady=5)

calculate_button = tk.Button(root, text="Calculate Total Cost", command=calculate_total_cost)
calculate_button.pack(pady=10)

result_label = tk.Label(root, text="Total Cost: $0.00", font=("Arial", 12))
result_label.pack(pady=10)

# Run the application
root.mainloop()
