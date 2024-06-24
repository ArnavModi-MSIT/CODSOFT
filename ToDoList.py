import tkinter as tk
from tkinter import ttk
import pickle

def add_task():
    task = entry.get()
    if task:
        task_listbox.insert(tk.END, task)

def delete_task():
    selected_task_index = task_listbox.curselection()
    if selected_task_index:
        task_listbox.delete(selected_task_index)

def delete_all_tasks():
    task_listbox.delete(0, tk.END)

def mark_important():
    selected_task_index = task_listbox.curselection()
    if selected_task_index:
        task_listbox.itemconfig(selected_task_index, bg="yellow")

def save_tasks():
    tasks = task_listbox.get(0, tk.END)
    with open('tasks.txt', 'wb') as f:
        pickle.dump(tasks, f)

def load_tasks():
    try:
        with open('tasks.txt', 'rb') as f:
            tasks = pickle.load(f)
            for task in tasks:
                task_listbox.insert(tk.END, task)
    except FileNotFoundError:
        pass

root = tk.Tk()
root.title("To-Do List")

style = ttk.Style()
style.configure("TLabel", font=("Helvetica", 20), foreground="blue")
style.configure("TButton", font=("Helvetica", 12), foreground="Black", background="blue")
style.map("TButton", background=[("active", "darkblue")])

mainframe = ttk.Frame(root, padding="10 10 10 10", width=500, height=250, style="TFrame")
mainframe.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))

ttk.Label(mainframe, text="Task List", style="TLabel", justify="center").grid(column=0, row=0, pady=10, columnspan=2)

entry = ttk.Entry(mainframe, width=20)
entry.grid(column=0, row=1, sticky=(tk.W), pady=10, columnspan=2)

task_listbox = tk.Listbox(mainframe, height=10, bg="lightgrey", selectbackground="blue", selectforeground="white")
task_listbox.grid(column=1, row=2, rowspan=4, sticky=(tk.N, tk.E, tk.S), padx=10)

ttk.Button(mainframe, text="Add Task", command=add_task, style="TButton").grid(column=0, row=2, sticky=tk.W, pady=5)
ttk.Button(mainframe, text="Delete Task", command=delete_task, style="TButton").grid(column=0, row=3, sticky=tk.W, pady=5)
ttk.Button(mainframe, text="Delete All Tasks", command=delete_all_tasks, style="TButton").grid(column=0, row=4, sticky=tk.W, pady=5)
ttk.Button(mainframe, text="Mark Important", command=mark_important, style="TButton").grid(column=0, row=5, sticky=tk.W, pady=5)
ttk.Button(mainframe, text="Save Tasks", command=save_tasks, style="TButton").grid(column=0, row=6, sticky=tk.W, pady=5)
ttk.Button(mainframe, text="Load Tasks", command=load_tasks, style="TButton").grid(column=1, row=6, sticky=tk.W, pady=5)

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
mainframe.columnconfigure(0, weight=1)
mainframe.columnconfigure(1, weight=1)

load_tasks()
root.mainloop()
