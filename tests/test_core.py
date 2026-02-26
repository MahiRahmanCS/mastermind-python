from src.core import score_guess, validate_guess, random_code
# When all 4 pegs are correct and in the correct position.
def test_all_exact_matches():
    secret = ["R", "G", "B", "Y"]
    guess = ["R", "G", "B", "Y"]
    
    exact, partial = score_guess(secret, guess)
    
    assert exact == 4
    assert partial == 0


# Test Zero Matches
def test_no_matches():
    secret = ["R", "R", "R", "R"]
    guess = ["G", "G", "G", "G"]
    
    exact, partial = score_guess(secret, guess)
    
    assert exact == 0
    assert partial == 0

# Test Partial Matches Only
def test_all_partial_matches():
    secret = ["R", "G", "B", "Y"]
    guess = ["G", "B", "Y", "R"]
    
    exact, partial = score_guess(secret, guess)
    
    assert exact == 0
    assert partial == 4

# Test Duplicate Double-Count Prevention
def test_no_duplicate_double_count():
    secret = ["R", "R", "G", "B"]
    guess = ["R", "R", "R", "R"]
    
    exact, partial = score_guess(secret, guess)
    
    assert exact == 2
    assert partial == 0

# Mixed Exact + Partial
def test_mixed_exact_and_partial():
    secret = ["R", "G", "B", "R"]
    guess = ["R", "R", "G", "B"]
    
    exact, partial = score_guess(secret, guess)
    
    assert exact == 1
    assert partial == 3


def test_validate_guess_valid():
    assert validate_guess(["R", "G", "B", "Y"]) == True

def test_validate_guess_invalid_length():
    assert validate_guess(["R", "G", "B"]) == False

def test_validate_guess_invalid_colour():
    assert validate_guess(["R", "G", "B", "X"]) == False

def test_generate_code_length():
    code = random_code()
    assert len(code) == 4

def test_generate_code_allowed_colours():
    code = random_code()
    for slot in code:
        assert slot in ["R","G","B","Y","W","K"]