import unittest
from main import find_missing_repeating_1, find_missing_repeating_2


class TestFindMissingRepeating(unittest.TestCase):
    # ! Approach 1
    def test_empty_input_1(self):
        self.assertIsNone(find_missing_repeating_1([]))

    def test_single_repeating_element_1(self):
        self.assertEqual(find_missing_repeating_1([1, 2, 3, 2, 4]), (5, 2))

    def test_single_missing_element_1(self):
        self.assertEqual(find_missing_repeating_1([1, 2, 3, 5]), (4, None))

    def test_missing_and_repeating_elements_1(self):
        self.assertEqual(find_missing_repeating_1([1, 2, 2, 4, 5, 6]), (3, 2))

    def test_repeating_element_at_beginning_1(self):
        self.assertEqual(find_missing_repeating_1([2, 2, 3, 4, 5]), (1, 2))

    def test_repeating_element_at_end_1(self):
        self.assertEqual(find_missing_repeating_1([1, 2, 3, 5, 5]), (4, 5))

    def test_missing_element_at_beginning_1(self):
        self.assertEqual(find_missing_repeating_1([2, 3, 4, 5]), (1, None))

    def test_missing_element_at_end_1(self):
        self.assertEqual(find_missing_repeating_1([1, 2, 3, 4]), (5, None))

    # # ! Approach 2
    def test_empty_input_2(self):
        self.assertIsNone(find_missing_repeating_2([]))

    def test_single_repeating_element_2(self):
        self.assertEqual(find_missing_repeating_2([1, 2, 3, 2, 4]), (5, 2))

    def test_single_missing_element_2(self):
        self.assertEqual(find_missing_repeating_2([1, 2, 3, 5]), (4, None))

    def test_missing_and_repeating_elements_2(self):
        self.assertEqual(find_missing_repeating_2([1, 2, 2, 4, 5, 6]), (3, 2))

    def test_repeating_element_at_beginning_2(self):
        self.assertEqual(find_missing_repeating_2([2, 2, 3, 4, 5]), (1, 2))

    def test_repeating_element_at_end_2(self):
        self.assertEqual(find_missing_repeating_2([1, 2, 3, 5, 5]), (4, 5))

    def test_missing_element_at_beginning_2(self):
        self.assertEqual(find_missing_repeating_2([2, 3, 4, 5]), (1, None))

    def test_missing_element_at_end_2(self):
        self.assertEqual(find_missing_repeating_2([1, 2, 3, 4]), (None, None))

if __name__ == "__main__":
    unittest.main()
