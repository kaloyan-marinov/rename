from src.utils import construct_new_filename


def test_success_scenario_within_construct_new_filename_1(
    reg_expr_for_macos_screenshot,
):
    original_filename = "Screen Shot 2022-02-09 at 20.43.30.png"
    new_filename = construct_new_filename(
        original_filename,
        reg_expr_for_macos_screenshot,
    )
    assert new_filename == "2022-02-09-20-43-30.png"


def test_success_scenario_within_construct_new_filename_2(
    reg_expr_for_macos_screenshot,
):
    original_filename = "Screen Shot 2022-03-03 at 9.21.21.png"
    new_filename = construct_new_filename(
        original_filename,
        reg_expr_for_macos_screenshot,
    )
    assert new_filename == "2022-03-03-09-21-21.png"


def test_success_scenario_within_construct_new_filename_3(
    reg_expr_for_fedora_screenshot,
):
    original_filename = "Screenshot from 2024-08-15 22-32-31.png"
    new_filename = construct_new_filename(
        original_filename,
        reg_expr_for_fedora_screenshot,
    )
    assert new_filename == "2024-08-15-22-32-31.png"


def test_failure_scenario_within_construct_new_filename(
    reg_expr_for_macos_screenshot,
):
    original_filename = "does-not-match-the-function-s-regular-expression-pattern.txt"
    new_filename = construct_new_filename(
        original_filename,
        reg_expr_for_macos_screenshot,
    )
    assert new_filename is None
