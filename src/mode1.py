import random

from .core import colours


# simple helper functions using the shared colour list

def generate_code():
    """Return a random four‑colour code (list of strings)."""
    return [random.choice(colours) for _ in range(4)]


def check_input(user_input, code):
    """Return True if ``user_input`` appears anywhere in ``code``."""
    return user_input in code


def check_position(user_input, code):
    """If ``user_input`` is in ``code`` return its index, otherwise ``-1``."""
    try:
        return code.index(user_input)
    except ValueError:
        return -1
