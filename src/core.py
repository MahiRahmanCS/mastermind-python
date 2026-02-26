import random

colours = ["red", "blue", "green", "yellow", "orange", "purple"]


class MastermindGame:
    """Simple Mastermind game engine.

    The secret code is a list of four colours chosen from :data:`colours`.
    ``evaluate_guess`` returns a tuple ``(black, white)`` where *black* is
    the number of pegs that are the correct colour in the correct position,
    and *white* is the number of correct colours in the wrong position.
    """

    def __init__(self):
        self.reset()

    def reset(self):
        """Generate a new secret code and clear attempt history."""
        self.code = [random.choice(colours) for _ in range(4)]
        self.attempts = []

    def evaluate_guess(self, guess):
        """Evaluate a single guess against the secret code.

        :param guess: iterable of four colour strings
        :returns: tuple ``(black, white)``
        """
        # make copies since we will modify the lists
        code_copy = list(self.code)
        guess_copy = list(guess)

        # first count exact matches (black pegs)
        black = 0
        for i in range(4):
            if guess_copy[i] == code_copy[i]:
                black += 1
                code_copy[i] = None
                guess_copy[i] = None

        # count correct colours in wrong positions (white pegs)
        white = 0
        for i in range(4):
            if guess_copy[i] and guess_copy[i] in code_copy:
                white += 1
                code_copy[code_copy.index(guess_copy[i])] = None

        self.attempts.append((guess, black, white))
        return black, white

    def is_solved(self):
        """Return ``True`` if the last guess solved the code."""
        if not self.attempts:
            return False
        return self.attempts[-1][1] == 4
