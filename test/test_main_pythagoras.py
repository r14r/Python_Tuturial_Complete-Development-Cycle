import pytest

from main import pythagoras


def test_sqr():
    assert pythagoras(3,4) == 5 * 5
    