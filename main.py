"""Entry point of the repository.

Runs the demo of every exercise in the src directory. The exercise files
are named <week>.<part>.<exercise name>.py, so they are run by path
instead of being imported.
"""
import pathlib
import runpy

SOURCE_DIRECTORY = pathlib.Path(__file__).parent / "src"
SKIPPED_EXERCISES = {
    # Needs input from the user.
    "5.1.no_vinnigrete.py",
    # Need resource files from the course notebooks.
    "5.1.thats_the_way.py",
    "5.3.parsle_tongue.py",
    "6.4.remember_remember.py",
}


def main() -> None:
    """Run the demo of each exercise that can run on its own."""
    for exercise_path in sorted(SOURCE_DIRECTORY.glob("*.py")):
        if exercise_path.name in SKIPPED_EXERCISES:
            continue
        print(f"=== {exercise_path.name}")
        runpy.run_path(str(exercise_path), run_name="__main__")


if __name__ == "__main__":
    main()
