
import tkinter as tk
import customtkinter
from itertools import product


# possible colours for the code and guesses
colours = ["R", "G", "B", "Y", "W", "K"]

# Force dark appearance for the customtkinter widgets before construction
customtkinter.set_appearance_mode("dark")

# main application window
root = customtkinter.CTk()
root.geometry("900x600")
root.title("Mastermind")

# current game mode: 1 = user guesses, 2 = program guesses
current_mode = tk.IntVar(value=1)

# game state variables
game_code = None
possible_codes = [list(code) for code in product(colours, repeat=4)]
current_attempt = 0
max_attempts = 10
current_guess = None

# each slot in the guess row is backed by a StringVar for easy
# reading/updating; initial value set to first colour
guess_vars = [tk.StringVar(value=colours[0]) for _ in range(4)]

# mode selection at the top
mode_frame = customtkinter.CTkFrame(root)
mode_frame.pack(pady=10)

mode_label = customtkinter.CTkLabel(mode_frame, text="Select Mode:", font=("Arial", 12, "bold"))
mode_label.grid(row=0, column=0, padx=5)

mode1_radio = customtkinter.CTkRadioButton(mode_frame, text="Mode 1: You Guess", variable=current_mode, value=1, command=lambda: on_mode_change())
mode1_radio.grid(row=0, column=1, padx=5)

mode2_radio = customtkinter.CTkRadioButton(mode_frame, text="Mode 2: Computer Guesses", variable=current_mode, value=2, command=lambda: on_mode_change())
mode2_radio.grid(row=0, column=2, padx=5)

# frame to hold the option menus for selecting a guess
input_frame = customtkinter.CTkFrame(root)
input_frame.pack(pady=20)

# create four dropdowns for player to choose each colour in the guess
for i in range(4):
    opt = customtkinter.CTkOptionMenu(
        input_frame,
        values=colours,
        variable=guess_vars[i],
        width=120
    )
    opt.grid(row=0, column=i, padx=5)

# button to submit the current guess to game logic
submit_btn = customtkinter.CTkButton(root, text="Guess", command=lambda: submit_guess())
submit_btn.pack(pady=(10, 5))

# feedback input frame for mode 2
feedback_frame = customtkinter.CTkFrame(root)
feedback_frame.pack(pady=5)

feedback_label = customtkinter.CTkLabel(feedback_frame, text="Feedback (position-colour):")
feedback_label.grid(row=0, column=0, padx=5)

feedback_entry = customtkinter.CTkEntry(feedback_frame, width=100)
feedback_entry.grid(row=0, column=1, padx=5)

submit_feedback_btn = customtkinter.CTkButton(feedback_frame, text="Submit Feedback", command=lambda: submit_feedback())
submit_feedback_btn.grid(row=0, column=2, padx=5)

# restart clears the game state; disabled until game ends
restart_btn = customtkinter.CTkButton(root, text="Restart", command=lambda: restart(), state="disabled")
restart_btn.pack(pady=(0, 10))

# read-only text area showing past guesses and feedback
history_box = customtkinter.CTkTextbox(root, width=700, height=200, state="disabled")
history_box.pack(pady=10)

# label used to display end-of-game messages or other status
status_label = customtkinter.CTkLabel(root, text="")
status_label.pack()

def on_mode_change():
    # update UI visibility based on selected mode
    if current_mode.get() == 1:
        # MODE 1: User guesses
        for widget in input_frame.winfo_children():
            widget.grid()
        submit_btn.configure(text="Guess")
        feedback_frame.pack_forget()
        history_box.configure(state="normal")
        history_box.delete("1.0", "end")
        history_box.configure(state="disabled")
        status_label.configure(text="")
        restart()
    else:
        # MODE 2: Computer guesses
        for widget in input_frame.winfo_children():
            widget.grid_remove()
        submit_btn.configure(text="Skip")
        feedback_frame.pack(pady=5)
        history_box.configure(state="normal")
        history_box.delete("1.0", "end")
        history_box.configure(state="disabled")
        status_label.configure(text="Think of a 4-colour code. Computer will start guessing!")
        feedback_entry.delete(0, "end")
        restart()


