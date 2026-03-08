
import mode2
import core
from itertools import product

# possible colours for the code and guesses
colours = ["R", "G", "B", "Y", "W", "K"]

# game state variables
game_code = None
possible_codes = [list(code) for code in product(colours, repeat=4)]
current_attempt = 0
max_attempts = 10
current_guess = None
current_mode = None

def select_mode():
    global current_mode
    while True:
        print("Select Mode:")
        print("1: Mode 1: You Guess")
        print("2: Mode 2: Computer Guesses")
        try:
            mode = int(input("Enter 1 or 2: "))
            if mode in [1, 2]:
                current_mode = mode
                break
            else:
                print("Invalid choice. Please enter 1 or 2.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def restart():
    global game_code, current_attempt, possible_codes, current_guess
    
    # reset all variables based on current mode
    if current_mode == 1:
        # MODE 1: Generate a random code using core.py for player to guess
        game_code = core.random_code()
    else:
        # MODE 2: Generate a random code using mode2.py for computer to guess
        game_code = mode2.generate_code()
    
    current_attempt = 0
    current_guess = None
    possible_codes = [list(code) for code in product(colours, repeat=4)]
    
    print("\n--- New Game Started ---")
    if current_mode == 2:
        print("Think of a 4-colour code. Computer will start guessing!")

def submit_guess():
    global current_attempt
    
    if current_mode == 1:
        # MODE 1: User guesses the computer's code using core.py logic
        while True:
            guess_input = input("Enter your guess (4 colours separated by spaces, e.g., R G B Y): ").strip().upper()
            guess = guess_input.split()
            
            if len(guess) != 4:
                print("❌ Invalid guess. Please enter exactly 4 colours.")
                continue
            
            if not all(c in colours for c in guess):
                print(f"❌ Invalid colours. Available colours: {', '.join(colours)}")
                continue
            
            # validate the guess using core
            if not core.validate_guess(guess):
                print("❌ Invalid guess. Please select four valid colours.")
                continue
            
            break
        
        # score the guess using core
        exact_matches, partial_matches = core.score_guess(game_code, guess)
        current_attempt += 1

        # show the result
        print(f"Attempt {current_attempt}: {guess} -> Correct Position: {exact_matches}, Correct Colour: {partial_matches}")

        # check if player won using core
        if core.is_win(exact_matches):
            print("🎉 Congratulations! You guessed the code!")
            return True
        elif core.game_over(current_attempt):
            print(f"❌ Game Over! The code was: {game_code}")
            return True
    return False

def submit_feedback():
    global current_attempt, possible_codes, game_code, current_guess
    
    if current_mode == 2:
        # MODE 2: User provides feedback to computer's guess
        while True:
            feedback = input("Enter feedback (position-colour, e.g., 2-1): ").strip()
            
            try:
                parts = feedback.split('-')
                if len(parts) != 2:
                    print("Invalid format. Use: position-colour (e.g., 2-1)")
                    continue
                
                correct_position = int(parts[0])
                correct_colour = int(parts[1])
                
                if not (0 <= correct_position <= 4 and 0 <= correct_colour <= 4):
                    print("Invalid values. Position and colour must be between 0 and 4.")
                    continue
                
                break
            
            except ValueError:
                print("Invalid input. Use format: 2-1 (position-colour)")
        
        if current_attempt == 0:
            # First attempt: generate initial guess
            current_guess = mode2.create_guess(possible_codes)
            current_attempt += 1
            print(f"Attempt {current_attempt}: Computer guesses {current_guess}")
        else:
            # Narrow down based on feedback from previous guess
            possible_codes = [code for code in possible_codes 
                             if mode2.get_feedback(current_guess, code) == (correct_position, correct_colour)]
            
            if not possible_codes:
                print("❌ Invalid feedback. No codes match!")
                return False
            
            # check if previous guess was correct
            if correct_position == 4:
                print("🎉 Computer guessed your code!")
                return True
            
            if current_attempt >= max_attempts:
                print("❌ Computer failed to guess within 10 attempts")
                return True
            
            # Make next guess
            current_guess = mode2.create_guess(possible_codes)
            current_attempt += 1
            print(f"Attempt {current_attempt}: Computer guesses {current_guess}")
        
        return False

def main():
    print("Welcome to Mastermind!")
    print(f"Available colours: {', '.join(colours)}")
    
    select_mode()
    restart()
    
    game_over = False
    while not game_over:
        if current_mode == 1:
            game_over = submit_guess()
        else:
            game_over = submit_feedback()
        
        if game_over:
            while True:
                play_again = input("Play again? (y/n): ").strip().lower()
                if play_again == 'y':
                    select_mode()
                    restart()
                    game_over = False
                    break
                elif play_again == 'n':
                    print("Thanks for playing!")
                    return
                else:
                    print("Please enter 'y' or 'n'.")

if __name__ == "__main__":
    main()