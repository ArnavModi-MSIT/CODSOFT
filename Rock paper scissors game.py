import tkinter as tk
from tkinter import ttk
import random
root = tk.Tk()
root.title("Rock Paper Scissors Game")
mainframe = ttk.Frame(root, padding="10 10 10 10", width=800, height=400)
mainframe.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))
options = ["rock", "paper", "scissors"]
user_score = 0
computer_score = 0
user_score_label = ttk.Label(mainframe, text="Your Score: 0")
user_score_label.grid(column=0, row=1, sticky=tk.W, pady=5)
computer_score_label = ttk.Label(mainframe, text="Computer Score: 0")
computer_score_label.grid(column=2, row=1, sticky=tk.W, pady=5)
listbox = tk.Listbox(mainframe, height=6)
listbox.grid(column=0, row=2, columnspan=5, padx=10, pady=10, sticky=(tk.W, tk.E))
def play(choice):
    global user_score, computer_score
    computer_choice = random.choice(options)
    if choice == computer_choice:
        result = "DRAW"
    elif (choice == "rock" and computer_choice == "scissors") or \
         (choice == "paper" and computer_choice == "rock") or \
         (choice == "scissors" and computer_choice == "paper"):
        result = "YOU WON"
        user_score += 1
    else:
        result = "YOU LOSE"
        computer_score += 1 
    listbox.insert(tk.END, f"You chose {choice}, computer chose {computer_choice}: {result}")
    user_score_label.config(text=f"Your Score: {user_score}")
    computer_score_label.config(text=f"Computer Score: {computer_score}")
    listbox.yview(tk.END)
def reset_game():
    global user_score, computer_score
    user_score = 0
    computer_score = 0
    user_score_label.config(text="Your Score: 0")
    computer_score_label.config(text="Computer Score: 0")
    listbox.delete(0, tk.END)
ttk.Button(mainframe, text="ROCK", command=lambda: play("rock")).grid(column=0, row=0, sticky=tk.W, pady=5)
ttk.Button(mainframe, text="PAPER", command=lambda: play("paper")).grid(column=1, row=0, sticky=tk.W, pady=5)
ttk.Button(mainframe, text="SCISSORS", command=lambda: play("scissors")).grid(column=2, row=0, sticky=tk.W, pady=5)
ttk.Button(mainframe, text="PLAY AGAIN", command=reset_game).grid(column=1, row=3, pady=10)
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
mainframe.columnconfigure(0, weight=1)
mainframe.columnconfigure(1, weight=1)
mainframe.columnconfigure(2, weight=1)
mainframe.rowconfigure(2, weight=1)
root.mainloop()
