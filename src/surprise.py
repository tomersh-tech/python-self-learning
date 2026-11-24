"""Bonus - Surprise.

A decorator that replaces what a function does with printing "surprise!".
"""
import functools
from typing import Any, Callable

SURPRISE_MESSAGE = "surprise!"


def surprise(func: Callable[..., Any]) -> Callable[..., None]:
    """Make a function print "surprise!" instead of doing what it does.

    The original function is never called. Any arguments are accepted
    and ignored, so the decorated function can still be called the
    same way as before.

    Args:
        func: The function to decorate.

    Returns:
        A function with the same name and docstring that only prints
        "surprise!".
    """
    @functools.wraps(func)
    def wrapper(*_args: Any, **_kwargs: Any) -> None:
        print(SURPRISE_MESSAGE)
    return wrapper


@surprise
def add(first: int, second: int) -> int:
    """Return the sum of two numbers."""
    return first + second


if __name__ == "__main__":
    print(add(2, 3))
