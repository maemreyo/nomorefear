import unittest
from using_loop import reverse_array__loop


class TestReverseInplace(unittest.TestCase):
    def test_reverse_using_loop(self):
        arr = [1, 2, 3, 4]
        expected = [4, 3, 2, 1]
        self.assertEqual(reverse_array__loop(arr), expected)


if __name__ == '__main__':
    unittest.main()
