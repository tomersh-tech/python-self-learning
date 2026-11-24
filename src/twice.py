"""Bonus - Twice.

A decorator that runs the function it wraps two times.
"""
from typing import Any, Callable

from decorator import decorator


@decorator
def twice(func: Callable[..., Any], *args: Any, **kwargs: Any) -> Any:
    """Run the decorated function twice with the same arguments.

    The decorator package keeps the decorated function's name,
    docstring and signature.

    Args:
        func: The decorated function.
        *args: Positional arguments the function was called with.
        **kwargs: Keyword arguments the function was called with.

    Returns:
        The result of the second call.
    """
    func(*args, **kwargs)
    return func(*args, **kwargs)


@twice
def greet(name: str) -> None:
    """Print a greeting."""
    print(f"Hello, {name}!")


if __name__ == "__main__":
    greet("Bug")
