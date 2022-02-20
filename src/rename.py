import re
from typing import Optional


def construct_new_filename(
    filename: str,
    debug: bool = False,
) -> Optional[str]:

    match = re.search(r"(\d+-\d+-\d+) at (\d+).(\d+).(\d+).(\w+)", filename)

    if debug:
        print()
        print(match)

        if match:
            print()
            print("the whole match:")
            print(match.group())

            print("group 1:")
            print(match.group(1))
            print("group 2:")
            print(match.group(2))
            print("group 3:")
            print(match.group(3))
            print("group 4:")
            print(match.group(4))
            print("group 5:")
            print(match.group(5))

    if not match:
        return None

    yyyy_mm_dd = match.group(1)
    hh = match.group(2)
    mm = match.group(3)
    ss = match.group(4)
    ext = match.group(5)
    new_filename = "-".join([yyyy_mm_dd, hh, mm, ss]) + "." + ext
    return new_filename


if __name__ == "__main__":
    original_filename = "Screen Shot 2022-02-09 at 20.43.30.png"
    new_filename = construct_new_filename(
        original_filename,
        debug=True,
    )
    print(new_filename)
