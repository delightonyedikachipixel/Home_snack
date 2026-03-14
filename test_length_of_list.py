from unittest import TestCase
from length_of_list import *

class TestClass(TestCase):

    def test_length_of_list(self):
        self.assertEqual(length_of_list([1,2,3,4]), 4)

    def test_even_sum(self):
        self.assertEqual(even_sum([1,2,3,4,5,6]), 12)

    def test_odd_sum(self):
        self.assertEqual(odd_sum([1,2,3,4,5,6]), 9)

    def test_multiply_elements_at_third_position(self):
        self.assertEqual(multiply_elements_at_third_position([1,2,3,4,5,6]), 18)

    def test_average_of_numbers(self):
        self.assertEqual(average_of_numbers([2,4,6,8]), 5)

    def test_get_largest_number(self):
        self.assertEqual(get_largest_number([4,8,2,9,1]), 9)

    def test_get_smallest_number(self):
        self.assertEqual(get_smallest_number([4,8,2,9,1]), 1)

    def test_get_length_of_word(self):
        words = ["level","python","radar","madam","no"]
        count, matched = get_length_of_word(words)

        self.assertEqual(count, 5)
        self.assertEqual(matched, ["level","radar","madam"])

    def test_get_sum_of_third_place_numbers(self):
        self.assertEqual(get_sum_of_third_place_numbers(), 18)

    def test_get_sum_of_first_middle_last_place_numbers(self):
        self.assertEqual(get_sum_of_first_middle_last_place_numbers(), 16.5)

