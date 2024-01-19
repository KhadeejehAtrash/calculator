import unittest
from calculator import calculate, validate_expression

class TestCalculator(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(calculate("2+3"), 5)

    def test_subtraction(self):
        self.assertEqual(calculate("5-3"), 2)

    def test_multiplication(self):
        self.assertEqual(calculate("2*3"), 6)

    def test_division(self):
        self.assertEqual(calculate("6/2"), 3)

    def test_complex_expression(self):
        self.assertEqual(calculate("2*(3+4)-5/2"), 13.5)

    def test_invalid_expression(self):
        with self.assertRaises(ValueError):
            validate_expression("2^3")

if __name__ == "__main__":
    unittest.main()

