#!/usr/bin/env python
""" diceware.py: Educational script for diceware passphrase generation.

This script provides functionality for generating secure passphrases using the Diceware method.
It simulates the rolling of dice to create a sequence of numbers, which are then used to
select words from a predefined word list.

Key features include:
- simulating the rolling of dice,
- reading and returning words from Diceware word lists,
- simulating the Diceware method for passphrase generation.
"""

import csv
import os
import secrets

__author__ = "inwerk"
__copyright__ = "Copyright 2024, inwerk"
__credits__ = ["inwerk"]
__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = "inwerk"
__status__ = "Production"


def dice(n: int = 1) -> str:
    """
    Simulate the rolling of one or multiple six-faced dice.\n
    This function will generate random numbers between 1 and 6 (including both 1 and 6).

    :param n: The number of dice to simulate. Must be greater than or equal to 1.
    :return: A sequence of ``n`` random numbers between 1 and 6.
    """

    # Check whether ``n`` is not within the permitted range.
    if n < 1:
        # If ``n`` is not within the permitted range, raise a ``ValueError``.
        raise ValueError(f'Parameter n must be greater than or equal to 1, but is {n}.')

    # String representing the sequence of dice results.
    dice_results = ""

    # Roll the dice ``n`` times.
    for i in range(n):
        # Append a randomly chosen element from an integer sequence representing a six-faced dice to the dice results.
        dice_results += secrets.choice(["1", "2", "3", "4", "5", "6"])

    # Return the sequence of dice results.
    return dice_results


def wordlist(language: str = "en") -> dict:
    """
    Read text files containing a Diceware word list and return a dictionary of those words.\n
    Currently supported languages: ``en`` and ``de``.\n
    ``en``: https://www.eff.org/document/passphrase-wordlists\n
    ``de``: https://github.com/dys2p/wordlists-de

    :param language: The language assigned to a specific inbuilt word list.
    :return: A Diceware wordlist as dictionary.
    """

    # Path to the word list text files.
    file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'wordlists')) + "/"

    # Check the value of ``language`` against different predefined cases.
    match language:
        # If ``language`` is ``en`` append the file name for the English word list to the ``file_path``.
        case "en":
            file_path += "eff_large_wordlist.txt"
        # If ``language`` is ``de`` append the file name for the German word list to the ``file_path``.
        case "de":
            file_path += "de-7776-v1-diceware.txt"
        # If ``language`` does not match any supported language raise a ``ValueError``.
        case _:
            raise ValueError(f'Language {language} not supported.')

    # Dictionary for the selected Diceware wordlist.
    ret_wordlist = dict([])

    # Open the Diceware word list text file in read mode.
    with open(file_path, "r") as file:
        # Read the file. Columns are tab-delimited. The first column contains the IDs,
        # the second column contains the corresponding words.
        reader = csv.DictReader(file, fieldnames=["id", "word"], delimiter="\t")

        # Iterate through the lines of the word list.
        for row in reader:
            # Index each Diceware word by its ID.
            # TODO https://youtrack.jetbrains.com/issue/PY-60440/False-positive-for-csv.DictReader-indexing
            ret_wordlist[row["id"]] = row["word"]

    # Return the dictionary containing the Diceware word list.
    return ret_wordlist


def diceware(n: int = 6, language: str = "en") -> list:
    """
    Function implementing the Diceware method for passphrase generation.\n
    For each word in the passphrase, five rolls of a six-faced dice are required.
    The numbers from 1 to 6 that come up in the rolls are assembled as a five-digit number.
    That number is then used to look up a word in a cryptographic word list.\n
    A minimum of 6 words is recommended for passphrases.

    :param n: The desired number of words to generate. Must be greater than or equal to 1.
    :param language: Currently supported languages: ``en`` and ``de``.
    :return: A list of ``n`` randomly selected words from a Diceware word list.
    """

    # Check whether ``n`` is not within the permitted range.
    if n < 1:
        # If ``n`` is not within the permitted range, raise a ``ValueError``.
        raise ValueError(f'Parameter n must be greater than or equal to 1, but is {n}.')

    # Retrieve the Diceware word list corresponding to the specified language.
    diceware_wordlist = wordlist(language=language)

    # List of randomly selected words.
    words = []

    # Generate ``n`` words.
    for i in range(n):
        # Roll five dice.
        dice_results = dice(n=5)

        # Append a randomly selected word to the list.
        words.append(diceware_wordlist[dice_results])

    # Return the list of ``n`` randomly selected words from the Diceware wordlist.
    return words


if __name__ == "__main__":
    pass
