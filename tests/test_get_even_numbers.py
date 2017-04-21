from unittest import TestCase
from errors import incorrect_output, no_function_found, succeed


class TestGet_even_numbers(TestCase):
    def test_even_numbers(self):
        try:
            from even_numbers import get_even_numbers
        except ImportError:
            self.assertFalse(no_function_found("get_even_numbers"))

        try:
            result = get_even_numbers(0)
        except ValueError:
            self.assertTrue("number should be less than 0 passed")

        result = get_even_numbers(10)
        self.assertEqual(2, result[0])
        self.assertEqual(4, result[1])
        self.assertEqual(6, result[2])
        self.assertEqual(8, result[3])
        self.assertTrue(succeed("all test cases passed for even numbers"))