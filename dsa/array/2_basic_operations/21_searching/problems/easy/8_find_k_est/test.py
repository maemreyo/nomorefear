import unittest
from main import find_k_est_1st, find_k_est_2nd


class TestFindKest_1st(unittest.TestCase):
    def test_k_equals_the_length_of_the_array_1st(self):
        arr = [3, 10, 4, 7, 8, 15]
        k = len(arr)
        self.assertCountEqual(find_k_est_1st(arr, k), [3, 10, 4, 7, 8, 15])

    def test_k_equals_0_1st(self):
        arr = [3, 10, 4, 7, 8, 15]
        k = 0
        self.assertEqual(find_k_est_1st(arr, k), [])

    def test_k_equals_1_1st(self):
        arr = [3, 10, 4, 7, 8, 15]
        k = 1
        self.assertEqual(find_k_est_1st(arr, k), [15])

    def test_array_with_negative_numbers_1st(self):
        arr = [3, -10, 4, -7, 8, 15]
        k = 2
        self.assertCountEqual(find_k_est_1st(arr, k), [8, 15])


class TestFindKest_2nd(unittest.TestCase):
    def test_find_k_est_2nd_basic(self):
        arr = [1, 2, 3, 4, 5]
        k = 3
        expected_result = 3
        result = find_k_est_2nd(arr, k)
        self.assertEqual(expected_result, result)

    def test_find_k_est_2nd_with_duplicates(self):
        arr = [1, 2, 2, 3, 4, 5]
        k = 3
        expected_result = 3
        result = find_k_est_2nd(arr, k)
        self.assertEqual(expected_result, result)

    def test_find_k_est_2nd_edge_case(self):
        arr = [1]
        k = 1
        expected_result = 1
        result = find_k_est_2nd(arr, k)
        self.assertEqual(expected_result, result)


if __name__ == "__main__":
    unittest.main()
