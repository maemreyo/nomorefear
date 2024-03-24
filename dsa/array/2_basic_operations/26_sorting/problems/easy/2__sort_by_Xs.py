"""
    |❓ PROBLEM
        =>> Given an array A[] consisting of only 0s, 1s, and 2s. The task is to write a function that sorts the given
        array. The functions should put all 0s first, then all 1s and all 2s in last.

    ! =================================================================================================================
    |🗳️ EXAMPLE
        Input: [0, 1, 2, 0, 1, 2]
        Output: [0, 0, 1, 1, 2, 2]

        Input: [0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]
        Output: [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 2]

    ! =================================================================================================================
    |🙌🏻 APPROACHES
        @Approach 1:
            ! Using


        |🚀 COMPLEXITIES:
            ⌛ Time complexity: O()
            🌌 Space complexity: O()

        ! =============================================================================================================
        @Approach 2:
            ! Using


        |🚀 COMPLEXITIES:
            ⌛ Time complexity: O()
            🌌 Space complexity: O()

    ! =================================================================================================================
    |🖇️ REFERENCES
    + Problem: https://www.geeksforgeeks.org/sort-an-array-of-0s-1s-and-2s/?ref=lbp
    + Dutch National Flag problem: https://en.wikipedia.org/wiki/Dutch_national_flag_problem

"""
# ! ===================================================================================================================
import unittest


# ! Approach 1
def do_something(arr: list):
    pass


class TestSuite(unittest.TestCase):
    def test_sorting_an_array(self):
        arr = [1, 4, 3, 2, 0]
        expected = [0, 1, 2, 3, 4]

        do_something(arr)

        self.assertEqual(expected, arr)


if __name__ == '__main__':
    unittest.main()
