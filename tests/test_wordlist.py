import pytest

from dicewarepy.diceware import wordlist

from unittest.mock import patch


@pytest.fixture(autouse=True)
def clear_wordlist_cache():
    wordlist.cache_clear()


def test_wordlist():
    """The ``wordlist`` function must return a dictionary and its entries must be strings."""
    assert isinstance(wordlist(), dict)
    for entry in wordlist():
        assert isinstance(entry, str)


def test_wordlist_length():
    """The length of the wordlist must be 7776 entries."""
    assert len(wordlist(language="en")) == 7776


def test_wordlist_language_english():
    """The English wordlist must return the correct word for a given key."""
    assert wordlist(language="en")["53434"] == "security"


def test_wordlist_language_english_length():
    """The length of the English wordlist must be 7776 entries."""
    assert len(wordlist(language="en")) == 7776

def test_wordlist_language_french():
    """The French wordlist must return the correct word for a given key."""
    assert wordlist(language="fr")["24363"] == "cube"

def test_wordlist_language_french_length():
    """The length of the French wordlist must be 7776 entries."""
    assert len(wordlist(language="fr")) == 7776


def test_wordlist_language_german():
    """The German wordlist must return the correct word for a given key."""
    assert wordlist(language="de")["16622"] == "bombensicher"


def test_wordlist_language_german_length():
    """The length of the German wordlist must be 7776 entries."""
    assert len(wordlist(language="de")) == 7776


def test_wordlist_language_spanish():
    """The Spanish wordlist must return the correct word for a given key."""
    assert wordlist(language="es")["62354"] == "seguridad"

def test_wordlist_language_spanish_length():
    """The length of the Spanish wordlist must be 7776 entries."""
    assert len(wordlist(language="es")) == 7776


def test_wordlist_language_default():
    """The default wordlist must be English."""
    assert wordlist()["53434"] == "security"


def test_wordlist_language_not_string():
    """The ``wordlist`` function must raise a TypeError when the language is not a string."""
    with pytest.raises(TypeError):
        wordlist(language=1)  # type: ignore
    with pytest.raises(TypeError):
        wordlist(language=1.5)  # type: ignore
    with pytest.raises(TypeError):
        wordlist(language=None)  # type: ignore


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
