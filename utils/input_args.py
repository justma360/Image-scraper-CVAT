import logging
import os
import sys
import argparse
import logging

from utils import createCipheriv

from dotenv import dotenv_values

config = dotenv_values(".env")

try:
    VERBOSE_LEVEL = int(config["VERBOSE"])
except Exception as e:
    print("No .env file given")
    VERBOSE_LEVEL = 1


__CWD_DIR__ = os.path.abspath(os.getcwd())
__SCRIPT_DIR__ = os.path.dirname(os.path.abspath(__file__))


def parse_arguments():
    """Read arguments from a command line."""
    parser = argparse.ArgumentParser(description="Arguments get parsed via --commands")
    parser.add_argument(
        "-v",
        metavar="--verbosity",
        type=int,
        required=False,
        default=VERBOSE_LEVEL,
        help="Verbosity of logging: 0 -critical, 1- error, 2 -warning, 3 -info, 4 -debug",
    )
    parser.add_argument(
        "-help",  # Tag to add to the parse
        metavar="--Help",
        required=False,
        default="Here is a default text",
        help="Returns help information",
    )
    parser.add_argument(
        "-cwd",
        metavar="--directory",
        required=False,
        default=__CWD_DIR__,
        help="Prints the current directory",
    )
    parser.add_argument(
        "-search",
        metavar="--search",
        nargs="+",
        required=True,
        default=[],
        help="List of search items",
    )

    args = parser.parse_args()

    verbose = {
        0: logging.CRITICAL,
        1: logging.ERROR,
        2: logging.WARNING,
        3: logging.INFO,
        4: logging.DEBUG,
    }
    logging.basicConfig(
        format="%(asctime)s | %(levelname)s: %(message)s",
        level=verbose[args.v],
        stream=sys.stdout,
    )
    logging.info(f"Logging level is at {args.v}")

    return args
