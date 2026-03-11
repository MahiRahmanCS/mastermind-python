import random
from itertools import product as itertools_product

ALLOWED_COLOURS = ["R", "G", "B", "Y", "W", "K"]

def get_feedback(guess, secret):
    correct_position = sum(g == s for g, s in zip(guess, secret))
    correct_colour = sum(min(guess.count(c), secret.count(c)) for c in set(guess)) - correct_position
    return (correct_position, correct_colour)

def random_code():
    return [random.choice(ALLOWED_COLOURS) for _ in range(4)]

def generate_guess(possible_codes):
    return random.choice(possible_codes)

def narrow_down_codes(possible_codes, guess, feedback):
    return [code for code in possible_codes if get_feedback(guess, code) == feedback]

def is_win(feedback):
    return feedback[0] == 4

def game_over(attempts, max_attempts):
    return attempts >= max_attempts