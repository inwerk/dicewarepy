import unittest

from dicewarepy.diceware import dice

class TestDice(unittest.TestCase):
    def test_dice(self):
        """The ``dice`` function must return a list of integers parsed into strings."""
        dice_results = dice()
        for result in dice_results:
            self.assertIsInstance(result, str)
            self.assertIsInstance(int(result), int)

    def test_dice_range(self):
        """The results of the ``dice`` function must be within the valid range (1 to 6)."""
        dice_results = dice(n=128)
        for result in dice_results:
            self.assertTrue(1 <= int(result) <= 6)

    def test_dice_number(self):
        """The number of results returned by the ``dice`` function must match the requested number."""
        for i in range(1, 5+1):
            dice_results = dice(n=i)
            self.assertEqual(len(dice_results), i)

    def test_dice_number_default(self):
        """The default number of dice rolled must be 1."""
        dice_results = dice()
        self.assertEqual(len(dice_results), 1)

    def test_dice_number_less_than_one(self):
        """The ``dice`` function must raise a ``ValueError`` when the number of dice is less than 1."""
        self.assertRaises(ValueError, dice, n=0)
        self.assertRaises(ValueError, dice, n=-5)

if __name__ == '__main__':
    unittest.main()
