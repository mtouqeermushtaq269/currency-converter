import requests
import tkinter as tk
from tkinter import ttk
# create the Tkinter window
root = tk.Tk()
root.title(" Currency Converter")
# set background color
root.geometry("300x400")
root.configure(bg="dark blue")
style = ttk.Style()
style.theme_create("my_style", parent="alt", settings={
    "TLabel": {
        "configure": {"foreground": "red", "background": "gray", "font": ("Arial", 16)}
    },
    "TEntry": {
        "configure": {"foreground": "red", "background": "gray", "font": ("Arial", 16)}
    },
    "TCombobox": {
        "configure": {"foreground": "red", "background": "light green", "font": ("Arial", 16)}
    },
    "TButton": {
        "configure": {"foreground": "green", "background": "light green", "font": ("Arial", 16)}
    }
})
style.theme_use("my_style")
# get the currency exchange rates from the internet
response = requests.get('https://api.exchangerate-api.com/v4/latest/USD')
rates = response.json()['rates']
# create the available currencies list
available_currencies = list(rates.keys())
amount_label = ttk.Label(root, text="Enter cash that you want to change:", style="TLabel")
amount_label.pack(pady=15)
amount_entry = ttk.Entry(root)
amount_entry.pack()
from_label = ttk.Label(root, text="From:", style="TLabel")
from_label.pack(pady=8)
from_menu = ttk.Combobox(root, values=available_currencies, state="readonly")
from_menu.pack()
to_label = ttk.Label(root, text="To:", style="TLabel")
to_label.pack(pady=8)
to_menu = ttk.Combobox(root, values=available_currencies, state="readonly")
to_menu.pack()
result_label = ttk.Label(root, text="", style="TLabel")
result_label.pack(pady=15)
# create the conversion function
def convert_currency():
    try:
        amount = float(amount_entry.get())
        currency_from = from_menu.get()
        currency_to = to_menu.get()
        # convert the currency
        result = amount * rates[currency_to] / rates[currency_from]
        result_label.configure(text=f"{amount:.2f} {currency_from} is equal to {result:.2f} {currency_to}")
    except ValueError:
        result_label.configure(text="Invalid input")
def reset_values():
    amount_entry.delete(0, tk.END)
    from_menu.current(0)
    to_menu.current(0)
    result_label.configure(text="")
# create  buttons
button_frame = ttk.Frame(root)
button_frame.pack(pady=20)
convert_button = ttk.Button(button_frame, text="CONVERT", command=convert_currency, style="TButton")
convert_button.pack(side=tk.LEFT, padx=10)
reset_button = ttk.Button(button_frame, text="RESET", command=reset_values, style="TButton")
reset_button.pack(side=tk.LEFT, padx=10)
root.mainloop()
