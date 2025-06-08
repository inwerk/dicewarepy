import pytest

from dicewarepy.diceware import dice


def test_dice():
    """The ``dice`` function must return a sequence of integers parsed into strings."""
    dice_results = dice()
    for result in dice_results:
        assert isinstance(result, str)
        assert isinstance(int(result), int)


def test_dice_range():
    """The results of the ``dice`` function must be within the valid range (1 to 6)."""
    dice_results = dice()
    for result in dice_results:
        assert 1 <= int(result) <= 6


def test_dice_number():
    """The number of results returned by the ``dice`` function must match the requested number."""
    for i in range(1, 16 + 1):
        dice_results = dice(n=i)
        assert len(dice_results) == i


def test_dice_number_default():
    """The default number of dice rolled must be 1."""
    dice_results = dice()
    assert len(dice_results) == 1


def test_dice_number_not_integer():
    """The ``dice`` function must raise a ``TypeError`` when the number of dice is not an integer."""
    with pytest.raises(TypeError):
        dice(n=1.5)  # type: ignore
    with pytest.raises(TypeError):
        dice(n="one")  # type: ignore
    with pytest.raises(TypeError):
        dice(n=None)  # type: ignore


def test_dice_number_less_than_one():
    """The ``dice`` function must raise a ``ValueError`` when the number of dice is less than 1."""
    with pytest.raises(ValueError):
        dice(n=0)
    with pytest.raises(ValueError):
        dice(n=-5)
