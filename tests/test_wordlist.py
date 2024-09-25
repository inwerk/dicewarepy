import unittest

from dicewarepy.diceware import wordlist

class TestWordlist(unittest.TestCase):
    def test_wordlist(self):
        """The ``wordlist`` function must return a dictionary and its entries must be strings."""
        self.assertIsInstance(wordlist(), dict)
        for entry in wordlist():
            self.assertIsInstance(entry, str)

    def test_wordlist_length(self):
        """The length of the wordlist must be 7776 entries."""
        self.assertEqual(len(wordlist(language="en")), 7776)

    def test_wordlist_language_english(self):
        """The English wordlist must return the correct word for a given key."""
        self.assertEqual(wordlist(language="en")["53434"], "security")

    def test_wordlist_language_english_length(self):
        """The length of the English wordlist must be 7776 entries."""
        self.assertEqual(len(wordlist(language="en")), 7776)

    def test_wordlist_language_german(self):
        """The German wordlist must return the correct word for a given key."""
        self.assertEqual(wordlist(language="de")["16622"], "bombensicher")

    def test_wordlist_language_german_length(self):
        """The length of the German wordlist must be 7776 entries."""
        self.assertEqual(len(wordlist(language="de")), 7776)

    def test_wordlist_language_default(self):
        """The default wordlist must be English."""
        self.assertEqual(wordlist()["53434"], "security")

    def test_wordlist_language_invalid(self):
        """The ``wordlist`` function must raise a ValueError for an invalid language tag."""
        self.assertRaises(ValueError, wordlist, language='la')


if __name__ == '__main__':
    unittest.main()
