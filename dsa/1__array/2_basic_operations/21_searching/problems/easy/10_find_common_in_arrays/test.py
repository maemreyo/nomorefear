import unittest
from main import find_common_in_sorted_arrays__naive, find_common_in_sorted_arrays__intersection_pair, find_common_in_sorted_arrays__intersection_full


class Test_FindingCommonInSortedArrays_NaiveApproach(unittest.TestCase):
    def test_an_array_has_no_element(self):
        arr1 = []
        arr2 = [1]
        arr3 = [1, 2, 3, 4, 5]

        expected = []
        self.assertEqual(find_common_in_sorted_arrays__naive(arr1, arr2, arr3), expected)

    def test_basic_flow(self):
        arr1 = [1, 5, 10, 20, 40, 80]
        arr2 = [6, 7, 20, 80, 100]
        arr3 = [3, 4, 15, 20, 30, 70, 80, 120]

        expected = [20, 80]
        self.assertEqual(find_common_in_sorted_arrays__naive(arr1, arr2, arr3), expected)

    def test_arrays_contain_duplicated_elements(self):
        arr1 = [1, 5, 5]
        arr2 = [3, 4, 5, 5, 10]
        arr3 = [5, 5, 10, 20]

        expected = [5, 5]
        self.assertEqual(find_common_in_sorted_arrays__naive(arr1, arr2, arr3), expected)


class Test_FindingCommonInSortedArrays_IntersectionPair(unittest.TestCase):
    def test_an_array_has_no_element(self):
        arr1 = []
        arr2 = [1]
        arr3 = [1, 2, 3, 4, 5]

        expected = []
        self.assertEqual(find_common_in_sorted_arrays__intersection_pair(arr1, arr2, arr3), expected)

    def test_basic_flow(self):
        arr1 = [1, 5, 10, 20, 40, 80]
        arr2 = [6, 7, 20, 80, 100]
        arr3 = [3, 4, 15, 20, 30, 70, 80, 120]

        expected = [20, 80]
        self.assertEqual(find_common_in_sorted_arrays__intersection_pair(arr1, arr2, arr3), expected)

    def test_arrays_contain_duplicated_elements(self):
        arr1 = [1, 5, 5]
        arr2 = [3, 4, 5, 5, 10]
        arr3 = [5, 5, 10, 20]

        expected = [5, 5]
        self.assertEqual(find_common_in_sorted_arrays__intersection_pair(arr1, arr2, arr3), expected)

class Test_FindingCommonInSortedArrays_IntersectionFull(unittest.TestCase):
    def test_an_array_has_no_element(self):
        arr1 = []
        arr2 = [1]
        arr3 = [1, 2, 3, 4, 5]

        expected = []
        self.assertEqual(find_common_in_sorted_arrays__intersection_full(arr1, arr2, arr3), expected)

    def test_basic_flow(self):
        arr1 = [1, 5, 10, 20, 40, 80]
        arr2 = [6, 7, 20, 80, 100]
        arr3 = [3, 4, 15, 20, 30, 70, 80, 120]

        expected = [20, 80]
        self.assertEqual(find_common_in_sorted_arrays__intersection_full(arr1, arr2, arr3), expected)

    def test_arrays_contain_duplicated_elements(self):
        arr1 = [1, 5, 5]
        arr2 = [3, 4, 5, 5, 10]
        arr3 = [5, 5, 10, 20]

        expected = [5, 5]
        self.assertEqual(find_common_in_sorted_arrays__intersection_full(arr1, arr2, arr3), expected)


if __name__ == '__main__':
    unittest.main()
