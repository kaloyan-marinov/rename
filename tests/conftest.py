"""
According to
https://docs.pytest.org/en/7.1.x/reference/fixtures.html#conftest-py-sharing-fixtures-across-multiple-files :

PyTest fixtures defined in this file
can be used by any test in the same package
without needing to import them.
(They will be discovered/resolved automatically by the `pytest` binary.)
"""

import pytest


@pytest.fixture
def reg_expr_for_macos_screenshot():
    return r"(\d+)-(\d+)-(\d+) at (\d+).(\d+).(\d+).(\w+)"


@pytest.fixture
def reg_expr_for_fedora_screenshot():
    return r"(\d+)-(\d+)-(\d+) (\d+)-(\d+)-(\d+).(\w+)"
