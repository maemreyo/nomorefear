import unittest
from main import find_first_repeating_1


class TestFindFirstRepeating(unittest.TestCase):
    def test_empty_list(self):
        self.assertIsNone(find_first_repeating_1([]))

    def test_no_repeating_elements(self):
        self.assertIsNone(find_first_repeating_1([1, 2, 3, 4]))

    def test_single_repeating_element(self):
        self.assertEqual(find_first_repeating_1([1, 2, 3, 2, 4]), 2)

    def test_multiple_repeating_elements(self):
        self.assertEqual(find_first_repeating_1([1, 2, 3, 2, 3, 4]), 2)

    def test_repeating_element_at_beginning(self):
        self.assertEqual(find_first_repeating_1([2, 1, 3, 4, 2]), 2)

    def test_repeating_element_at_middle(self):
        self.assertEqual(find_first_repeating_1([1, 2, 3, 2, 4]), 2)

    def test_repeating_element_at_end(self):
        self.assertEqual(find_first_repeating_1([1, 2, 3, 4, 2]), 2)


if __name__ == "__main__":
    unittest.main()
