import tkinter as tk
from tkinter import messagebox
import random

def check_guess():
    try:
        user_input = int(entry_guess.get())
        numbers = list(range(1, 6))
        computer_choice = random.choice(numbers)

        if user_input == computer_choice:
            messagebox.showinfo("Result", f"YOU GUESSED IT WOW!\nThe number was {computer_choice}")
        else:
            messagebox.showinfo("Result", f"Sorry, you didn't guess it.\nIt was {computer_choice}")

    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter a number between 1 and 5.")

window = tk.Tk()
window.title("Paise de de bhai")

label_instruction = tk.Label(window, text="Enter your guess (1-5):")
label_instruction.pack()
entry_guess = tk.Entry(window)
entry_guess.pack()
btn_guess = tk.Button(window, text="Guess", command=check_guess)
btn_guess.pack()
window.mainloop()
