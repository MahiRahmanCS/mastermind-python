#pytest for core2.py
from core2 import random_code, generate_guess, narrow_down_codes, is_win, game_over

# Test random_code function
def test_random_code():
    code = random_code()
    assert len(code) == 4
    for color in code:
        assert color in ["R", "G", "B", "Y"]

# Test generate guess function
def test_generate_guess():
    possible_codes = [["R", "G", "B", "Y"], ["G", "B", "Y", "R"]]
    guess = generate_guess(possible_codes)
    assert len(guess) == 4
    for color in guess:
        assert color in ["R", "G", "B", "Y"]

# Test partial matches only
def test_narrow_down_codes():
    possible_codes = [["R", "G", "B", "Y"], ["G", "B", "Y", "R"], ["R", "R", "R", "R"]]
    guess = ["R", "G", "B", "Y"]
    feedback = (0, 4)  # 0 exact matches, 4 partial matches

    narrowed_codes = narrow_down_codes(possible_codes, guess, feedback)
    assert narrowed_codes == [["G", "B", "Y", "R"]]

# Test is_win function for a winning guess
def test_is_win():
    secret = ["R", "G", "B", "Y"]
    guess = ["R", "G", "B", "Y"]

    assert is_win(secret, guess) == True


# Test game_over function for a game over scenario 
def test_game_over():
    secret = ["R", "G", "B", "Y"]
    guess = ["R", "G", "B", "Y"]

    assert game_over(secret, guess) == True 


# test incorrect user input
def test_incorrect_user_input():
    secret = ["R", "G", "B", "Y"]
    guess = ["R", "G", "B"]  # Invalid guess (only 3 colors instead of 4)

    try:
        is_win(secret, guess)
        assert False, "Expected an exception for invalid input"
    except ValueError:
        pass  # Expected



