"""Exercise 5.1 - No vinaigrette.

Pick a random date between two dates given by the user, and warn
if it falls on a Monday (no vinaigrette that day!).
"""
import datetime
import random

DATE_FORMAT = "%Y-%m-%d"
MONDAY = 0
NO_VINAIGRETTE_MESSAGE = "אין לי ויניגרט!"


def parse_date(date_text: str) -> datetime.date:
    """Convert a YYYY-MM-DD string into a date.

    Args:
        date_text: The date as typed by the user.

    Returns:
        The matching date object.

    Raises:
        ValueError: If the text is not a valid YYYY-MM-DD date.
    """
    return datetime.datetime.strptime(date_text.strip(), DATE_FORMAT).date()


def random_date_between(
    first_date: datetime.date, second_date: datetime.date
) -> datetime.date:
    """Return a random date between two dates, both ends included.

    The dates can be given in any order.

    Args:
        first_date: One end of the range.
        second_date: The other end of the range.

    Returns:
        A random date inside the range.
    """
    start_date, end_date = sorted((first_date, second_date))
    days_between = (end_date - start_date).days
    random_offset = random.randint(0, days_between)
    return start_date + datetime.timedelta(days=random_offset)


def no_vinnigrete() -> None:
    """Ask the user for two dates and print a random date between them.

    If the random date is a Monday, also print a vinaigrette warning.
    """
    try:
        first_date = parse_date(input("Enter the first date (YYYY-MM-DD): "))
        second_date = parse_date(input("Enter the second date (YYYY-MM-DD): "))
    except ValueError:
        print("Error: dates must be valid and in the format YYYY-MM-DD.")
        return

    chosen_date = random_date_between(first_date, second_date)
    print(chosen_date.strftime(DATE_FORMAT))
    if chosen_date.weekday() == MONDAY:
        print(NO_VINAIGRETTE_MESSAGE)


if __name__ == "__main__":
    no_vinnigrete()
