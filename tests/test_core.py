from src.core import score_guess
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