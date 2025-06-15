import pytest

from dicewarepy import diceware
from dicewarepy.diceware import wordlist

from unittest.mock import patch


def test_diceware():
    """The ``diceware`` function must return a list of strings."""
    words = diceware()
    for word in words:
        assert isinstance(word, str)


def test_diceware_default_language():
    """The ``diceware`` function must use the English wordlist by default."""
    english_wordlist = wordlist(language="en")

    words = diceware()
    for word in words:
        assert word in english_wordlist.values()


def test_diceware_language_english():
    """The ``diceware`` function must use the English wordlist when the language parameter is set to ``en``."""
    english_wordlist = wordlist(language="en")

    words = diceware(language="en")
    for word in words:
        assert word in english_wordlist.values()


def test_diceware_language_french():
    """The ``diceware`` function must use the French wordlist when the language parameter is set to ``fr``."""
    french_wordlist = wordlist(language="fr")

    words = diceware(language="fr")
    for word in words:
        assert word in french_wordlist.values()


def test_diceware_language_german():
    """The ``diceware`` function must use the German wordlist when the language parameter is set to ``de``."""
    german_wordlist = wordlist(language="de")

    words = diceware(language="de")
    for word in words:
        assert word in german_wordlist.values()

def test_diceware_language_spanish():
    """The ``diceware`` function must use the Spanish wordlist when the language parameter is set to ``es``."""
    spanish_wordlist = wordlist(language="es")

    words = diceware(language="es")
    for word in words:
        assert word in spanish_wordlist.values()


def test_diceware_language_not_string():
    """The ``diceware`` function must raise a ``TypeError`` when the language parameter is not a string."""
    with pytest.raises(TypeError):
        diceware(language=1)  # type: ignore
    with pytest.raises(TypeError):
        diceware(language=1.5)  # type: ignore
    with pytest.raises(TypeError):
        diceware(language=None)  # type: ignore


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


def test_diceware_number_not_integer():
    """The ``diceware`` function must raise a ``TypeError`` when the specified number of words is not an integer."""
    with pytest.raises(TypeError):
        diceware(n=1.5)  # type: ignore
    with pytest.raises(TypeError):
        diceware(n="one")  # type: ignore
    with pytest.raises(TypeError):
        diceware(n=None)  # type: ignore


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
