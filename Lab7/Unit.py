import unittest
from main import is_prime, prime_factors


class TestIsPrime(unittest.TestCase):
    def test_is_prime(self):
        self.assertFalse(is_prime(1))
        self.assertFalse(is_prime(4))
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(3))


class TestPrimeFactors(unittest.TestCase):
    def test_prime_factors(self):
        self.assertEqual(prime_factors(2), [2])
        self.assertEqual(prime_factors(4), [2, 2])
        self.assertEqual(prime_factors(6), [2, 3])
        self.assertEqual(prime_factors(9), [3, 3])
        self.assertEqual(prime_factors(10), [2, 5])
        self.assertEqual(prime_factors(12), [2, 2, 3])
        self.assertEqual(prime_factors(14), [2, 7])
        self.assertEqual(prime_factors(18), [2, 3, 3])
        self.assertEqual(prime_factors(20), [2, 2, 5])