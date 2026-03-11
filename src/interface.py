"""
Interface (menu dispatcher) for the Mastermind game.
Provides a menu to select between two game modes:
Run it directly:  python src/interface.py
"""

# Import game constants and mode entry points
from core import ALLOWED_COLOURS
from cli import main as mode1_main      # Mode 1 — You guess
from cli2 import main as mode2_main     # Mode 2 — Computer guesses


def _ask_mode() -> int:
    # Repeatedly prompt user until they select a valid mode (1 or 2)
    while True:
        print("Select Mode:")
        print("1: Mode 1 — You Guess")
        print("2: Mode 2 — Computer Guesses")
        choice = input("Enter 1 or 2: ").strip()
        if choice in ("1", "2"):
            return int(choice)
        print("Invalid choice. Please enter 1 or 2.")


def _ask_play_again() -> bool:
    # Repeatedly prompt user for yes/no until they give a valid response
    while True:
        ans = input("Play again? (y/n): ").strip().lower()
        if ans in ("y", "n"):
            return ans == "y"
        print("Please enter 'y' or 'n'.")


def main() -> None:
    # Display welcome message and available colours
    print("Welcome to Mastermind!")
    try:
        print(f"Allowed colours: {', '.join(ALLOWED_COLOURS)}\n")
    except Exception:
        # If ALLOWED_COLOURS ever changes or is missing, don't crash the menu.
        pass

    # Main game loop: keep playing until user chooses to exit
    while True:
        mode = _ask_mode()

        # Launch the selected game mode
        if mode == 1:
            # Mode 1: player guesses the secret code
            mode1_main()
        else:
            # Mode 2: computer guesses; user provides feedback 
            mode2_main()

        # Ask if user wants to play again
        if not _ask_play_again():
            print("Thanks for playing!")
            return


if __name__ == "__main__":
    main()