For Each Entry Include
Name: Mahi Rahman
Task –  create an interface layer for the Mastermind game, separating user interaction (prompts, formatting, display) from logic modules like core.py and mode2.py.
Prompt – 
    Write a Python module called interfaces.py for a Mastermind game.
    It must contain functions that handle all user‑interface responsibilities such as:

    formatted printing
    showing guesses and feedback
    asking for mode selection
    asking for user guesses
    asking for feedback in mode 2

    No game logic should be inside this module.

AI Output (Summary) –
     def display_welcome():
         print("Welcome to Mastermind!")
    def prompt_mode():
        return input("Select mode (1: You guess, 2: Computer guesses): ")
    def prompt_guess():
        return input("Enter your guess: ")
    def show_feedback(exact, partial):
        print(f"Correct Position: {exact}, Correct Colour: {partial}")

Evaluation – 
        Correct - UI‑only functions, separation from logic, Clear naming
        incorrect/incomplete -No validation inside interface prompts, No structured return types, Missing error‑display messages

Refinement – I refined the next prompt to improve consistency and future‑proofing

Testing – missing error display messages may cause confusion to users on whats wrong

Learning – AI needs explicit instructions for data validation


Sequence Diagrams
I will provide a brief overview in Thursday’s lecture (along with automated testing).
