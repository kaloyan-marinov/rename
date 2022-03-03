import logging
import re
from typing import Optional


logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)


def construct_new_filename(
    filename: str,
    debug: bool = False,
) -> Optional[str]:

    match = re.search(r"(\d+-\d+-\d+) at (\d+).(\d+).(\d+).(\w+)", filename)

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

    yyyy_mm_dd = match.group(1)
    hour = match.group(2)
    mm = match.group(3)
    ss = match.group(4)
    ext = match.group(5)
    new_filename = (
        "-".join(
            [
                yyyy_mm_dd,
                hour if len(hour) == 2 else "0" + hour,
                mm,
                ss,
            ]
        )
        + "."
        + ext
    )
    return new_filename


if __name__ == "__main__":  # pragma: no cover
    original_filename = "Screen Shot 2022-02-09 at 20.43.30.png"
    new_filename = construct_new_filename(
        original_filename,
        debug=True,
    )
    logging.info(new_filename)  # 2022-02-09-20-43-30.png
