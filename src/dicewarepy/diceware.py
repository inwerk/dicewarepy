import csv
import secrets

from functools import lru_cache

from importlib import resources

DICE: list[str] = ["1", "2", "3", "4", "5", "6"]
DICE_ROLLS_PER_WORD: int = 5

WORDLISTS: dict[str, str] = {
    "de": "de-7776-v1-diceware.txt",
    "en": "eff_large_wordlist.txt",
    "es": "DW-es-bonito.txt",
    "fr": "diceware-fr-alt.txt",
}

SUPPORTED_LANGUAGES: list[str] = list(WORDLISTS.keys())


def dice(n: int = 1) -> str:
    """
    Simulate the rolling of one or multiple six-faced dice.

    :param n: the number of dice to simulate. Must be greater than or equal to 1.
    :returns: a sequence of ``n`` random numbers between 1 and 6.
    :raises TypeError: if ``n`` is not an integer.
    :raises ValueError: if ``n`` is less than 1.
    """

    if not isinstance(n, int):
        raise TypeError(f"Parameter n must be an integer, but is {type(n)}.")

    if n < 1:
        raise ValueError(f"Parameter n must be greater than or equal to 1, but is {n}.")

    dice_results: list[str] = []

    # Roll the dice ``n`` times.
    for _ in range(n):
        dice_results.append(secrets.choice(DICE))

    return "".join(dice_results)


@lru_cache(maxsize=len(SUPPORTED_LANGUAGES))
def wordlist(language: str = "en") -> dict[str, str]:
    """
    Read text files containing a Diceware word list and return a dictionary of those words.\n
    Currently supported languages: ``de``, ``en``, ``es`` and ``fr``.

    :param language: the language tag assigned to a specific inbuilt word list.
    :returns: a Diceware wordlist as dictionary.
    :raises ValueError: if the specified language is not supported.
    :raises TypeError: if ``language`` is not a string.
    :raises FileNotFoundError: if the word list file does not exist.
    :raises RuntimeError: if an error occurs while reading the word list file.
    """

    if not isinstance(language, str):
        raise TypeError(
            f"Parameter language must be a string, but is {type(language)}."
        )

    if language not in SUPPORTED_LANGUAGES:
        raise ValueError(
            f"Language {language} not supported. Supported languages: {', '.join(SUPPORTED_LANGUAGES)}."
        )

    ret_wordlist: dict[str, str] = {}

    # Open the word list and index each word by its key.
    filename = WORDLISTS[language]
    try:
        file_path = resources.files("dicewarepy.wordlists").joinpath(filename)
        with file_path.open("r") as file:
            reader = csv.DictReader(file, fieldnames=["key", "word"], delimiter="\t")
            for row in reader:
                ret_wordlist[row["key"]] = row["word"]
    except FileNotFoundError as e:
        raise FileNotFoundError(
            f"The word list file {filename} does not exist in the package."
        ) from e
    except Exception as e:
        raise RuntimeError(
            f"An error occurred while reading the word list file {filename}: {e}"
        ) from e

    return ret_wordlist


def diceware(n: int = 6, language: str = "en") -> list[str]:
    """
    Function implementing the Diceware method for passphrase generation.\n
    For each word in the passphrase, five rolls of a six-faced dice are required.
    The numbers from 1 to 6 that come up in the rolls are assembled as a five-digit number.
    That number is then used to look up a word in a cryptographic word list.\n
    A minimum of 6 words is recommended for passphrases.

    :param n: the desired number of words to generate. Must be greater than or equal to 1.
    :param language: the language tag assigned to a specific inbuilt word list. Currently supported languages: ``de``, ``en``, ``es`` and ``fr``.
    :returns: a list of ``n`` randomly selected words from a Diceware word list.
    :raises TypeError: if ``n`` is not an integer or if ``language`` is not a string.
    :raises ValueError: if ``n`` is less than 1 or if the specified language is not supported.
    :raises RuntimeError: if an error occurs while retrieving the word list file.
    """

    if not isinstance(n, int):
        raise TypeError(f"Parameter n must be an integer, but is {type(n)}.")

    if n < 1:
        raise ValueError(f"Parameter n must be greater than or equal to 1, but is {n}.")

    if not isinstance(language, str):
        raise TypeError(
            f"Parameter language must be a string, but is {type(language)}."
        )

    if language not in SUPPORTED_LANGUAGES:
        raise ValueError(
            f"Language {language} not supported. Supported languages: {', '.join(SUPPORTED_LANGUAGES)}."
        )

    # Retrieve the Diceware word list corresponding to the specified language.
    try:
        diceware_wordlist: dict[str, str] = wordlist(language=language)
    except (FileNotFoundError, RuntimeError) as e:
        raise RuntimeError(
            f"An error occurred while retrieving the word list for language {language}: {e}"
        ) from e

    words: list[str] = []

    # Generate ``n`` words.
    for _ in range(n):
        dice_results: str = dice(n=DICE_ROLLS_PER_WORD)
        words.append(diceware_wordlist[dice_results])

    return words
