import unittest
from main import find_floor__linear_search, find_floor__binary_search


class TestFindingFloor_LinearSearch(unittest.TestCase):
    def test_basic_case(self):
        arr = [1, 2, 8, 10, 10, 12, 19]
        x = 5
        self.assertEqual(find_floor__linear_search(arr, x), 2)

    def test_x_above_the_greatest_element_in_input_array(self):
        arr = [1, 2, 8, 10, 10, 12, 19]
        x = 20
        self.assertEqual(find_floor__linear_search(arr, x), 19)

    def test_x_below_the_smallest_element_in_input_array(self):
        arr = [1, 2, 8, 10, 10, 12, 19]
        x = 0
        self.assertEqual(find_floor__linear_search(arr, x), -1)

class TestFindingFloor_BinarySearch(unittest.TestCase):
    def test_basic_case(self):
        arr = [1, 2, 8, 10, 10, 12, 19]
        x = 5
        self.assertEqual(find_floor__binary_search(arr, x), 2)

    def test_x_above_the_greatest_element_in_input_array(self):
        arr = [1, 2, 8, 10, 10, 12, 19]
        x = 20
        self.assertEqual(find_floor__binary_search(arr, x), 19)

    def test_x_below_the_smallest_element_in_input_array(self):
        arr = [1, 2, 8, 10, 10, 12, 19]
        x = 0
        self.assertEqual(find_floor__binary_search(arr, x), -1)


if __name__ == '__main__':
    unittest.main()
