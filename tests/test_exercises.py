"""Tests for the exercises in the src directory.

The exercise files are named <week>.<part>.<exercise name>.py, which
can't be imported with a normal import statement, so they are loaded
by path.
"""
import datetime
import importlib.util
import pathlib
import sys
import tempfile
import time
import types
import unittest

from PIL import Image

SOURCE_DIRECTORY = pathlib.Path(__file__).parent.parent / "src"
WHITE = 255
BLACK = 0


def load_exercise(file_name: str) -> types.ModuleType:
    """Load an exercise module from the src directory by its file name."""
    module_name = file_name.removesuffix(".py").replace(".", "_")
    spec = importlib.util.spec_from_file_location(
        module_name, SOURCE_DIRECTORY / file_name
    )
    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    spec.loader.exec_module(module)
    return module


class TestWeek5(unittest.TestCase):
    """Tests for the week 5 exercises."""

    def test_thats_the_way(self) -> None:
        """Only files that start with "deep" are returned, sorted."""
        exercise = load_exercise("5.1.thats_the_way.py")
        with tempfile.TemporaryDirectory() as directory:
            folder = pathlib.Path(directory)
            for name in ("deeper2.svg", "deeper.svg", "logo.jpg"):
                (folder / name).touch()
            (folder / "deep_folder").mkdir()
            self.assertEqual(
                exercise.thats_the_way(directory),
                ["deeper.svg", "deeper2.svg"],
            )

    def test_random_date_between(self) -> None:
        """The random date is inside the range, in any order."""
        exercise = load_exercise("5.1.no_vinnigrete.py")
        start = datetime.date(2026, 1, 10)
        end = datetime.date(2026, 1, 15)
        for _ in range(100):
            self.assertTrue(
                start <= exercise.random_date_between(end, start) <= end
            )

    def test_cup_of_join(self) -> None:
        """Lists are joined with the separator between them."""
        exercise = load_exercise("5.2.cup_of_join.py")
        self.assertEqual(
            exercise.cup_of_join([1, 2], [8], [9, 5, 6], sep="@"),
            [1, 2, "@", 8, "@", 9, 5, 6],
        )
        self.assertEqual(exercise.cup_of_join([1]), [1])
        with self.assertRaises(ValueError):
            exercise.cup_of_join()

    def test_piece_of_cake(self) -> None:
        """The recipe price matches the notebook examples."""
        exercise = load_exercise("5.2.piece_of_cake.py")
        prices = {"chocolate": 18, "milk": 8}
        self.assertEqual(
            exercise.piece_of_cake(prices, chocolate=200, milk=100), 44
        )
        self.assertEqual(
            exercise.piece_of_cake(prices, optionals=["milk"], chocolate=300),
            54,
        )
        self.assertEqual(exercise.piece_of_cake({}), 0)

    def test_parsle_tongue(self) -> None:
        """Messages are found, including ones split between chunks."""
        exercise = load_exercise("5.3.parsle_tongue.py")
        split_message = b"\x00" * (exercise.CHUNK_SIZE - 3) + b"hello!"
        content = b"\xffabc!\x00python!\x10" + split_message
        with tempfile.TemporaryDirectory() as directory:
            file_path = pathlib.Path(directory) / "secret.bin"
            file_path.write_bytes(content)
            self.assertEqual(
                exercise.parsle_tongue(str(file_path)), ["python!", "hello!"]
            )

    def test_interleaves(self) -> None:
        """Items are interleaved, and longer iterables keep going."""
        exercise = load_exercise("5.4.interleaves.py")
        self.assertEqual(
            exercise.interleaves("abc", [1, 2, 3], ("!", "@", "#")),
            ["a", 1, "!", "b", 2, "@", "c", 3, "#"],
        )
        self.assertEqual(
            list(exercise.generator_interleaves("ab", [1, 2, 3, 4])),
            ["a", 1, "b", 2, 3, 4],
        )


class TestWeek6(unittest.TestCase):
    """Tests for the week 6 exercises."""

    def test_running_2000(self) -> None:
        """The measured time is at least the time the function sleeps."""
        exercise = load_exercise("6.2.running_2000.py")
        sleep_seconds = 0.05
        self.assertGreaterEqual(
            exercise.running_2000(time.sleep, sleep_seconds), sleep_seconds
        )

    def test_long_cat_is_long(self) -> None:
        """Punctuation is removed and words are lowercased."""
        exercise = load_exercise("6.3.long_cat_is_long.py")
        self.assertEqual(
            exercise.long_cat_is_long("You see, a very long cat."),
            {"you": 3, "see": 3, "a": 1, "very": 4, "long": 4, "cat": 3},
        )

    def test_remember_remember(self) -> None:
        """The rows of the dark pixels are decoded into text."""
        exercise = load_exercise("6.4.remember_remember.py")
        image = Image.new("L", (2, 255), WHITE)
        image.putpixel((0, ord("H")), BLACK)
        image.putpixel((1, ord("i")), BLACK)
        with tempfile.TemporaryDirectory() as directory:
            image_path = pathlib.Path(directory) / "code.png"
            image.save(image_path)
            self.assertEqual(exercise.remember_remember(str(image_path)), "Hi")

    def test_group_by(self) -> None:
        """Items are grouped by the key function, in order."""
        exercise = load_exercise("6.5.group_by.py")
        self.assertEqual(
            exercise.group_by(len, ["hi", "bye", "yo", "try"]),
            {2: ["hi", "yo"], 3: ["bye", "try"]},
        )


class TestWeek7(unittest.TestCase):
    """Tests for the week 7 exercise."""

    def test_read_and_search_inbox(self) -> None:
        """Messages are read once, and search looks in title and body."""
        exercise = load_exercise("7.2.turtle_sent.py")
        post_office = exercise.PostOffice(["a", "b"])
        post_office.send_message("a", "b", "first body", title="Lunch")
        post_office.send_message("a", "b", "second body")
        self.assertEqual(len(post_office.search_inbox("b", "Lunch")), 1)
        self.assertEqual(len(post_office.read_inbox("b", 1)), 1)
        self.assertEqual(len(post_office.read_inbox("b")), 1)
        self.assertEqual(post_office.read_inbox("b"), [])


class TestBonus(unittest.TestCase):
    """Tests for the bonus decorator exercises."""

    def test_type_check(self) -> None:
        """A wrong argument type raises the custom error."""
        exercise = load_exercise("type_check.py")
        self.assertEqual(exercise.times_two(5), 10)
        self.assertEqual(exercise.times_two(number=5), 10)
        with self.assertRaises(exercise.WrongArgumentTypeError):
            exercise.times_two("5")

    def test_surprise(self) -> None:
        """The decorated function returns None instead of its result."""
        exercise = load_exercise("surprise.py")
        self.assertIsNone(exercise.add(2, 3))

    def test_twice(self) -> None:
        """The decorated function runs two times."""
        exercise = load_exercise("twice.py")
        calls = []

        @exercise.twice
        def record_call() -> None:
            calls.append(None)

        record_call()
        self.assertEqual(len(calls), 2)


if __name__ == "__main__":
    unittest.main()
