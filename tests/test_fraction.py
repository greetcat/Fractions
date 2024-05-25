# tests/test_fraction.py

import unittest
from fraction import Fraction

class TestFraction(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(Fraction(1, 2) + Fraction(1, 3), Fraction(5, 6))
    
    def test_subtraction(self):
        self.assertEqual(Fraction(1, 2) - Fraction(1, 3), Fraction(1, 6))
    
    def test_multiplication(self):
        self.assertEqual(Fraction(1, 2) * Fraction(2, 3), Fraction(1, 3))
    
    def test_division(self):
        self.assertEqual(Fraction(1, 2) / Fraction(1, 3), Fraction(3, 2))

if __name__ == '__main__':
    unittest.main()
