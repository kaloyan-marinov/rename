import os
import shutil
import subprocess


os.environ["PYTHONPATH"] = os.path.realpath(
    os.path.join(os.path.basename(__file__), "..")
)


def test_rename_1_failure():
    """
    Test the scenario of the script crashing
    due to the value provided to `--directory` being non-existent.
    """

    # Arrange.
    command = [
        "python",
        "src/rename.py",
        "--directory",
        "non-existent-directory",
        "--regular-expression",
        "this-value-does-not-matter-for-this-test",
    ]

    # Act.
    c_p: subprocess.CompletedProcess = subprocess.run(command)

    # Assert.
    assert c_p.returncode == 1


def test_rename_2_failure():
    """
    Test the scenario of the script crashing
    due to the value provided to `--directory` not being a directory.
    """

    # Arrange.
    command = [
        "python",
        "src/rename.py",
        "--directory=README.md",
    ]

    # Act.
    c_p: subprocess.CompletedProcess = subprocess.run(command)

    # Assert.
    assert c_p.returncode == 2


def test_rename_3_success(
    tmp_path,
    reg_expr_for_macos_screenshot,
):
    """
    Create a temporary directory, one for each run of this test case.
    """

    # Arrange.
    shutil.copytree(
        "data",
        tmp_path,
        dirs_exist_ok=True,
    )

    command = [
        "python",
        "src/rename.py",
        "--directory",
        tmp_path,
        "--regular-expression",
        reg_expr_for_macos_screenshot,
    ]

    # Act.
    c_p: subprocess.CompletedProcess = subprocess.run(command)

    # Assert.
    assert c_p.returncode == 0

    assert {dir_entry for dir_entry in os.listdir(tmp_path)} == {
        "these-files-should-not-be-modified",
        "2022-02-09-20-43-30.txt",
        "2022-02-09-20-43-33.txt",
        "2022-03-03-08-21-21.txt",
    }

    assert {
        dir_entry
        for dir_entry in os.listdir(tmp_path / "these-files-should-not-be-modified")
    } == {"Screen Shot 2022-03-06 at 10.41.57.txt"}
