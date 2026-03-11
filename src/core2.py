import random

from mode2 import get_feedback

ALLOWED_COLOURS = ["R", "G", "B", "Y", "W", "K"]

def random_code():
    return [random.choice(ALLOWED_COLOURS) for _ in range(4)]

# create a function that generates a guess and then uses the feedback from the user to narrow down the possible codes
from itertools import product

def generate_guess(possible_codes):
    return random.choice(possible_codes)

#create a function that takes the user's feedback and narrows down the possible codes based on the feedback
def narrow_down_codes(possible_codes, guess, feedback):
    correct_position, correct_colour = feedback
    new_possible_codes = []
    
    for code in possible_codes:
        if get_feedback(guess, code) == (correct_position, correct_colour):
            new_possible_codes.append(code)
    
    return new_possible_codes

# create a function that ends the game if the program guesses right 
def is_win(feedback):
    correct_position, _ = feedback
    return correct_position == 4

# create a function that ends the game if the program runs out of attempts or if the user gives invalid feedback
def game_over(attempts, max_attempts):
    return attempts >= max_attempts

    