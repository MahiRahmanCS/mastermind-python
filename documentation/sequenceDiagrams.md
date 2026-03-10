Mode 1 and Mode 2 of the program both implement the logic of the Mastermind game, but they differ in terms of how the guessing process works and how clear the interaction is for the user.

In Mode 1, the computer generates a random secret code and the player tries to guess it within a limited number of attempts. This mode is quite accurate because the program directly checks the player’s guess against the secret code using the `score_guess` function. The feedback given (exact matches and partial matches) clearly reflects how close the guess is to the correct answer. From a clarity perspective, this mode is easy for the user to understand because the player simply enters guesses and receives straightforward feedback.

Mode 2 works in the opposite way: the user thinks of a secret code and the computer attempts to guess it. The program generates all possible colour combinations and gradually narrows them down based on the feedback provided by the user. This approach is also accurate in theory because it systematically eliminates codes that do not match the feedback. However, its accuracy depends on the user giving correct feedback each time. If the user makes a mistake when entering the feedback, the program may remove valid possibilities and fail to guess the correct code.

In terms of clarity, Mode 2 is slightly more complex. The user must understand how to provide feedback in the correct format (for example “2-1”), which can make the interaction less intuitive compared to Mode 1. However, it demonstrates a more advanced problem-solving approach, as the program logically reduces the set of possible codes after each guess.

Overall, Mode 1 is simpler and clearer for users, while Mode 2 is more algorithmically interesting but relies more heavily on accurate user input.

