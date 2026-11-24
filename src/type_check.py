"""Bonus - Type check.

A decorator factory that checks the type of a function's argument.
"""
import functools
from typing import Any, Callable


class WrongArgumentTypeError(TypeError):
    """Raised when a decorated function gets an argument of the wrong type."""


def type_check(
    expected_type: type,
) -> Callable[[Callable[[Any], Any]], Callable[[Any], Any]]:
    """Create a decorator that checks the type of a function's argument.

    The decorated function must take exactly one argument.

    Args:
        expected_type: The type the argument must be.

    Returns:
        A decorator that raises WrongArgumentTypeError when the decorated
        function gets an argument that isn't of expected_type.
    """
    def decorator(func: Callable[[Any], Any]) -> Callable[[Any], Any]:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            for argument in (*args, *kwargs.values()):
                if not isinstance(argument, expected_type):
                    raise WrongArgumentTypeError(
                        f"{func.__name__} expected {expected_type.__name__}, "
                        f"got {type(argument).__name__}."
                    )
            return func(*args, **kwargs)
        return wrapper
    return decorator


@type_check(int)
def times_two(number: int) -> int:
    """Return the number multiplied by two."""
    return number * 2


if __name__ == "__main__":
    print(times_two(5))
    print(times_two.__name__, "-", times_two.__doc__)
    try:
        times_two("5")
    except WrongArgumentTypeError as error:
        print(f"Error: {error}")
