import unittest
from using_extra_array import reverse__extra_array


class TestReverseInplace(unittest.TestCase):
    def test_reverse_using_an_extra_array(self):
        arr = [5, 6, 7, 8, 9, 10, 11]
        expected = [11, 10, 9, 8, 7, 6, 5]
        reversed_arr = reverse__extra_array(arr)
        self.assertEqual(expected, reversed_arr)


if __name__ == '__main__':
    unittest.main()
