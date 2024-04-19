import sys
import os
current_dir = os.path.dirname(os.path.abspath(__file__))
calculator_dir = os.path.join(current_dir, '..') 
if calculator_dir not in sys.path:
    sys.path.append(calculator_dir)

from calculator import subtract, divide

import unittest
from calculator import subtract, divide

class TestCalculator(unittest.TestCase):
    def test_subtract(self):
        self.assertEqual(subtract(8, 3), 5)
        self.assertEqual(subtract(-1, 1), -2)
        self.assertEqual(subtract(-1, -1), 0)
        self.assertEqual(subtract(-5, 0), -5)
        self.assertEqual(subtract(4, 0), 4)

    def test_divide(self):
        self.assertEqual(divide(8, 2), 4)
        self.assertEqual(divide(5, 2), 2.5)
        self.assertEqual(divide(10, 3), 10 / 3)
        self.assertEqual(divide(7, 1), 7)
        self.assertRaises(ValueError, divide, 10, 0)

if __name__ == '__main__':
    unittest.main()
