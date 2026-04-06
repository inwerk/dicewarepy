import itertools
from unittest.mock import patch

import pytest

from dicewarepy.diceware import wordlist


@pytest.fixture(autouse=True)
def clear_wordlist_cache():
    wordlist.cache_clear()


@pytest.mark.parametrize("language", ["en", "fr", "de", "es"])
def test_wordlist(language):
    """The ``wordlist`` function must return a dictionary and its entries must be strings."""
    wordlist_dict = wordlist(language)
    assert isinstance(wordlist_dict, dict)
    for entry in wordlist_dict:
        assert isinstance(entry, str)


@pytest.mark.parametrize("language", ["en", "fr", "de", "es"])
def test_wordlist_length(language):
    """The wordlist must contain 7776 entries."""
    assert len(wordlist(language=language)) == 7776


@pytest.mark.parametrize("language", ["en", "fr", "de", "es"])
def test_wordlist_keys(language):
    """The wordlist must contain all keys from 11111 to 66666 in insertion order, each 5 digits long and only digits 1-6."""
    wordlist_dict = wordlist(language=language)
    expected_keys = ["".join(p) for p in itertools.product("123456", repeat=5)]
    actual_keys = list(wordlist_dict.keys())
    assert actual_keys == expected_keys


@pytest.mark.parametrize(
    "language, key, expected_word",
    [
        ("en", "53434", "security"),
        ("fr", "24363", "cube"),
        ("de", "16622", "bombensicher"),
        ("es", "62354", "seguridad"),
    ],
)
def test_wordlist_expected_words(language: str, key: str, expected_word: str):
    """Each wordlist must return the correct word for a given key."""
    assert wordlist(language=language)[key] == expected_word


def test_wordlist_language_default():
    """The ``wordlist`` function must use the English wordlist by default."""
    assert wordlist()["53434"] == "security"


@pytest.mark.parametrize("language", ["EN", "En", "eN"])
def test_wordlist_language_case_insensitive(language: str):
    """The ``wordlist`` function must treat the language parameter case-insensitively."""
    assert wordlist(language=language)["53434"] == "security"


@pytest.mark.parametrize("invalid_language", [1, 1.5, None])
def test_wordlist_language_not_string(invalid_language: object):
    """The ``wordlist`` function must raise a TypeError when the language is not a string."""
    with pytest.raises(TypeError):
        wordlist(language=invalid_language)


def test_wordlist_language_invalid():
    """The ``wordlist`` function must raise a ValueError for an invalid language tag."""
    with pytest.raises(ValueError):
        wordlist(language="la")


def test_wordlist_file_not_found():
    """The ``wordlist`` function must raise a FileNotFoundError if the word list file does not exist."""
    with patch("importlib.resources.files") as mock_files:
        mock_files.return_value.joinpath.return_value.open.side_effect = (
            FileNotFoundError
        )
        with pytest.raises(FileNotFoundError):
            wordlist()


def test_wordlist_runtime_error():
    """The ``wordlist`` function must raise a RuntimeError if an error occurs while reading the word list file."""
    with patch("dicewarepy.diceware.csv.DictReader", side_effect=OSError):
        with pytest.raises(RuntimeError):
            wordlist()


def test_wordlist_cache():
    """The ``wordlist`` function must cache the word list after the first call."""
    with patch("importlib.resources.files") as mock_files:
        # First call to wordlist should read the file and cache it.
        wordlist(language="en")
        mock_files.assert_called_once()

        # Second call to wordlist should use the cache and not read the file again.
        wordlist(language="en")
        mock_files.assert_called_once()  # still only called once
