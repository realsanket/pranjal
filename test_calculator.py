import unittest
from calculator import add, subtract, multiply, divide, find_even, find_odd

class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(-1, -1), -2)

    def test_subtract(self):
        self.assertEqual(subtract(10, 5), 5)
        self.assertEqual(subtract(-1, 1), -2)
        self.assertEqual(subtract(-1, -1), 0)

    def test_multiply(self):
        self.assertEqual(multiply(3, 7), 21)
        self.assertEqual(multiply(-1, 1), -1)
        self.assertEqual(multiply(-1, -1), 1)

    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)
        self.assertEqual(divide(-1, 1), -1)
        self.assertEqual(divide(-1, -1), 1)
        with self.assertRaises(ValueError):
            divide(10, 0)

    def test_find_even(self):
        self.assertEqual(find_even([1, 2, 3, 4, 5]), [2, 4])
        self.assertEqual(find_even([10, 15, 20, 25]), [10, 20])

    def test_find_odd(self):
        self.assertEqual(find_odd([1, 2, 3, 4, 5]), [1, 3, 5])
        self.assertEqual(find_odd([10, 15, 20, 25]), [15, 25])

if __name__ == '__main__':
    unittest.main()
