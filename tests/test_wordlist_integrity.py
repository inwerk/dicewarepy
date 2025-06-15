from pathlib import Path

from tests.utils import md5sum


def test_english_wordlist_integrity():
    """The MD5 checksum for the English wordlist must equal to ``fcb9fd13e5f6512a790553aefff54f10``."""
    wordlist_path = Path("src/dicewarepy/wordlists/eff_large_wordlist.txt")
    assert md5sum(wordlist_path) == "fcb9fd13e5f6512a790553aefff54f10"

def test_french_wordlist_integrity():
    """The MD5 checksum for the French wordlist must equal to ``bb003eac3093c6a730baf71e21f9e9e5``."""
    wordlist_path = Path("src/dicewarepy/wordlists/diceware-fr-alt.txt")
    assert md5sum(wordlist_path) == "bb003eac3093c6a730baf71e21f9e9e5"


def test_german_wordlist_integrity():
    """The MD5 checksum for the German wordlist must equal to ``73f3dc62619785f99e7f9e778c0c9476``."""
    wordlist_path = Path("src/dicewarepy/wordlists/de-7776-v1-diceware.txt")
    assert md5sum(wordlist_path) == "73f3dc62619785f99e7f9e778c0c9476"

def test_spanish_wordlist_integrity():
    """The MD5 checksum for the Spanish wordlist must equal to ``56d95324fa2f75da7d9f838d06f2a681``."""
    wordlist_path = Path("src/dicewarepy/wordlists/DW-es-bonito.txt")
    assert md5sum(wordlist_path) == "56d95324fa2f75da7d9f838d06f2a681"
