Name: Mahi

Task: Designing a mode‑selection interface for switching between player‑guess and computer‑guess modes.

Prompt:
"How do I implement a clean console interface that allows players to select between Mode 1 (player guesses) and Mode 2 (computer guesses)?"

AI Output Summary:
The AI suggested using a loop that repeatedly asks for user input until a valid option is given. It recommended validating with try/except for numeric input and mapping the selected number to game modes.

Evaluation:
The proposed structure was simple and readable. However, the AI initially didn’t enforce re-prompting after invalid input.

Refinement:
Added explicit error messages and a loop that continues until a valid input (1 or 2) is entered.

Testing:
Verified behaviour with inputs such as "abc", "5", "", and "1".

Learning:
AI provides strong structural suggestions, but usability improvements (e.g., clearer error handling) benefit from manual adjustment.


Name: Mahi

Task: Building a restart system that resets all game state variables.

Prompt:
"What is a good way to reset all Mastermind game variables when the player chooses to restart?"

AI Output Summary:
The AI recommended creating a restart() function to reinitialize variables such as game_code, current_attempt, current_guess, and possible_codes. It also suggested regenerating the correct code depending on game mode.

Evaluation:
The logic was appropriate, but the AI initially placed code generation outside the function, which didn’t allow mode‑sensitive resets.

Refinement:
Integrated a mode check (current_mode == 1 vs 2) inside the restart function.

Testing:
Manually verified restarts after Mode 1 and Mode 2 games, ensuring separate code generators were used.

Learning:
AI-provided structure is helpful, but details about multi‑mode interactions require clarification.


Name: Mahi

Task: Creating input validation for user guesses in Mode 1.

Prompt:
"How can I validate a user's guess in a Mastermind console game to ensure it contains exactly four valid colours?"

AI Output Summary:
The AI recommended checking length, verifying each token against a list of valid colours, and looping until the user enters a correct format. It also suggested integrating existing core.validate_guess() logic.

Evaluation:
The flow was correct, although confirmation messages needed improvement for clarity.

Refinement:
Added more user‑friendly feedback messages and improved spacing and formatting in the console output.

Testing:
Tried cases like "R G B", "R K X Y", "R G B Y R", and random incorrect formatting.

Learning:
AI can structure logic well, but human iteration helps make the user experience smoother and more intuitive.













Name: Muhammad

Task: Implement correct duplicate handling in scoring logic.

Prompt:
"How do I prevent double-counting duplicates in a Mastermind scoring algorithm?"

AI Output Summary:
Suggested a two-pass system where exact matches are identified first and marked, followed by partial matches using modified copies of the lists.

Evaluation:
The two-pass approach was correct and aligned with the Mastermind specification. However, initial output did not fully clarify how to prevent reusing matched elements.

Refinement:
Refined the approach to explicitly replace matched elements with None to ensure they cannot be reused.

Testing:
Validated using duplicate-heavy test cases such as secret = ["R","R","G","B"] and guess = ["R","R","R","R"].

Learning:
AI can generate correct high-level solutions, but careful refinement and testing are necessary to ensure full compliance with specifications.




Name: Muhammad

Task: Improve readability and maintainability of the scoring function.

Prompt:

"How can I refactor a Python function to make the Mastermind scoring logic cleaner and easier to maintain?"

AI Output Summary:
Suggested separating the logic into smaller steps, detecting exact matches, filtering remaining elements, and calculating partial matches. It also recommended clearer variable names.

Evaluation:
The response improved readability and made the logic easier to follow. However, some suggested variable names required adjustment to match the project’s naming conventions.

Refinement:
Renamed variables to match project standards and added comments explaining each stage of the algorithm.

Testing:
Executed existing unit tests to confirm that refactoring did not change the scoring behaviour.

Learning:
AI can be very helpful for improving code structure, but the final implementation still requires human judgement to ensure clarity and consistency.



Name: Muhammad

Task

Evaluate the efficiency of the Mastermind scoring algorithm and determine its time complexity.

Prompt

"What is the time complexity of a Mastermind scoring algorithm that first checks for exact matches and then checks remaining elements for partial matches?"

AI Output Summary

The AI explained that the algorithm typically runs in linear time relative to the length of the code sequence. It described that the first pass checks for exact matches by iterating through both lists once. The second pass then checks the remaining unmatched elements to identify partial matches. Since both passes iterate through the lists only once, the overall time complexity was identified as O(n).

Evaluation

