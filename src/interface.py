# src/interface.py
from __future__ import annotations

# Menu/dispatcher for the two CLI entry points.
# Run it with:  python -m src.interface   (or simply: python -m src)

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
            mode1_main()
        else:
            mode2_main()

        if not _ask_play_again():
            print("Thanks for playing!")
            return


if __name__ == "__main__":
    # You can still run: python -m src.interface
    # This guard is harmless and keeps symmetry if someone runs this file directly.
    main()