"""
    |❓ PROBLEM
        =>> Print the elements of an array in the decreasing frequency if 2 numbers have the same frequency then print
        the one which came first

    ! =================================================================================================================
    |🗳️ EXAMPLE
        Input:  arr[] = [2, 5, 2, 8, 5, 6, 8, 8]
        Output: arr[] = [8, 8, 8, 2, 2, 5, 5, 6]

        Input: arr[] = [2, 5, 2, 6, -1, 9999999, 5, 8, 8, 8]
        Output: arr[] = [8, 8, 8, 2, 2, 5, 5, 6, -1, 9999999]

    ! =================================================================================================================
    |🙌🏻 APPROACHES
        @Approach 1:
            ! Using Hashing and sort method in Python
            -> Initialize a frequency map (element: frequency)
            -> Use arr.sort() with key = (-frequency[x], x)
                -> the first criterion will sort the arr as descending order
                -> the second criterion will sort the arr as the original order of arr if the first criterion is equal

        |🚀 COMPLEXITIES:
            ⌛ Time complexity: O(n*log(n))
            🌌 Space complexity: O(n)

        ! =============================================================================================================
        @Approach 2:
            ! Using


        |🚀 COMPLEXITIES:
            ⌛ Time complexity: O()
            🌌 Space complexity: O()

"""
# ! ===================================================================================================================
import unittest


# ! Approach 1
def sort_by_frequency__2d_array(arr: list):
    # Count the frequency of each element using a dictionary
    frequency = {}
    for element in arr:
        frequency[element] = frequency.get(element, 0) + 1

    # Sort the array based on frequency, value, and sign
    arr.sort(key=lambda x: (-frequency[x], x), reverse=False)


class TestSuite(unittest.TestCase):
    def test_sorting_an_array__basic_case(self):
        arr = [2, 5, 2, 8, 5, 6, 8, 8]
        expected = [8, 8, 8, 2, 2, 5, 5, 6]

        sort_by_frequency__2d_array(arr)

        self.assertEqual(expected, arr)

    def test_sorting_an_array__negative_number(self):
        arr = [2, 5, 2, 6, -1, 9999999, 5, 8, 8, 8]
        expected = [8, 8, 8, 2, 2, 5, 5, -1, 6, 9999999]

        sort_by_frequency__2d_array(arr)

        self.assertEqual(expected, arr)


if __name__ == '__main__':
    unittest.main()
