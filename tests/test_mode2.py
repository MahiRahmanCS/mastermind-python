# pytest for core2.py
import pytest
from src.core2 import random_code, generate_guess, narrow_down_codes, is_win, game_over


# Test random_code function
def test_random_code():
    code = random_code()
    assert len(code) == 4
    for color in code:
        assert color in ["R","G","B","Y","W","K"]


# Test generate_guess function
def test_generate_guess():
    possible_codes = [["R", "G", "B", "Y"], ["G", "B", "Y", "R"]]
    guess = generate_guess(possible_codes)
    assert len(guess) == 4
    for color in guess:
        assert color in ["R","G","B","Y","W","K"]


# Test partial matches only
def test_narrow_down_codes():
    possible_codes = [["R", "G", "B", "Y"], ["G", "B", "Y", "R"], ["R", "R", "R", "R"]]
    guess = ["R", "G", "B", "Y"]
    feedback = (0, 4)  # 0 exact matches, 4 partial matches

    narrowed_codes = narrow_down_codes(possible_codes, guess, feedback)
    assert narrowed_codes == [["G", "B", "Y", "R"]]


# Test is_win function
def test_is_win():
    assert is_win((4,0)) == True
    assert is_win((3,1)) == False


# Test game_over function
def test_game_over():
    assert game_over(10, 10) == True
    assert game_over(5, 10) == False


# Test incorrect user input
def test_incorrect_user_input():
    with pytest.raises(ValueError):
        is_win((3,))   # invalid feedback format