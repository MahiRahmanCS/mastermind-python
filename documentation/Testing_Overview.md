Testing Overview

Testing Categories Used

We implemented:
Unit tests for individual functions

Boundary tests (max guesses = 10)

Edge case tests (all matches, no matches)

Duplicate handling tests (critical for Mastermind scoring)


Why These Tests Are Important:
The scoring logic is the most complex component of the system.
Incorrect duplicate handling can result in inflated partial matches.

Testing exact, partial, and duplicate scenarios ensures the feedback mechanism matches the game rules.

Most Critical Tests:
The most critical test was test_duplicate_handling.

This ensures that duplicate colours in the guess do not result in double-counting, which would violate the specification.

Example Defect Identified:
During testing, incorrect partial match behaviour occurred when duplicates were not properly marked as used. This was resolved by marking matched elements as None in both secret and guess copies.

Traceability:
Each test maps directly to a functional requirement, ensuring full traceability from specification to implementation to validation.


Automated Testing:
All tests were implemented using the pytest framework.
The test suite validates:

- scoring correctness
- duplicate handling
- guess validation
- secret code generation

Tests can be executed using:
pytest tests/

This ensures that changes to the code do not break existing functionality.