import unittest
from using_loop import reverse__loop
from using_recursion import reverse__recursion


class TestReverseInplace(unittest.TestCase):
    def test_reverse_using_loop(self):
        arr = [1, 2, 3, 4]
        expected = [4, 3, 2, 1]
        reverse__loop(arr)
        self.assertEqual(expected, arr)

    def test_reverse_using_recursion(self):
        arr = [1, 2, 3, 4]
        expected = [4, 3, 2, 1]
        reverse__recursion(arr, 0, len(arr) - 1)
        self.assertEqual(expected, arr)


if __name__ == '__main__':
    unittest.main()
