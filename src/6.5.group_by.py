"""Exercise 6.5 - Group by.

Group the items of an iterable by the result of a key function.
"""
from collections.abc import Callable, Hashable, Iterable
from typing import Any


def group_by(
    key_func: Callable[[Any], Hashable], items: Iterable[Any]
) -> dict[Hashable, list[Any]]:
    """Group items by the value a function returns for each of them.

    Args:
        key_func: Called on each item. Its result is the item's group.
        items: The items to group.

    Returns:
        A dictionary from each result of key_func to a list of the items
        that gave that result, in their original order.
    """
    groups: dict[Hashable, list[Any]] = {}
    for item in items:
        groups.setdefault(key_func(item), []).append(item)
    return groups


if __name__ == "__main__":
    print(group_by(len, ["hi", "bye", "yo", "try"]))
