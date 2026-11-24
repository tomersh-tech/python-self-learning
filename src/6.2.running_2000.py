"""Exercise 6.2 - Running 2000.

Measure how long a function takes to run with given arguments.
"""
import time
from typing import Any, Callable


def running_2000(func: Callable[..., Any], *args: Any, **kwargs: Any) -> float:
    """Return how many seconds it takes to call a function.

    Args:
        func: The function to measure.
        *args: Positional arguments to pass to the function.
        **kwargs: Keyword arguments to pass to the function.

    Returns:
        The time the call took, in seconds.
    """
    start_time = time.perf_counter()
    func(*args, **kwargs)
    return time.perf_counter() - start_time


if __name__ == "__main__":
    print(running_2000(print, "Hello"))
    print(running_2000(zip, [1, 2, 3], [4, 5, 6]))
    # Timing str.format itself is the notebook's example, not a style choice.
    # pylint: disable-next=consider-using-f-string
    print(running_2000("Hi {name}".format, name="Bug"))
