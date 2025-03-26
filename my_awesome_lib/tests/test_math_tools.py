import unittest
from my_awesome_lib.math_tools import factorial, is_prime

class TestMathTools(unittest.TestCase):
    def test_factorial(self):
        self.assertEqual(factorial(5), 120)
        with self.assertRaises(ValueError):
            factorial(-1)

    def test_is_prime(self):
        self.assertTrue(is_prime(7))
        self.assertFalse(is_prime(10))

if __name__ == "__main__":
    unittest.main()
