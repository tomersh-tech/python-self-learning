"""Exercise 6.3 - Long cat is long.

Map each word in a text to its length.
"""

WORD_SEPARATOR = " "

EXAMPLE_TEXT = """
You see, wire telegraph is a kind of a very, very long cat.
You pull his tail in New York and his head is meowing in Los Angeles.
Do you understand this?
And radio operates exactly the same way:
you send signals here, they receive them there.
The only difference is that there is no cat.
"""


def long_cat_is_long(text: str) -> dict[str, int]:
    """Return a dictionary that maps each word in a text to its length.

    Words are lowercased, and anything that isn't a letter is treated
    as a space, so punctuation is not counted as part of a word.

    Args:
        text: The text to go over.

    Returns:
        A dictionary from each word to the number of letters in it.
    """
    clean_text = "".join(
        char if char.isalpha() else WORD_SEPARATOR for char in text.lower()
    )
    return {word: len(word) for word in clean_text.split()}


if __name__ == "__main__":
    print(long_cat_is_long(EXAMPLE_TEXT))
