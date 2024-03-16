import unittest
from main import find_pair_with_difference_1st, find_pair_with_difference_2nd

class TestFindPairWithDifference(unittest.TestCase):
    # ! Approach 1
    def test_empty_input_1st(self):
        self.assertIsNone(find_pair_with_difference_1st([], 5))

    def test_array_less_than_two_elements_1st(self):
        self.assertIsNone(find_pair_with_difference_1st([1], 5))

    def test_array_with_two_elements_difference_equal_to_n_1st(self):
        self.assertEqual(find_pair_with_difference_1st([1, 6], 5), [(1, 6)])

    def test_array_with_two_elements_difference_not_equal_to_n_1st(self):
        self.assertEqual(find_pair_with_difference_1st([1, 4], 5), None)

    def test_array_with_multiple_elements_pair_exists_1st(self):
        self.assertEqual(find_pair_with_difference_1st([4, 2, 6, 8, 1], 2), [(4, 2), (4, 6), (6, 8)])

    def test_array_with_multiple_elements_pair_does_not_exist_1st(self):
        self.assertIsNone(find_pair_with_difference_1st([4, 2, 6, 8, 10], 5), None)

    def test_array_with_negative_numbers_pair_exists_1st(self):
        self.assertEqual(find_pair_with_difference_1st([4, -2, 6, 8, -1], 5), [(4, -1)])

    def test_array_with_negative_numbers_pair_does_not_exist_1st(self):
        self.assertIsNone(find_pair_with_difference_1st([4, -2, 6, 8, -1], 3))

    # ! Approach 2
    def test_empty_input_2nd(self):
        self.assertIsNone(find_pair_with_difference_2nd([], 5))

    def test_array_less_than_two_elements_2nd(self):
        self.assertIsNone(find_pair_with_difference_2nd([1], 5))

    def test_array_with_two_elements_difference_equal_to_n_2nd(self):
        self.assertEqual(find_pair_with_difference_2nd([1, 6], 5), [(1, 6)])

    def test_array_with_two_elements_difference_not_equal_to_n_2nd(self):
        self.assertEqual(find_pair_with_difference_2nd([1, 4], 5), [])

    def test_array_with_multiple_elements_pair_exists_2nd(self):
        self.assertEqual(find_pair_with_difference_2nd([4, 2, 6, 8, 1], 2), [(2, 4), (4, 6), (6, 8)])

    def test_array_with_multiple_elements_pair_does_not_exist_2nd(self):
        self.assertEqual(find_pair_with_difference_2nd([4, 2, 6, 8, 10], 5), [])

    def test_array_with_negative_numbers_pair_exists_2nd(self):
        self.assertEqual(find_pair_with_difference_2nd([4, -2, 6, 8, -1], 5), [(-1, 4)])

    def test_array_with_negative_numbers_pair_does_not_exist_2nd(self):
        self.assertEqual(find_pair_with_difference_2nd([4, -2, 6, 8, -1], 3), [])

if __name__ == "__main__":
    unittest.main()
