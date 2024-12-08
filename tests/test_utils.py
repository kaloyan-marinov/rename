from src.utils import construct_new_filename


def test_construct_new_filename_1_success_scenario(
    reg_expr_for_macos_screenshot,
):
    # Arrange.
    original_filename = "Screen Shot 2022-02-09 at 20.43.30.png"

    # Act.
    new_filename = construct_new_filename(
        original_filename,
        reg_expr_for_macos_screenshot,
    )

    # Assert.
    assert new_filename == "2022-02-09-20-43-30.png"


def test_construct_new_filename_2_success_scenario(
    reg_expr_for_macos_screenshot,
):
    # Arrange.
    original_filename = "Screen Shot 2022-03-03 at 9.21.21.png"

    # Act.
    new_filename = construct_new_filename(
        original_filename,
        reg_expr_for_macos_screenshot,
    )

    # Assert.
    assert new_filename == "2022-03-03-09-21-21.png"


def test_construct_new_filename_3_success_scenario(
    reg_expr_for_fedora_screenshot,
):
    # Arrange.
    original_filename = "Screenshot from 2024-08-15 22-32-31.png"

    # Act.
    new_filename = construct_new_filename(
        original_filename,
        reg_expr_for_fedora_screenshot,
    )

    # Assert.
    assert new_filename == "2024-08-15-22-32-31.png"


def test_construct_new_filename_4_failure_scenario(
    reg_expr_for_macos_screenshot,
):
    # Arrange.
    original_filename = "does-not-match-the-function-s-regular-expression-pattern.txt"

    # Act.
    new_filename = construct_new_filename(
        original_filename,
        reg_expr_for_macos_screenshot,
    )

    # Assert.
    assert new_filename is None
