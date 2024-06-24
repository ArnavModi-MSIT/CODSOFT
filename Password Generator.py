import tkinter as tk
from tkinter import ttk
import random
import string

root = tk.Tk()
root.title("Password Generator")

style = ttk.Style()
style.configure("TLabel", font=("Helvetica", 14), foreground="blue")
style.configure("TButton", font=("Helvetica", 12), foreground="Black", background="blue", padding=5)
style.map("TButton", background=[("active", "darkblue")])

mainframe = ttk.Frame(root, padding="10 10 10 10", style="TFrame", relief="sunken")
mainframe.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))

ttk.Label(mainframe, text="Password", justify="center", style="TLabel").grid(column=0, row=0, pady=10)
entry = ttk.Entry(mainframe, width=20, font=("Helvetica", 14))
entry.grid(column=1, row=0, sticky=(tk.W), pady=10, columnspan=2)

ttk.Label(mainframe, text="Length", justify="center", style="TLabel").grid(column=0, row=1, pady=10)
length_entry = ttk.Entry(mainframe, width=5, font=("Helvetica", 14))
length_entry.grid(column=1, row=1, sticky=(tk.W), pady=10, columnspan=2)

def generate_password(length, chars):
    return ''.join(random.choice(chars) for _ in range(length))

def get_length():
    try:
        return int(length_entry.get())
    except ValueError:
        return 8

def low_password():
    length = get_length()
    password = generate_password(length, string.ascii_lowercase)
    entry.delete(0, tk.END)
    entry.insert(0, password)

def medium_password():
    length = get_length()
    password = generate_password(length, string.ascii_letters + string.digits)
    entry.delete(0, tk.END)
    entry.insert(0, password)

def strong_password():
    length = get_length()
    password = generate_password(length, string.ascii_letters + string.digits + string.punctuation)
    entry.delete(0, tk.END)
    entry.insert(0, password)

ttk.Button(mainframe, text="Low", command=low_password, style="TButton").grid(column=0, row=2, sticky=tk.W, pady=5)
ttk.Button(mainframe, text="Medium", command=medium_password, style="TButton").grid(column=1, row=2, sticky=tk.W, pady=5)
ttk.Button(mainframe, text="Strong", command=strong_password, style="TButton").grid(column=2, row=2, sticky=tk.W, pady=5)

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
mainframe.columnconfigure(0, weight=1)
mainframe.columnconfigure(1, weight=1)
mainframe.columnconfigure(2, weight=1)

root.mainloop()