def submit_guess():
    global current_attempt
    
    if current_mode.get() == 1:
        # MODE 1: User guesses the computer's code using core.py logic
        guess = [var.get() for var in guess_vars]
        
        # validate the guess using core
        if not core.validate_guess(guess):
            status_label.configure(text="❌ Invalid guess. Please select four valid colours.")
            return
        
        # score the guess using core
        exact_matches, partial_matches = core.score_guess(game_code, guess)
        current_attempt += 1

        # show the result in the history text box
        history_box.configure(state="normal")
        history_box.insert("end", f"Attempt {current_attempt}: {guess} -> Correct Position: {exact_matches}, Correct Colour: {partial_matches}\n")
        history_box.see("end")
        history_box.configure(state="disabled")

        # check if player won using core
        if core.is_win(exact_matches):
            status_label.configure(text="🎉 Congratulations! You guessed the code!")
            submit_btn.configure(state="disabled")
            restart_btn.configure(state="normal")
        elif core.game_over(current_attempt):
            status_label.configure(text=f"❌ Game Over! The code was: {game_code}")
            submit_btn.configure(state="disabled")
            restart_btn.configure(state="normal")
    else:
        # MODE 2: Computer is guessing, just skip this round
        pass


def submit_feedback():
    global current_attempt, possible_codes, game_code, current_guess
    
    if current_mode.get() == 2:
        # MODE 2: User provides feedback to computer's guess
        feedback = feedback_entry.get().strip()
        
        try:
            parts = feedback.split('-')
            if len(parts) != 2:
                status_label.configure(text="Invalid format. Use: position-colour (e.g., 2-1)")
                return
            
            correct_position = int(parts[0])
            correct_colour = int(parts[1])
            
            if current_attempt == 0:
                # First attempt: generate initial guess
                current_guess = mode2.create_guess(possible_codes)
                current_attempt += 1
                history_box.configure(state="normal")
                history_box.insert("end", f"Attempt {current_attempt}: Computer guesses {current_guess}\n")
                history_box.see("end")
                history_box.configure(state="disabled")
            else:
                # Narrow down based on feedback from previous guess
                possible_codes = [code for code in possible_codes 
                                 if mode2.get_feedback(current_guess, code) == (correct_position, correct_colour)]
                
                if not possible_codes:
                    status_label.configure(text="❌ Invalid feedback. No codes match!")
                    return
                
                # check if previous guess was correct
                if correct_position == 4:
                    status_label.configure(text="🎉 Computer guessed your code!")
                    submit_feedback_btn.configure(state="disabled")
                    restart_btn.configure(state="normal")
                    return
                
                if current_attempt >= max_attempts:
                    status_label.configure(text="❌ Computer failed to guess within 10 attempts")
                    submit_feedback_btn.configure(state="disabled")
                    restart_btn.configure(state="normal")
                    return
                
                # Make next guess
                current_guess = mode2.create_guess(possible_codes)
                current_attempt += 1
                history_box.configure(state="normal")
                history_box.insert("end", f"Attempt {current_attempt}: Computer guesses {current_guess}\n")
                history_box.see("end")
                history_box.configure(state="disabled")
            
            feedback_entry.delete(0, "end")
        
        except ValueError:
            status_label.configure(text="Invalid input. Use format: 2-1 (position-colour)")


def restart():
    global game_code, current_attempt, possible_codes, current_guess
    
    # reset all variables based on current mode
    if current_mode.get() == 1:
        # MODE 1: Generate a random code using core.py for player to guess
        game_code = core.random_code()
    else:
        # MODE 2: Generate a random code using mode2.py for computer to guess
        game_code = mode2.generate_code()
    
    current_attempt = 0
    current_guess = None
    possible_codes = [list(code) for code in product(colours, repeat=4)]
    
    # clear UI
    history_box.configure(state="normal")
    history_box.delete("1.0", "end")
    history_box.configure(state="disabled")
    status_label.configure(text="")
    feedback_entry.delete(0, "end")
    
    # reset buttons
    if current_mode.get() == 1:
        submit_btn.configure(state="normal")
        feedback_frame.pack_forget()
        for i, var in enumerate(guess_vars):
            var.set(colours[0])
    else:
        submit_feedback_btn.configure(state="normal")
        feedback_frame.pack(pady=5)
        status_label.configure(text="Think of a 4-colour code. Computer will start guessing!")
    
    restart_btn.configure(state="disabled")

# initialize game
on_mode_change()

# start the GUI event loop
root.mainloop()