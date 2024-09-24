import unittest
import hashlib
import json

from dicewarepy.diceware import wordlist


class TestWordlistIntegrity(unittest.TestCase):
    def test_english_wordlist_integrity(self):
        """The MD5 checksum for the English wordlist must equal to ``5ab3d0bf84ce3164f8c6cfdd0e5957d2``."""
        md5sum = hashlib.md5(json.dumps(wordlist(language="en")).encode()).hexdigest()
        self.assertEqual(md5sum, "5ab3d0bf84ce3164f8c6cfdd0e5957d2")

    def test_german_wordlist_integrity(self):
        """The MD5 checksum for the German wordlist must equal to ``be72f0303f13b04a321f813d67cd5aff``."""
        md5sum = hashlib.md5(json.dumps(wordlist(language="de")).encode()).hexdigest()
        self.assertEqual(md5sum, "be72f0303f13b04a321f813d67cd5aff")


if __name__ == '__main__':
    unittest.main()
