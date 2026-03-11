from itertools import product
from core2 import random_code, generate_guess, narrow_down_codes, is_win, game_over


def main():
    print("Welcome to Mastermind! The program will try to guess your code.")
    print("Think of a 4-color code using: R, G, B, Y, W, K")
    print("After each guess, provide feedback as 'correct_position-correct_colour'")
    print("Example: 2-1 means 2 pegs in correct position, 1 correct color in wrong position\n")

    colours = ['R', 'G', 'B', 'Y', 'W', 'K']
    possible_codes = [list(code) for code in product(colours, repeat=4)]
    attempts = 10

    for attempt in range(attempts):
        guess = generate_guess(possible_codes)
        print(f"Attempt {attempt + 1}: Program guesses {guess}")

        try:
            feedback = input("Enter feedback (correct position - correct colour): ")
            correct_position, correct_colour = map(int, feedback.split('-'))

            if is_win((correct_position, correct_colour)):
                print("The program guessed the code correctly!")
                return

            possible_codes = narrow_down_codes(possible_codes, guess, (correct_position, correct_colour))

            if not possible_codes:
                print("Invalid feedback. No possible codes match the feedback provided.")
                print("Please make sure your feedback is accurate based on your secret code.")
                return

        except ValueError:
            print("Invalid input format. Please use format: 0-0 (e.g., 2-1)")
            return

    print("The program failed to guess the code within the allowed attempts.")


if __name__ == "__main__":
    main()