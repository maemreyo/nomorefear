import unittest
from using_loop import find_sub_arrays__loop


class TestFindSubArrays(unittest.TestCase):
    def test_finding_sub_arrays__loop_(self):
        arr = [1, 2, 3]
        sub_arrays = [[1], [1, 2], [2], [1, 2, 3], [2, 3], [3]]
        self.assertCountEqual(sub_arrays, find_sub_arrays__loop(arr))

    def test_finding_sub_arrays__loop_2(self):
        arr = [1, 2]
        sub_arrays = [[1], [1, 2], [2]]
        self.assertCountEqual(sub_arrays, find_sub_arrays__loop(arr))


if __name__ == '__main__':
    unittest.main()
