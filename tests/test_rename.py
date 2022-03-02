import os
import shutil
import subprocess

from src.rename import construct_new_filename


def test_success_scenario_within_construct_new_filename():
    original_filename = "Screen Shot 2022-02-09 at 20.43.30.png"
    new_filename = construct_new_filename(original_filename)
    assert new_filename == "2022-02-09-20-43-30.png"


def test_failure_scenario_within_construct_new_filename():
    original_filename = "does-not-match-the-function-s-regular-expression-pattern.txt"
    new_filename = construct_new_filename(original_filename)
    assert new_filename is None


def test_failure_scenario_due_to_non_existent_directory():
    # Arrange.
    command = [
        "python",
        "bin/rename.py",
        "--directory",
        "non-existent-directory",
    ]

    # Act.
    c_p: subprocess.CompletedProcess = subprocess.run(command)

    # Assert.
    assert c_p.returncode == 1


def test_failure_scenario_due_to_not_a_directory():
    # Arrange.
    command = [
        "python",
        "bin/rename.py",
        "--directory=README.md",
    ]

    # Act.
    c_p: subprocess.CompletedProcess = subprocess.run(command)

    # Assert.
    assert c_p.returncode == 2


def test_success_scenario(tmp_path):
    """
    Create a temporary directory, one for each run of this test case.
    """

    # Arrange.
    for f in os.listdir("data"):
        shutil.copy(
            os.path.join("data", f),
            tmp_path / f,
        )

    command = [
        "python",
        "bin/rename.py",
        "--directory",
        tmp_path,
    ]

    # Act.
    c_p: subprocess.CompletedProcess = subprocess.run(command)

    # Assert.
    assert c_p.returncode == 0

    assert set(os.listdir(tmp_path)) == {
        "2022-02-09-20-43-30.txt",
        "2022-02-09-20-43-33.txt",
        "2022-02-09-20-43-38.txt",
    }
