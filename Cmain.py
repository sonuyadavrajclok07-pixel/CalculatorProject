import tkinter as tk
from tkinter import messagebox

def calculate_gst():
    try:
        amount = float(entry_amount.get())
        percentage = float(entry_percentage.get())
        gst_amount = (amount * percentage) / 100
        total_amount = amount + gst_amount
        label_result.config(text=f"GST: {gst_amount:.2f}\nTotal: {total_amount:.2f}", fg="#00FF00")
    except ValueError:
        messagebox.showerror("Error", "Sahi number bhariye")

root = tk.Tk()
root.title("GST Calculator")
root.geometry("350x500")
root.configure(bg="#121212")

tk.Label(root, text="Calculator App", font=("Arial", 20), bg="#121212", fg="#ff9500").pack(pady=20)
entry_amount = tk.Entry(root, font=("Arial", 14))
entry_amount.pack(pady=10)
entry_percentage = tk.Entry(root, font=("Arial", 14))
entry_percentage.pack(pady=10)

btn_calc = tk.Button(root, text="CALCULATE", command=calculate_gst, bg="#ff9500", fg="white")
btn_calc.pack(pady=30)

label_result = tk.Label(root, text="", bg="#121212", font=("Arial", 16))
label_result.pack(pady=10)

root.mainloop()
