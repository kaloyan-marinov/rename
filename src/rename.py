import argparse
import logging
import os
import sys

from src.utils import construct_new_filename


logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)


def main():
    a_p = argparse.ArgumentParser(
        "Rename each 'file containing a timestamp' to `%Y-%m-%d-%H-%M-%S`"
    )
    a_p.add_argument(
        "-d",
        "--directory",
        required=True,
    )
    a_p.add_argument(
        "-re",
        "--regular-expression",
        required=True,
        help="regular expression for timestamp",
    )

    args = a_p.parse_args()
    directory = args.directory
    regular_expression = args.regular_expression

    if not os.path.exists(directory):
        logging.info(
            "there doesn't exist a directory at '%s'; aborting!",
            directory,
        )
        sys.exit(1)

    if not os.path.isdir(directory):
        logging.info(
            "'%s' exists but is not a directory; aborting!",
            directory,
        )
        sys.exit(2)

    logging.info(
        "beginning to loop through the contents of the following folder %s",
        directory,
    )
    for dir_entry in os.listdir(directory):
        logging.info("processing '%s'", dir_entry)

        source = os.path.join(directory, dir_entry)

        if not os.path.isfile(source):
            logging.info(4 * " " + "not a file - skipping")
            continue
        else:
            new_filename = construct_new_filename(
                dir_entry,
                regular_expression,
            )

            if new_filename is None:
                logging.info(
                    4 * " "
                    + "did not find a match (for the regular expression '%s')"
                    + " - skipping",
                    regular_expression,
                )
                continue

            target = os.path.join(directory, new_filename)

            if dir_entry == new_filename:
                logging.info(
                    4 * " " + "'dir_entry' and 'new_filename' are equal - skipping"
                )
                continue

            if os.path.exists(target):
                logging.info(
                    4 * " " + "there already exists a file at '%s' - aborting", target
                )
                sys.exit(1)

            logging.info(4 * " " + "renaming the file to '%s'", new_filename)
            os.rename(source, target)


if __name__ == "__main__":
    main()
