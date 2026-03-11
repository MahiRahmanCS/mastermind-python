# src/interface.py
from __future__ import annotations

# Menu/dispatcher for the two CLI entry points.
# Uses relative imports so it runs cleanly with: `python -m src.interface`

from . import core2, core, cli, cli2      # now the relative imports in
                                       # mode1/mode2 succeed

colours = cli2.colours   # or core.colours; only used for display


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
    print(f"Allowed colours: {', '.join(ALLOWED_COLOURS)}\n")

    while True:
        mode = _ask_mode()

        if mode == 1:
            # Mode 1: player guesses the secret code
            mode1_main()
        else:
            # Mode 2: computer guesses; you provide feedback (e.g., "2-1")
            mode2_main()

        if not _ask_play_again():
            print("Thanks for playing!")
            return


if __name__ == "__main__":
    main()