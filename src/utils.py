import logging
import re
from typing import Optional


logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)


def construct_new_filename(
    filename: str,
    reg_expr: str,
    debug: bool = False,
) -> Optional[str]:
    """
    Use `reg_expr` as regular expression
    to look for a year, month, day, hour, minute, and second
    within `filename`.

    If all those components are found, construct and return a new filename;
    otherwise, return `None`.
    """

    match = re.search(reg_expr, filename)

    if debug:  # pragma: no cover
        logging.info("")
        logging.info(match)

        if match:
            logging.info("")
            logging.info("the whole match:")
            logging.info(match.group())

            logging.info("group 1:")
            logging.info(match.group(1))
            logging.info("group 2:")
            logging.info(match.group(2))
            logging.info("group 3:")
            logging.info(match.group(3))
            logging.info("group 4:")
            logging.info(match.group(4))
            logging.info("group 5:")
            logging.info(match.group(5))

    if not match:
        return None

    date_yyyy = match.group(1)
    date_mm = match.group(2)
    date_dd = match.group(3)
    hh = match.group(4)
    mm = match.group(5)
    ss = match.group(6)
    ext = match.group(7)

    timestamp_components = [
        date_yyyy,
        date_mm,
        date_dd,
        hh if len(hh) == 2 else "0" + hh,
        mm,
        ss,
    ]
    new_filename = "-".join(timestamp_components) + "." + ext
    return new_filename


if __name__ == "__main__":  # pragma: no cover
    original_filename = "Screen Shot 2022-02-09 at 20.43.30.png"
    new_filename = construct_new_filename(
        original_filename,
        debug=True,
    )
    logging.info(new_filename)  # 2022-02-09-20-43-30.png
