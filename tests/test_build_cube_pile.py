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
