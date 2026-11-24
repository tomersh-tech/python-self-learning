"""Exercise 5.3 - Parsle tongue.

Find secret messages hidden inside a binary file. A secret message is
at least 5 lowercase English letters followed by an exclamation mark.
"""
from typing import Iterator

CHUNK_SIZE = 1024
MIN_MESSAGE_LENGTH = 5
MESSAGE_END = ord("!")
LOWERCASE_START = ord("a")
LOWERCASE_END = ord("z")


def read_in_chunks(
    file_path: str, chunk_size: int = CHUNK_SIZE
) -> Iterator[bytes]:
    """Yield the content of a binary file, one chunk at a time.

    Args:
        file_path: Path to the file to read.
        chunk_size: How many bytes to read each time.

    Yields:
        The next chunk of bytes from the file.
    """
    with open(file_path, "rb") as binary_file:
        chunk = binary_file.read(chunk_size)
        while chunk:
            yield chunk
            chunk = binary_file.read(chunk_size)


def parsle_tongue(file_path: str) -> list[str]:
    """Return the secret messages hidden in a binary file.

    The file is read in chunks, so it never has to fit in memory.
    Messages that are split between two chunks are still found, because
    the current run of letters is kept between chunks.

    Args:
        file_path: Path to the file to search in.

    Returns:
        The secret messages in the order they appear, each including
        its exclamation mark.
    """
    messages: list[str] = []
    letters: list[str] = []
    for chunk in read_in_chunks(file_path):
        for byte in chunk:
            if LOWERCASE_START <= byte <= LOWERCASE_END:
                letters.append(chr(byte))
                continue
            if byte == MESSAGE_END and len(letters) >= MIN_MESSAGE_LENGTH:
                messages.append("".join(letters) + "!")
            letters = []
    return messages


if __name__ == "__main__":
    for message in parsle_tongue("resources/logo.jpg"):
        print(message)