The explanation correctly identified the algorithm as having linear time complexity. However, the AI initially did not fully explain how the method used to check for partial matches could affect performance. For example, if nested loops were used to search through remaining elements, the complexity could increase to O(n²). This highlighted the importance of choosing efficient data structures and avoiding unnecessary repeated searches.

Refinement

The prompt was refined to ask how different implementation approaches such as nested loops, removing elements from lists, or using dictionary counting, could affect the complexity. This helped clarify that efficient implementations can maintain O(n) complexity, while poorly designed approaches could increase the runtime to O(n²).

Testing

The algorithm was tested using multiple guess combinations to verify correct scoring behaviour. 
Test cases included:

All correct guesses

All incorrect guesses

Scenarios with duplicate colours

An example test case was:

secret = ["R","R","G","B"]

guess = ["R","R","R","R"]

This ensured the algorithm correctly handled duplicate colours and did not overcount partial matches.

Learning

This interaction demonstrated that AI can help explain algorithm complexity and efficiency. However, it is important to critically evaluate the explanations and consider how different implementation choices affect performance. Testing the algorithm with edge cases also helped confirm that the scoring logic works correctly.





Name: Emmauel

Task:
Verify that the narrow_down_codes function correctly filters the list of possible codes based on feedback from a guess.

Prompt:
"How can I test whether narrow_down_codes(possible_codes, guess, feedback) correctly removes codes that do not match the provided Mastermind feedback?"

AI Output Summary:
The AI suggested creating a unit test where a guess is compared with multiple possible codes and only the code that produces the same feedback remains in the filtered list.

Evaluation:
The test effectively checks whether the filtering logic works correctly. By using feedback (0,4), it ensures that only codes containing the same colours as the guess but in different positions are retained.

Refinement:
The test could be expanded by adding additional cases, such as feedback with exact matches (4,0) or mixed feedback (2,1), to ensure the function behaves correctly across different scenarios.

Testing:
Example values used:

possible_codes = [["R","G","B","Y"], ["G","B","Y","R"], ["R","R","R","R"]]
guess = ["R","G","B","Y"]
feedback = (0,4)

The expected result is:

[["G","B","Y","R"]]

Learning:
This test demonstrates how filtering functions can be validated by using inputs and checking the expected output. Testing with different feedback combinations helps ensure the solver correctly narrows the search space.




Name: Emmanuel

Task:
Check the correctness of the get_feedback function used to calculate Mastermind scoring results.

Prompt:
"How does the get_feedback(guess, secret) function calculate the number of correct positions and correct colours in a Mastermind game, does it also check for duplicates"

AI Output Summary:
The AI explained that the function first counts exact matches by comparing each element of the guess and secret lists using zip. It then calculates colour matches by counting the minimum occurrences of each colour in both lists and subtracting the exact matches to determine partial matches.

Evaluation:
The explanation correctly described how the algorithm works. The use of min(guess.count(c), secret.count(c)) ensures that duplicate colours are not overcounted. However, the approach requires multiple count() operations, which can increase computational cost as the number of colours grows.

Refinement:
The prompt was refined to consider whether using a two-pass algorithm with marked elements or using a dictionary-based counting approach could improve clarity and efficiency while still preventing duplicate colour overcounting.

Testing:
The function was tested with several scenarios, including duplicate-heavy cases such as:

secret = ["R","R","G","B"]
guess = ["R","R","R","R"]

This verified that the function correctly returns (2,0) without incorrectly counting extra partial matches.

Learning:
This interaction showed that AI can effectively explain algorithm logic and help identify potential efficiency concerns.




Name: Emmanuel

Task:
Verify that the generate_guess function returns a valid guess from the list of possible codes.

Prompt:
"How can I test that the generate_guess(possible_codes) function correctly returns a valid Mastermind guess with four colours taken from the allowed colour set?"

AI Output Summary:
The AI suggested creating a unit test that checks the structure of the returned guess. The test verifies that the guess contains exactly four elements and that each element is a valid colour from the allowed set.

Evaluation:
The test successfully confirms that the function returns a correctly formatted guess. However, it does not guarantee that the guess actually comes from the possible_codes list, which is the intended behavior of the function.

Refinement:
The test could be improved by asserting that the returned guess is one of the codes in possible_codes, ensuring the function does not generate a value outside the candidate list.

Testing:
Example test case used:

possible_codes = [["R","G","B","Y"], ["G","B","Y","R"]]

The test confirms:

The guess length is 4

Each colour in the guess is valid

Learning
This interaction showed that unit tests should verify the intended logic of the function. Ensuring the returned guess is part of the possible_codes list would make the test more complete.

