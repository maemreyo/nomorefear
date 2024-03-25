"""
    |❓ PROBLEM
        =>> Print the elements of an 1__array in the decreasing frequency if 2 numbers have the same frequency then print
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
            ! Using Quick Sort
            -> Make a structure called “ele” with two fields called “val” and “count” to hold the value and count of
            each element in the input 1__array.
            -> Make an 1__array of “ele” structures of size n, where n is the size of the input 1__array, and set the “val”
            field of each element to the value from the input 1__array and the “count” field to 0.
            -> Traverse through the input 1__array and for each element,  increase the count field of the corresponding
            “ele” structure by 1.
            -> Using the quicksort method and a custom comparison function for elements, sort the “ele” 1__array in
            decreasing order of count and rising order of value.
            -> Finally, recreate the input 1__array by iterating over the sorted “ele” 1__array in descending order of count
            and adding the value of each element to the input 1__array count number of times equal to its count field.

        |🚀 COMPLEXITIES:
            ⌛ Time complexity: O()
            🌌 Space complexity: O()

    ! =================================================================================================================
    |🖇️ REFERENCES
    + Problem: https://www.geeksforgeeks.org/sort-elements-by-frequency/
"""
# ! ===================================================================================================================
import unittest


# ! Approach 1
def sort_by_frequency__2d_array(arr: list):
    # Count the frequency of each element using a dictionary
    frequency = {}
    for element in arr:
        frequency[element] = frequency.get(element, 0) + 1

    # Sort the 1__array based on frequency, value, and sign
    arr.sort(key=lambda x: (-frequency[x], x), reverse=False)


# ! ===================================================================================================================
# ! Approach 2
def sort_by_frequency__quick_sort(arr: list):
    element = []
    for i in range(len(arr)):
        element.append({'val': arr[i], 'count': 0})

    for i in range(len(arr)):
        j = 0
        while j < i:
            if arr[i] == arr[j]:
                break
            j += 1

        if i == j:
            element[i]['count'] += 1
        else:
            element[j]['count'] += 1

    def partition(arr, low, high):
        pivot = arr[high]
        i = low - 1

        for j in range(low, high):
            if arr[j]['count'] < pivot['count'] or (arr[j]['count'] == pivot['count'] and arr[j]['val'] > pivot['val']):
                i += 1
                arr[i], arr[j] = arr[j], arr[i]

        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    def quicksort(arr, low, high):
        if low < high:
            pi = partition(arr, low, high)
            quicksort(arr, low, pi - 1)
            quicksort(arr, pi + 1, high)

    quicksort(element, 0, len(arr) - 1)

    index = 0
    for i in range(len(arr) - 1, -1, -1):
        for j in range(element[i]['count']):
            arr[index] = element[i]['val']
            index += 1

    return arr


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

    def test_sorting_an_array__basic_case__quick_sort(self):
        arr = [2, 5, 2, 8, 5, 6, 8, 8]
        expected = [8, 8, 8, 2, 2, 5, 5, 6]

        sort_by_frequency__quick_sort(arr)

        self.assertEqual(expected, arr)


if __name__ == '__main__':
    unittest.main()


# TODO: Check the logic to partition
# def sort_by_frequency__quick_sort(arr: list):
#     element = []
#     for i in range(len(arr)):
#         element.append({'val': arr[i], 'count': 0})
#
#     for i in range(len(arr)):
#         j = 0
#         while j < i:
#             if arr[i] == arr[j]:
#                 break
#             j += 1
#
#         if i == j:
#             element[i]['count'] += 1
#         else:
#             element[j]['count'] += 1
#
#     def partition(arr, low, high):
#         pivot = arr[low]
#         i = low + 1
#         j = high
#
#         while True:
#             while i <= j and (
#                 arr[i]['count'] >= pivot['count'] or (
#                     arr[i]['count'] == pivot['count'] and arr[i]['val'] < pivot['val']
#                 )
#             ):
#                 i += 1
#
#             while j >= i and arr[j]['count'] <= pivot['count']:
#                 j -= 1
#
#             if i > j:
#                 break
#
#             arr[i], arr[j] = arr[j], arr[i]
#             i += 1
#             j -= 1
#
#         arr[low], arr[j] = arr[j], arr[low]
#
#         return j
#
#     def quick_sort(arr, low, high):
#         if low < high:
#             pivot_idx = partition(arr, low, high)
#
#             quick_sort(arr, low, pivot_idx - 1)
#             quick_sort(arr, pivot_idx + 1, high)
#
#     quick_sort(element, 0, len(arr) - 1)
#
#     print(f"Elements: {element}")
#
#     # index = 0
#     # for i in range(len(arr) - 1, -1, -1):
#     #     for j in range(element[i]['count']):
#     #         arr[index] = element[i]['val']
#     #         index += 1
#
#     return arr
