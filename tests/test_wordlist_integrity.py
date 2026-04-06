from pathlib import Path

import pytest

from tests.utils import md5sum


@pytest.mark.parametrize(
    "wordlist, expected_checksum",
    [
        (
            "src/dicewarepy/wordlists/eff_large_wordlist.txt",
            "fcb9fd13e5f6512a790553aefff54f10",
        ),
        (
            "src/dicewarepy/wordlists/diceware-fr-alt.txt",
            "bb003eac3093c6a730baf71e21f9e9e5",
        ),
        (
            "src/dicewarepy/wordlists/de-7776-v1-diceware.txt",
            "73f3dc62619785f99e7f9e778c0c9476",
        ),
        (
            "src/dicewarepy/wordlists/DW-es-bonito.txt",
            "80905d54a881313886f415506beade02",
        ),
    ],
)
def test_wordlist_integrity(wordlist: str, expected_checksum: str):
    """The MD5 checksum for each wordlist must equal to the expected value."""
    wordlist_path = Path(wordlist)
    assert md5sum(wordlist_path) == expected_checksum
