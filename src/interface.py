#
# `mode1` and `mode2` live in the same package (`src`), and both of them
# perform relative imports of `core`.  if you execute this file directly
# the package machinery isn’t set up, so the relative imports blow up.
# the little bootstrap below fixes that.
if __name__ == "__main__" and __package__ is None:
    import sys, os

    base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    sys.path.insert(0, base)          # make the parent of `src` importable
    __package__ = "src"               # behave as if we were imported
                                     # as `python -m src.interface`

from . import core2, core       # now the relative imports in
                                       # mode1/mode2 succeed

colours = core.colours   # or core.colours; only used for display


def _ask_mode() -> int:
    while True:
        print("Select Mode:")
        print("1: Mode 1: You Guess")
        print("2: Mode 2: Computer Guesses")
        try:
            m = int(input("Enter 1 or 2: "))
            if m in (1, 2):
                return m
        except ValueError:
            pass
        print("Invalid choice. Please enter 1 or 2.")


def _ask_play_again() -> bool:
    while True:
        ans = input("Play again? (y/n): ").strip().lower()
        if ans in ("y", "n"):
            return ans == "y"
        print("Please enter 'y' or 'n'.")


def main() -> None:
    """Command–line driver.  The only job of this module is to let the
    user pick a mode and then hand control off to the appropriate
    module; it does *not* contain the mode‑2 algorithm and it only uses
    one tiny helper from mode1."""
    print("Welcome to Mastermind!")
    print(f"Available colours: {', '.join(colours)}")

    while True:
        core = _ask_mode()

        if core == 1:
            # mode‑1 logic lives here because mode1.py has no entry point;
            # the only function we call from mode1 is generate_code().
            code = core.generate_code()
            attempts = 0
            while True:
                attempts += 1
                guess = (
                    input(
                        "Enter your guess (4 colours separated by spaces, "
                        "e.g., R G B Y): "
                    )
                    .strip()
                    .upper()
                    .split()
                )
                if len(guess) != 4 or not all(c in colours for c in guess):
                    print("❌ Invalid guess. Available colours:", ", ".join(colours))
                    attempts -= 1
                    continue
                if not core.validate_guess(guess):
                    print("❌ Invalid guess. Please select four valid colours.")
                    attempts -= 1
                    continue

                exact, partial = core.score_guess(code, guess)  # type: ignore[arg-type]
                print(
                    f"Attempt {attempts}: {guess} -> "
                    f"Correct Position: {exact}, Correct Colour: {partial}"
                )

                if core.is_win(exact):
                    print("🎉 Congratulations! You guessed the code!")
                    break
                if core.game_over(attempts):
                    print(f"❌ Game Over! The code was: {code}")
                    break

        else:  # core == 2
            # delegate completely; mode2.main() contains the whole loop.
            core2.main()

        if not _ask_play_again():
            print("Thanks for playing!")
            return


if __name__ == "__main__":
    main()