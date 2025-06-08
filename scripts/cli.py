#!/usr/bin/env python3
"""
dicewarepy CLI

A command-line tool for generating Diceware passphrases.

Example:
    python scripts/cli.py -n 8 -l de

Options:
    -n, --number    Number of words in the passphrase (default: 6)
    -l, --language  Language tag of the wordlist (default: en)
"""

import argparse

from dicewarepy import diceware

__author__ = "inwerk"
__copyright__ = "Copyright 2025, inwerk"
__credits__ = ["inwerk"]
__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = "inwerk"
__status__ = "Production"


def main():
    parser = argparse.ArgumentParser(description="generate a Diceware passphrase")
    parser.add_argument(
        "-n",
        "--number",
        dest="number",
        metavar="<number>",
        nargs="?",
        default=6,
        type=int,
        help="desired number of words in the passphrase (defaults to `6`)",
    )
    parser.add_argument(
        "-l",
        "--language",
        dest="language",
        metavar="<language tag>",
        nargs="?",
        default="en",
        type=str,
        help="language tag of the wordlist to select from (defaults to `en`)",
    )

    parsed = parser.parse_args()

    delimiter = " "
    words = diceware(parsed.number, parsed.language)

    print(delimiter.join(words))


if __name__ == "__main__":
    main()
