For Each Entry Include
Name: Mahi Rahman
Task –  create an interface layer for the Mastermind game, separating user interaction (prompts, formatting, display) from logic modules like core.py and mode2.py.
Prompt – 
    Write a Python module called interfaces.py for a Mastermind game.
    It must contain functions that handle all user‑interface responsibilities such as:

    formatted printing
    showing guesses and feedback
    asking for mode selection
    asking for user guesses
    asking for feedback in mode 2

    No game logic should be inside this module.

AI Output (Summary) –
     def display_welcome():
         print("Welcome to Mastermind!")
    def prompt_mode():
        return input("Select mode (1: You guess, 2: Computer guesses): ")
    def prompt_guess():
        return input("Enter your guess: ")
    def show_feedback(exact, partial):
        print(f"Correct Position: {exact}, Correct Colour: {partial}")

Evaluation – 
        Correct - UI‑only functions, separation from logic, Clear naming
        incorrect/incomplete -No validation inside interface prompts, No structured return types, Missing error‑display messages

Refinement – I refined the next prompt to improve consistency and future‑proofing

Testing – missing error display messages may cause confusion to users on whats wrong

Learning – AI needs explicit instructions for data validation


Sequence Diagrams
I will provide a brief overview in Thursday’s lecture (along with automated testing).























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