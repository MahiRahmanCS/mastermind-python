# for the system to guess coulours from and user has the 4 pegs

import random
from itertools import product

#program guesses 4 colours from 6 coulours and tries to guess a sequence of 4 pegs
def generate_code():
    colours = ['R', 'G', 'B', 'Y', 'W', 'K'] # R=Red, G=Green, B=Blue, Y=Yellow, W=White, K=Black
    code = []
    for i in range(4):
        code.append(random.choice(colours))
    return code

# the user will then give a code such as 2-1 meaning 2 correct colours in the correct position and 1 correct colour in the wrong position. 
# the program will then use this information to narrow down the possible codes and make another guess. This process continues until the program guesses the correct code or runs out of attempts. max attemps program has is 10  
def get_feedback(guess, code):
    correct_position = 0
    correct_colour = 0
    code_copy = list(code)
    guess_copy = list(guess)        
    
    # First pass: count correct positions
    for i in range(4):
        if guess[i] == code[i]:
            correct_position += 1
            code_copy[i] = None
            guess_copy[i] = None
    
    # Second pass: count correct colors in wrong positions
    for i in range(4):
        if guess_copy[i] is not None and guess_copy[i] in code_copy:
            correct_colour += 1
            code_copy[code_copy.index(guess_copy[i])] = None
    
    return correct_position, correct_colour

# make a create guess function that generates a random guess and then uses the feedback to narrow down the possible codes
def create_guess(possible_codes):
    return random.choice(possible_codes)

def main():
    colours = ['R', 'G', 'B', 'Y', 'W', 'K']
    # Generate ALL possible codes (6^4 = 1296 combinations)
    possible_codes = [list(code) for code in product(colours, repeat=4)]
    attempts = 10
    
    print("Welcome to Mastermind! The program will try to guess your code.")
    print("Think of a 4-color code using: R, G, B, Y, W, K")
    print("After each guess, provide feedback as 'correct_position-correct_color'")
    print("Example: 2-1 means 2 pegs in correct position, 1 correct color in wrong position\n")
    
    for attempt in range(attempts):
        guess = create_guess(possible_codes)
        print(f"Attempt {attempt + 1}: Program guesses {guess}")
        
        try:
            feedback = input("Enter feedback (correct position - correct colour): ")
            correct_position, correct_colour = map(int, feedback.split('-'))
            
            if correct_position == 4:
                print("The program guessed the code correctly!")
                return
            
            # Narrow down possible codes based on feedback
            possible_codes = [code for code in possible_codes if get_feedback(guess, code) == (correct_position, correct_colour)]
            
            if not possible_codes:
                print("Invalid feedback. No possible codes match the feedback provided.")
                print("Please make sure your feedback is accurate based on your secret code.")
                return
        except ValueError:
            print("Invalid input format. Please use format: 0-0 (e.g., 2-1)")
            return
    
    print("The program failed to guess the code within 10 attempts.")

if __name__ == "__main__":
    main()



    #rgkr