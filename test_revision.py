import unittest
from revision import *


class TestRevision(unittest.TestCase):


    # --------------------------
    # BASIC LOOPS
    # --------------------------

    def test_sum_to_n(self):
        self.assertEqual(sum_to_n(5), 15)

    def test_count_even(self):
        self.assertEqual(count_even([1,2,3,4,6]), 3)

    def test_print_numbers(self):
        self.assertEqual(print_numbers(4), [1,2,3,4])


    # --------------------------
    # ADVANCED LOOPS
    # --------------------------

    def test_multiplication_table(self):
        self.assertEqual(multiplication_table(3), [3,6,9])

    def test_nested_count(self):
        self.assertEqual(nested_count(3), 9)

    def test_pyramid_levels(self):
        self.assertEqual(pyramid_levels(3), ["*", "**", "***"])


    # --------------------------
    # ALGORITHMS
    # --------------------------

    def test_find_max(self):
        self.assertEqual(find_max([1,5,3]), 5)

    def test_find_min(self):
        self.assertEqual(find_min([1,5,3]), 1)

    def test_average(self):
        self.assertEqual(average([2,4,6]), 4)


if __name__ == "__main__":
    unittest.main()