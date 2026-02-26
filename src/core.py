# mode 1
import random

ALLOWED_COLOURS = ["R", "G", "B", "Y", "W", "K"]

def random_code():
    return [random.choice(ALLOWED_COLOURS) for i in range(4)]

def validate_guess(guess):
    if len(guess) != 4:
        return False
    for slot in guess:
        if slot not in ALLOWED_COLOURS:
            return False
    return True

def score_guess(secret, guess):
    exact_matches = 0
    partial_matches = 0
    
    # Create copies so we can mark matched slots
    secret_copy = secret.copy()
    guess_copy = list(guess)
    
    # First pass: exact matches
    for i in range(4):
        if guess_copy[i] == secret_copy[i]:
            exact_matches += 1
            secret_copy[i] = None  # mark as matched
            guess_copy[i] = None
    
    # Second pass: partial matches
    for i in range(4):
        if guess_copy[i] is not None and guess_copy[i] in secret_copy:
            partial_matches += 1
            secret_index = secret_copy.index(guess_copy[i])
            secret_copy[secret_index] = None  # mark as used
    
    return exact_matches, partial_matches


def is_win(exact_matches):
    return exact_matches == 4


def game_over(guess_count):
    return guess_count >= 10