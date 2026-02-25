Mastermind Game — Requirements Specification
1. Definitions

Code Length:
The secret code shall consist of 4 slots.

Allowed Colours:
The allowed colours shall be represented by the following letters:

R – Red

G – Green

B – Blue

Y – Yellow

W – White

K – Black

Duplicates:
Duplicate colours shall be permitted in the secret code and in guesses.

Maximum Guesses:
The player shall have a maximum of 10 guesses.

Exact Match:
A slot is an exact match if it has the correct colour in the correct position.

Partial Match:
A slot is a partial match if it has the correct colour but is in the wrong position.

Duplicate Counting Rule:
Each slot in the secret code may only contribute to one match (exact or partial).
No slot may be double-counted.

2. Functional Requirements

FR1 — Secret Code Generation
The system shall generate a secret code consisting of 4 slots selected from the 6 allowed colours, with duplicates permitted.

FR2 — Guess Validation
The system shall validate that each guess:

Contains exactly 4 characters.

Uses only allowed colours.
Invalid guesses shall be rejected.

FR3 — Exact Match Calculation
The system shall correctly calculate the number of exact matches between the secret code and the player's guess.

FR4 — Partial Match Calculation
The system shall correctly calculate the number of partial matches without double-counting duplicate colours.

FR5 — Guess Limit Enforcement
The system shall allow a maximum of 10 guesses per game.

FR6 — Win Condition
The system shall declare a win if the player achieves 4 exact matches.

FR7 — Game Termination
The system shall terminate after a win or after 10 guesses, whichever occurs first.