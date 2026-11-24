"""Exercise 6.4 - Remember remember.

Decode a message hidden in an image. Each column of the image has one
dark pixel, and the row of that pixel is the character code of the
next letter of the message.
"""
from PIL import Image

GRAYSCALE_MODE = "L"


def find_dark_row(image: Image.Image, column: int) -> int:
    """Return the row of the darkest pixel in one column of an image.

    Args:
        image: A grayscale image.
        column: The index of the column to search in.

    Returns:
        The row index of the darkest pixel in that column.
    """
    return min(
        range(image.height),
        key=lambda row: image.getpixel((column, row)),
    )


def remember_remember(image_path: str) -> str:
    """Return the message hidden in an image.

    Args:
        image_path: Path to the encoded image file.

    Returns:
        The decoded message, read from the left column to the right.

    Raises:
        ValueError: If the image has columns but no rows.
    """
    with Image.open(image_path) as image:
        grayscale_image = image.convert(GRAYSCALE_MODE)
    if grayscale_image.width and not grayscale_image.height:
        raise ValueError("The image has no rows, so it can't hold a message.")
    return "".join(
        chr(find_dark_row(grayscale_image, column))
        for column in range(grayscale_image.width)
    )


if __name__ == "__main__":
    print(remember_remember("resources/code.png"))
