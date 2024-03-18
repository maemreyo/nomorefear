import unittest
from main import find_k_th_smallest


class TestFindKthSmallest_BruteForce(unittest.TestCase):
    def test_find_k_th_smallest_basic(self):
        arr = [[10, 20, 30, 40],
               [15, 25, 35, 45],
               [24, 29, 37, 48],
               [32, 33, 39, 50]]

        n = 4
        k = 3
        expected_result = 20
        result = find_k_th_smallest(arr, n, k)
        self.assertEqual(expected_result, result)

    def test_find_k_th_smallest_k_greater_than_n(self):
        arr = [[10, 20, 30, 40],
               [15, 25, 35, 45],
               [24, 29, 37, 48],
               [32, 33, 39, 50]]

        n = 4
        k = 7
        expected_result = 30
        result = find_k_th_smallest(arr, n, k)
        self.assertEqual(expected_result, result)

    def test_find_kth_smallest_basic(self):
        arr = [[1, 2], [3, 4]]
        k = 3
        expected_result = 3
        result = find_k_th_smallest(arr, 2, k)
        self.assertEqual(result, expected_result)

    def test_find_kth_smallest_with_duplicates(self):
        arr = [[1, 2], [2, 3]]
        k = 2
        expected_result = 2
        result = find_k_th_smallest(arr, 2, k)
        self.assertEqual(result, expected_result)

    def test_find_kth_smallest_edge_case_single_element(self):
        arr = [[1]]
        k = 1
        expected_result = 1
        result = find_k_th_smallest(arr, 1, k)
        self.assertEqual(result, expected_result)

    def test_find_kth_smallest_edge_case_empty_array(self):
        arr = []
        k = 1
        expected_result = -1
        result = find_k_th_smallest(arr, 0, k)
        self.assertEqual(result, expected_result)

    def test_find_kth_smallest_edge_case_k_greater_than_length(self):
        arr = [[1, 2], [3, 4]]
        k = 5
        expected_result = -1
        result = find_k_th_smallest(arr, 2, k)
        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
