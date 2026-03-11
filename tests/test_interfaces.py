import mode1
import mode2
import core

# reuse the colour list that lives in core/mode1 rather than
# re‑declaring it here
colours = mode1.colours  # core.colours would work just as well

# state used for mode‑1 (mode‑2 has its own main)
game_code = None
current_attempt = 0
max_attempts = 10
current_mode = None


def select_mode():
    """Ask the player which mode to run; does **not** start the game."""
    global current_mode
    while True:
        print("Select Mode:")
        print("1: Mode 1: You Guess")
        print("2: Mode 2: Computer Guesses")
        try:
            mode = int(input("Enter 1 or 2: "))
            if mode in (1, 2):
                current_mode = mode
                return
        except ValueError:
            pass
        print("Invalid choice. Please enter 1 or 2.")


def restart():
    """Initialise/reset state for a new mode‑1 game."""
    global game_code, current_attempt

    if current_mode == 1:
        # use the helper defined in mode1.py
        game_code = mode1.generate_code()
        current_attempt = 0
        print("\n--- New Game Started ---")
    else:
        # nothing to do here; mode2.main() will handle its own startup
        print("\n--- New Game Started ---")
        print("Think of a 4-colour code. Computer will start guessing!")


def submit_guess():
    """Mode‑1 only: prompt the human for a guess and score it."""
    global current_attempt

    if current_mode != 1:
        return False

    while True:
        guess_input = input(
            "Enter your guess (4 colours separated by spaces, e.g., R G B Y): "
        ).strip().upper()
        guess = guess_input.split()

        if len(guess) != 4:
            print("❌ Invalid guess. Please enter exactly 4 colours.")
            continue
        if not all(c in colours for c in guess):
            print(f"❌ Invalid colours. Available colours: {', '.join(colours)}")
            continue
        if not core.validate_guess(guess):
            print("❌ Invalid guess. Please select four valid colours.")
            continue
        break

    exact_matches, partial_matches = core.score_guess(game_code, guess)  # type: ignore[arg-type]
    current_attempt += 1

    print(
        f"Attempt {current_attempt}: {guess} -> "
        f"Correct Position: {exact_matches}, Correct Colour: {partial_matches}"
    )

    if core.is_win(exact_matches):
        print("🎉 Congratulations! You guessed the code!")
        return True
    if core.game_over(current_attempt):
        print(f"❌ Game Over! The code was: {game_code}")
        return True
    return False


def main():
    """Command‑line entry point; selects a mode and delegates as needed."""
    print("Welcome to Mastermind!")
    print(f"Available colours: {', '.join(colours)}")

    while True:
        select_mode()
        if current_mode == 2:
            # hand control over to mode2; it has its own loop and feedback
            mode2.main()
        else:
            restart()
            finished = False
            while not finished:
                finished = submit_guess()

        # ask whether to play again regardless of mode
        while True:
            play_again = input("Play again? (y/n): ").strip().lower()
            if play_again in ("y", "n"):
                break
            print("Please enter 'y' or 'n'.")
        if play_again == "n":
            print("Thanks for playing!")
            return


if __name__ == "__main__":
    main()