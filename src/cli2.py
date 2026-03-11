from src.core2 import random_code, validate_guess, score_guess, is_win, game_over
from mode2 import get_feedback, generate_guess, narrow_down_codes

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
            feedback_input = input("Enter feedback (correct position - correct colour): ")
            correct_position, correct_colour = map(int, feedback_input.split('-'))
            feedback = (correct_position, correct_colour)
            
            if is_win(feedback):
                print("The program guessed the code correctly!")
                return
            
            possible_codes = narrow_down_codes(possible_codes, guess, feedback)
        except ValueError:
            print("Invalid feedback format. Please enter as 'correct_position-correct_colour'.")
            continue
    
    print("Game over! The program couldn't guess the code within the attempts.")