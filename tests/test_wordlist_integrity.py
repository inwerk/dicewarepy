from pathlib import Path

from tests.utils import md5sum


def test_english_wordlist_integrity():
    """The MD5 checksum for the English wordlist must equal to ``fcb9fd13e5f6512a790553aefff54f10``."""
    wordlist_path = Path("src/dicewarepy/wordlists/eff_large_wordlist.txt")
    assert md5sum(wordlist_path) == "fcb9fd13e5f6512a790553aefff54f10"


def test_german_wordlist_integrity():
    """The MD5 checksum for the German wordlist must equal to ``73f3dc62619785f99e7f9e778c0c9476``."""
    wordlist_path = Path("src/dicewarepy/wordlists/de-7776-v1-diceware.txt")
    assert md5sum(wordlist_path) == "73f3dc62619785f99e7f9e778c0c9476"
