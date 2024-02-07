import pytest
from modules import build_cube_pile


def describe_find_number():
    def should_give_error_when_not_number():
        """🧪 should error when the input is not a number"""
        with pytest.raises(ValueError, match="❗️ Input should be a number"):
            build_cube_pile.find_number("blah")

    def should_give_1_when_input_1():
        """🧪 should give 1 when the input is 1"""
        assert build_cube_pile.find_number(1) == 1

    def should_give_2_when_input_9():
        """🧪 should give 2 when the input is 9"""
        assert build_cube_pile.find_number(9) == 2

    def should_give_3_when_input_36():
        """🧪 should give 3 when the input is 36"""
        assert build_cube_pile.find_number(36) == 3

    def should_give_45_when_input_1071225():
        """🧪 should give 45 when the input is 1071225"""
        assert build_cube_pile.find_number(1071225) == 45

    def should_give_negative_1_when_input_91716553919377():
        """🧪 should give -1 when the input is 91716553919377"""
        assert build_cube_pile.find_number(91716553919377) == -1

    def should_give_negative_1_when_input_8():
        """🧪 should give -1 when the input is 8"""
        assert build_cube_pile.find_number(8) == -1

    def should_give_negative_1_when_input_37():
        """🧪 should give -1 when the input is 37"""
        assert build_cube_pile.find_number(37) == -1
