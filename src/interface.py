"""
Interface (menu dispatcher) for the Mastermind game.

This version is for the "normal" (non-package) setup.
Run it directly:  python src/interface.py
"""

from core import ALLOWED_COLOURS
from cli import main as mode1_main      # Mode 1 — You guess
from cli2 import main as mode2_main     # Mode 2 — Computer guesses


def _ask_mode() -> int:
    while True:
        print("Select Mode:")
        print("1: Mode 1 — You Guess")
        print("2: Mode 2 — Computer Guesses")
        choice = input("Enter 1 or 2: ").strip()
        if choice in ("1", "2"):
            return int(choice)
        print("Invalid choice. Please enter 1 or 2.")


def _ask_play_again() -> bool:
    while True:
        ans = input("Play again? (y/n): ").strip().lower()
        if ans in ("y", "n"):
            return ans == "y"
        print("Please enter 'y' or 'n'.")


def main() -> None:
    print("Welcome to Mastermind!")
    try:
        print(f"Allowed colours: {', '.join(ALLOWED_COLOURS)}\n")
    except Exception:
        # If ALLOWED_COLOURS ever changes or is missing, don't crash the menu.
        pass

    while True:
        mode = _ask_mode()

        if mode == 1:
            # Mode 1: player guesses the secret code
            mode1_main()
        else:
            # Mode 2: computer guesses; user provides feedback (e.g., "2-1")
            mode2_main()

        if not _ask_play_again():
            print("Thanks for playing!")
            return


if __name__ == "__main__":
    main()