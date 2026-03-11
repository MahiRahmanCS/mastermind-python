from itertools import product
from core2 import random_code, generate_guess, narrow_down_codes, is_win, game_over

colours = ['R', 'G', 'B', 'Y', 'W', 'K']

def main():
    print("Welcome to Mastermind! The program will try to guess your code.")
    print("Think of a 4-color code using: R, G, B, Y, W, K")
    print("After each guess, provide feedback as 'correct_position-correct_colour'")
    print("Example: 2-1 means 2 pegs in correct position, 1 correct color in wrong position\n")

    possible_codes = [list(code) for code in product(colours, repeat=4)]
    attempts = 10

    for attempt in range(attempts):
        guess = generate_guess(possible_codes)
        print(f"Attempt {attempt + 1}: Program guesses {guess}")

        # Keep asking until feedback is valid
        while True:
            try:
                feedback = input("Enter feedback (correct position - correct colour): ").strip()
                correct_position, correct_colour = map(int, feedback.split('-'))

                # Basic bounds check
                if not (0 <= correct_position <= 4 and 0 <= correct_colour <= 4):
                    print("Values must be between 0 and 4. Try again.")
                    continue
                if correct_position + correct_colour > 4:
                    print("Invalid feedback: total cannot exceed 4. Try again.")
                    continue

                if is_win((correct_position, correct_colour)):
                    print("The program guessed the code correctly!")
                    return

                new_possible_codes = narrow_down_codes(
                    possible_codes, guess, (correct_position, correct_colour)
                )

                if not new_possible_codes:
                    print("That feedback is inconsistent with earlier answers. Try again.")
                    continue

                possible_codes = new_possible_codes
                break  # valid feedback, move to next attempt

            except ValueError:
                print("Invalid input format. Please use format: 0-0 (e.g., 2-1)")
                continue

    print("The program failed to guess the code within the allowed attempts.")


if __name__ == "__main__":
    main()