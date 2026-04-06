from unittest.mock import patch

import pytest

from dicewarepy import diceware
from dicewarepy.diceware import wordlist


def test_diceware():
    """The ``diceware`` function must return a list of strings."""
    words = diceware()
    for word in words:
        assert isinstance(word, str)


@pytest.mark.parametrize("language", ["en", "fr", "de", "es"])
def test_diceware_language(language: str):
    """The ``diceware`` function must use the correct wordlist when the language parameter is specified."""
    specified_wordlist = wordlist(language=language)

    words = diceware(language=language)
    for word in words:
        assert word in specified_wordlist.values()


def test_diceware_language_default():
    """The ``diceware`` function must use the English wordlist by default."""
    english_wordlist = wordlist(language="en")

    words = diceware()
    for word in words:
        assert word in english_wordlist.values()


@pytest.mark.parametrize("language", ["EN", "En", "eN"])
def test_diceware_language_case_insensitive(language: str):
    """The ``diceware`` function must treat the language parameter case-insensitively."""
    specified_wordlist = wordlist(language=language)

    words = diceware(language=language)
    for word in words:
        assert word in specified_wordlist.values()


@pytest.mark.parametrize("invalid_language", [1, 1.5, None])
def test_diceware_language_not_string(invalid_language: object):
    """The ``diceware`` function must raise a ``TypeError`` when the language parameter is not a string."""
    with pytest.raises(TypeError):
        diceware(language=invalid_language)  # type: ignore


def test_diceware_language_invalid():
    """The ``diceware`` function must raise a ``ValueError`` when an invalid language code is provided."""
    with pytest.raises(ValueError):
        diceware(language="la")


def test_diceware_length():
    """The ``diceware`` function must return a list of the correct length when the number of words is specified."""
    for i in range(1, 8 + 1):
        words = diceware(n=i)
        assert len(words) == i


def test_diceware_length_default():
    """The ``diceware`` function must return a list of 6 words by default when no number is specified."""
    words = diceware()
    assert len(words) == 6


@pytest.mark.parametrize("invalid_number", [1.5, "one", None])
def test_diceware_number_not_integer(invalid_number: object):
    """The ``diceware`` function must raise a ``TypeError`` when the specified number of words is not an integer."""
    with pytest.raises(TypeError):
        diceware(n=invalid_number)  # type: ignore


def test_diceware_length_less_than_one():
    """The ``diceware`` function must raise a ``ValueError`` when the specified number of words is less than 1."""
    with pytest.raises(ValueError):
        diceware(n=0)
    with pytest.raises(ValueError):
        diceware(n=-5)


def test_diceware_file_not_found():
    """The ``diceware`` function must raise a ``RuntimeError`` when the word list file does not exist."""
    with patch("dicewarepy.diceware.wordlist", side_effect=FileNotFoundError):
        with pytest.raises(RuntimeError):
            diceware()


def test_diceware_runtime_error():
    """The ``diceware`` function must raise a ``RuntimeError`` when an error occurs while reading the word list file."""
    with patch("dicewarepy.diceware.wordlist", side_effect=RuntimeError):
        with pytest.raises(RuntimeError):
            diceware()
