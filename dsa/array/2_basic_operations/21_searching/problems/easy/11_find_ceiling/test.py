import unittest
from main import find_ceiling__linear_search
class Test_FindCeiling__LinearSearch(unittest.TestCase):
    def test_regular_case(self):
        arr = [1, 3, 5, 7, 9]
        x = 6
        low, high = 0, len(arr) - 1
        self.assertEqual(find_ceiling__linear_search(arr, x, low, high), 3)

    def test_x_less_than_first_element(self):
        arr = [5, 10, 15, 20, 25]
        x = 2
        low, high = 0, len(arr) - 1
        self.assertEqual(find_ceiling__linear_search(arr, x, low, high), 0)

    def test_x_greater_than_last_element(self):
        arr = [5, 10, 15, 20, 25]
        x = 30
        low, high = 0, len(arr) - 1
        self.assertEqual(find_ceiling__linear_search(arr, x, low, high), -1)

    def test_x_equal_to_an_element(self):
        arr = [5, 10, 15, 20, 25]
        x = 20
        low, high = 0, len(arr) - 1
        self.assertEqual(find_ceiling__linear_search(arr, x, low, high), 3)

    def test_x_between_two_elements(self):
        arr = [5, 10, 15, 20, 25]
        x = 17
        low, high = 0, len(arr) - 1
        self.assertEqual(find_ceiling__linear_search(arr, x, low, high), 3)


if __name__ == '__main__':
    unittest.main()
