import pytest
from unittest import TestCase


# content of test_sample.py
def f():
    raise SystemExit(1)


def func(x):
    return x + 1


class TestClass(TestCase):
class TestClass:
    def test_answer(self):
        assert func(4) == 5

    def test_mytest(self):
        with pytest.raises(SystemExit):
            f()
