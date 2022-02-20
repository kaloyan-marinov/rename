from src.rename import construct_new_filename


def test_success_scenario_within_construct_new_filename():
    original_filename = "Screen Shot 2022-02-09 at 20.43.30.png"
    new_filename = construct_new_filename(original_filename)
    assert new_filename == "2022-02-09-20-43-30.png"


def test_failure_scenario_within_construct_new_filename():
    original_filename = "does-not-match-the-function-s-regular-expression-pattern.txt"
    new_filename = construct_new_filename(original_filename)
    assert new_filename is None
