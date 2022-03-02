import datetime as dt
import os
import shutil
import subprocess

from bin.rename import main
from src.rename import construct_new_filename


def test_success_scenario_within_construct_new_filename():
    original_filename = "Screen Shot 2022-02-09 at 20.43.30.png"
    new_filename = construct_new_filename(original_filename)
    assert new_filename == "2022-02-09-20-43-30.png"


def test_failure_scenario_within_construct_new_filename():
    original_filename = "does-not-match-the-function-s-regular-expression-pattern.txt"
    new_filename = construct_new_filename(original_filename)
    assert new_filename is None


def test_failure_scenario_due_to_non_existent_folder():
    #     # Create a temporary directory, one for each test run.
    #     # Create a file in a test

    #     # Arrange.
    #     filename = dt.datetime.utcnow().strftime("%Y-%m-%d-%H-%M-%S.%f")

    #     for f in os.listdir("data"):
    #         shutil.copy(
    #             os.path.join("data", f),
    #             tmp_path / f,
    #         )

    #     print(tmp_path)

    # Act.
    # fmt: off
    c_p: subprocess.CompletedProcess = subprocess.run(
        ["python", "bin/rename.py", "--directory", "non-existent-folder"],
    )
    # fmt: on

    #     # Assert.

    assert c_p.returncode == 1
