"""Exercise 5.4 - Interleaves.

Interleave the items of several iterables: first item of each, then
the second item of each, and so on.
"""
from typing import Any, Iterable, Iterator


def generator_interleaves(*iterables: Iterable[Any]) -> Iterator[Any]:
    """Yield the items of the given iterables, interleaved.

    When an iterable runs out of items it is skipped, and the others
    keep going until all of them are used up.

    Args:
        *iterables: The iterables to interleave.

    Yields:
        The next item in the interleaved order.
    """
    iterators = [iter(iterable) for iterable in iterables]
    while iterators:
        still_active = []
        for iterator in iterators:
            try:
                item = next(iterator)
            except StopIteration:
                continue
            still_active.append(iterator)
            yield item
        iterators = still_active


def interleaves(*iterables: Iterable[Any]) -> list[Any]:
    """Return a list of the items of the given iterables, interleaved.

    Args:
        *iterables: The iterables to interleave.

    Returns:
        All the items, in interleaved order.
    """
    return list(generator_interleaves(*iterables))


if __name__ == "__main__":
    print(interleaves("abc", [1, 2, 3], ("!", "@", "#")))
    print(list(generator_interleaves("abc", [1, 2, 3], ("!", "@", "#"))))
