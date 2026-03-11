"""
Command line interface for the Mastermind game.
Handles user input, displays feedback, and controls the game loop.
"""

from .core import random_code, validate_guess, score_guess, is_win, game_over

def main():
    print("Welcome to Mastermind!")
    secret = random_code()
    guess_count = 0
    
    while not game_over(guess_count):
        guess_input = input("Enter your guess of 4 letters (allowed: R, G, B, Y, W, K): ").upper()
        guess = list(guess_input)
        
        if not validate_guess(guess):
            print("Invalid guess. Try again.")
            continue
        
        guess_count += 1
        exact, partial = score_guess(secret, guess)
        print(f"Exact matches: {exact}, Partial matches: {partial}")
        
        if is_win(exact):
            print(f"Congratulations! You guessed the code in {guess_count} tries.")
            break

        print(f"You have {MAX_GUESSES - guess_count} guesses left.\n")
    else:
        print(f"Game over! The secret code was: {''.join(secret)}")

if __name__ == "__main__":
    main()