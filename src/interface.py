import tkinter as tk
import customtkinter

from .core import MastermindGame, colours

# Set dark mode FIRST, before creating any widgets
customtkinter.set_appearance_mode("dark")

root = customtkinter.CTk()
root.geometry("800x500")
root.title("Mastermind")

# game engine
game = MastermindGame()

# variables for the four guess slots
guess_vars = [tk.StringVar(value=colours[0]) for _ in range(4)]

# --- layout -------------------------------------------------------------
input_frame = customtkinter.CTkFrame(root)
input_frame.pack(pady=20)

for i in range(4):
    opt = customtkinter.CTkOptionMenu(
        input_frame,
        values=colours,
        variable=guess_vars[i],
        width=120
    )
    opt.grid(row=0, column=i, padx=5)

submit_btn = customtkinter.CTkButton(root, text="Guess", command=lambda: submit_guess())
submit_btn.pack(pady=(10, 5))

restart_btn = customtkinter.CTkButton(root, text="Restart", command=lambda: restart(), state="disabled")
restart_btn.pack(pady=(0, 10))

history_box = customtkinter.CTkTextbox(root, width=700, height=200, state="disabled")
history_box.pack(pady=10)

status_label = customtkinter.CTkLabel(root, text="")
status_label.pack()

# --- callback definitions ---------------------------------------------
def submit_guess():
    guess = [var.get() for var in guess_vars]
    black, white = game.evaluate_guess(guess)

    history_box.configure(state="normal")
    history_box.insert("end", f"Guess {len(game.attempts)}: {guess} -> black={black}, white={white}\n")
    history_box.configure(state="disabled")

    if game.is_solved():
        status_label.configure(text="🎉 Congratulations! You solved the code.")
        submit_btn.configure(state="disabled")
        restart_btn.configure(state="normal")


def restart():
    game.reset()
    history_box.configure(state="normal")
    history_box.delete("1.0", "end")
    history_box.configure(state="disabled")
    status_label.configure(text="")
    submit_btn.configure(state="normal")
    restart_btn.configure(state="disabled")

# start the GUI event loop
root.mainloop()
