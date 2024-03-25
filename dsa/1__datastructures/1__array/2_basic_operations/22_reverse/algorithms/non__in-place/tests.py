import unittest
from using_extra_array import reverse__extra_array
from using_builtin_methods import reverse__builtin
from using_recursion import reverse__recursion
from using_stack import reverse__stack


class TestReverseInplace(unittest.TestCase):
    def test_reverse_using_an_extra_array(self):
        arr = [5, 6, 7, 8, 9, 10, 11]
        expected = [11, 10, 9, 8, 7, 6, 5]
        reversed_arr = reverse__extra_array(arr)
        self.assertEqual(expected, reversed_arr)

    def test_reverse_using_builtin_method(self):
        arr = [5, 6, 7, 8, 9, 10, 11]
        expected = [11, 10, 9, 8, 7, 6, 5]
        reversed_arr = reverse__builtin(arr)
        self.assertEqual(expected, reversed_arr)

    def test_reverse_using_recursion(self):
        arr = [5, 6, 7, 8, 9, 10, 11]
        expected = [11, 10, 9, 8, 7, 6, 5]
        reversed_arr = reverse__recursion(arr)
        self.assertEqual(expected, reversed_arr)

    def test_reverse_using_stack(self):
        arr = [5, 6, 7, 8, 9, 10, 11]
        expected = [11, 10, 9, 8, 7, 6, 5]
        reversed_arr = reverse__stack(arr)
        self.assertEqual(expected, reversed_arr)


if __name__ == '__main__':
    unittest.main()
