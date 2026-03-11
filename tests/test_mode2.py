#pytest for core2.py
import pytest
from core2 import random_code, generate_guess, narrow_down_codes, is_win, game_over

# Test Exact Matches Only
def test_exact_matches_only():
    secret = ["R", "G", "B", "Y"]

    guess = ["R", "G", "B", "Y"]
    assert is_win(secret, guess) == True

    guess = ["R", "G", "B", "K"]
    assert is_win(secret, guess) == False


# Test Partial Matches Only
def test_partial_matches_only():
    secret = ["R", "G", "B", "Y"]

    guess = ["G", "B", "Y", "R"]    
    assert is_win(secret, guess) == False

# Test No Matches
# This test checks that the function correctly identifies when there are no matches between the secret code and the guess.
# It ensures that the function does not falsely identify any matches when there are none, which is crucial for the integrity of the game logic.
def test_no_matches():
    secret = ["R", "R", "R", "R"]
    guess = ["G", "G", "G", "G"]    


    assert is_win(secret, guess) == False

# Test Mixed Exact and Partial Matches
def test_mixed_exact_and_partial():
    secret = ["R", "G", "B", "R"]
    guess = ["R", "R", "G", "B"]

    assert is_win(secret, guess) == False        



