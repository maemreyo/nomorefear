import unittest
from main import find_sum_closest_zero_1st, find_sum_closest_zero_2nd


class TestSumClosestZero(unittest.TestCase):
    # ! Approach 1
    def test_empty_array_1st(self):
        self.assertIsNone(find_sum_closest_zero_1st([]))

    def test_array_with_less_than_two_elements_1st(self):
        self.assertIsNone(find_sum_closest_zero_1st([1]))

    def test_array_with_two_elements_1st(self):
        self.assertIsNone(find_sum_closest_zero_1st([1, 2]))

    def test_array_with_more_than_two_elements_1st(self):
        self.assertEqual(find_sum_closest_zero_1st([1, -1, 5]), (1, -1))

    def test_array_with_positive_elements_1st(self):
        self.assertEqual(find_sum_closest_zero_1st([1, 1, 5]), (1, 1))

    def test_array_with_negative_elements_1st(self):
        self.assertEqual(find_sum_closest_zero_1st([-1, -1, -5]), (-1, -1))

    def test_array_with_mixed_elements_1st(self):
        self.assertEqual(find_sum_closest_zero_1st([-1, 1, -5]), (-1, 1))

    def test_array_with_zeros_1st(self):
        self.assertEqual(find_sum_closest_zero_1st([-1, 2, -5, 0, 0]), (0, 0))

    # ! Approach 2
    def test_empty_array_2nd(self):
        self.assertIsNone(find_sum_closest_zero_2nd([]))

    def test_array_with_less_than_two_elements_2nd(self):
        self.assertIsNone(find_sum_closest_zero_2nd([1]))

    def test_array_with_two_elements_2nd(self):
        self.assertIsNone(find_sum_closest_zero_2nd([1, 2]))

    # ! Because the second approach is using Sort in-place, then the order of the elements in the result can be changed
    def test_array_with_more_than_two_elements_2nd(self):
        self.assertEqual(find_sum_closest_zero_2nd([1, -1, 5]), (-1, 1))

    def test_array_with_positive_elements_2nd(self):
        self.assertEqual(find_sum_closest_zero_2nd([1, 1, 5]), (1, 1))

    def test_array_with_negative_elements_2nd(self):
        self.assertEqual(find_sum_closest_zero_2nd([-1, -1, -5]), (-1, -1))

    def test_array_with_mixed_elements_2nd(self):
        self.assertEqual(find_sum_closest_zero_2nd([-1, 1, -5]), (-1, 1))

    def test_array_with_zeros_2nd(self):
        self.assertEqual(find_sum_closest_zero_2nd([-1, 2, -5, 0, 0]), (0, 0))
if __name__ == "__main__":
    unittest.main()
