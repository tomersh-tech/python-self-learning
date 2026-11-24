"""Exercise 5.2 - Cup of join.

Join any number of lists into one list, with a separator between them.
"""
from typing import Any

DEFAULT_SEPARATOR = "-"


def cup_of_join(*lists: list[Any], sep: Any = DEFAULT_SEPARATOR) -> list[Any]:
    """Join lists into a single list, putting a separator between each two.

    The input lists are not changed.

    Args:
        *lists: The lists to join, in order.
        sep: The item placed between each two lists. Defaults to "-".

    Returns:
        A new list with all the items of the given lists and the separators.

    Raises:
        ValueError: If no lists are given.
    """
    if not lists:
        raise ValueError("cup_of_join needs at least one list.")

    joined = list(lists[0])
    for current_list in lists[1:]:
        joined.append(sep)
        joined.extend(current_list)
    return joined


if __name__ == "__main__":
    print(cup_of_join([1, 2], [8], [9, 5, 6], sep="@"))
    print(cup_of_join([1, 2], [8], [9, 5, 6]))
    print(cup_of_join([1]))
