from mode2.py import generate_code, get_feedback, create_guess
import random   

def test_generate_code():
    code = generate_code()
    assert len(code) == 4
    for color in code:
        assert color in ['R', 'G', 'B', 'Y', 'W', 'K']
def test_get_feedback():
    code = ['R', 'G', 'B', 'Y']
    guess = ['R', 'G', 'B', 'Y']
    assert get_feedback(guess, code) == (4, 0)
    
    guess = ['R', 'G', 'B', 'K']
    assert get_feedback(guess, code) == (3, 0)
    
    guess = ['R', 'G', 'K', 'K']
    assert get_feedback(guess, code) == (2, 0)
    
    guess = ['R', 'K', 'K', 'K']
    assert get_feedback(guess, code) == (1, 0)
    
    guess = ['K', 'K', 'K', 'K']
    assert get_feedback(guess, code) == (0, 0)
    
    guess = ['Y', 'B', 'G', 'R']
    assert get_feedback(guess, code) == (0, 4)

def test_create_guess():
    possible_codes = [['R', 'G', 'B', 'Y'], ['R', 'G', 'B', 'K'], ['R', 'G', 'K', 'K']]
    guess = create_guess(possible_codes)
    assert guess in possible_codes


    
        