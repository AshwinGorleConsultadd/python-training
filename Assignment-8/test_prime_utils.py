import unittest
from prime_utils import is_prime

class TestPrimeChecker(unittest.TestCase):
    def test_prime_numbers(self):
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(5))
        self.assertTrue(is_prime(13))

    def test_non_prime_numbers(self):
        self.assertFalse(is_prime(1))
        self.assertFalse(is_prime(4))
        self.assertFalse(is_prime(-3))

if __name__ == "__main__":
    unittest.main()
