"""
Unit tests for the basic math library
"""

import basic_math


class TestCalculator:

    def test_addition(self):
        assert 4 == basic_math.add(2, 2)

    def test_subtraction(self):
        assert 2 == basic_math.subtract(4, 2)

    def test_multiplication(self):
        assert 100 == basic_math.multiply(10, 10)