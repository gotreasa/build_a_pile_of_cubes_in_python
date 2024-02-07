import pytest
from modules import build_cube_pile


def describe_find_number():
    def should_give_error_when_not_number():
        """🧪 should error when the input is not a number"""
        with pytest.raises(ValueError, match="❗️ Input should be a number"):
            build_cube_pile.find_number("blah")
