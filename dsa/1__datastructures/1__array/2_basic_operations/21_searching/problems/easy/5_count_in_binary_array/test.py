import unittest
from main import count_1s_2nd

class TestCountOnes(unittest.TestCase):
    def test_empty_array_2nd(self):
        self.assertEqual(count_1s_2nd([]), 0)

    def test_no_ones_2nd(self):
        self.assertEqual(count_1s_2nd([0, 0, 0, 0]), 0)

    def test_all_ones_2nd(self):
        self.assertEqual(count_1s_2nd([1, 1, 1, 1]), 4)

    def test_mixed_array_2nd(self):
        self.assertEqual(count_1s_2nd([1, 1, 0, 0, 0]), 2)

    def test_single_element_2nd(self):
        self.assertEqual(count_1s_2nd([1]), 1)
        self.assertEqual(count_1s_2nd([0]), 0)

    def test_large_array_2nd(self):
        self.assertEqual(count_1s_2nd([1] * 1000), 1000)
        self.assertEqual(count_1s_2nd([0] * 1000), 0)

if __name__ == '__main__':
    unittest.main()
