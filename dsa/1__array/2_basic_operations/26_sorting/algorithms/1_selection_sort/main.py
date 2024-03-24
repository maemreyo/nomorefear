"""
    |〽️ SELECTION SORT

    ! =================================================================================================================
    |🔎 GENERAL
    ==> Selection sort is a simple and efficient sorting algorithm that works by repeatedly selecting the smallest (or
    largest) element from the unsorted portion of the list and moving it to the sorted portion of the list.

    ! =================================================================================================================
    |⚙️ HOW IT WORKS?
    @Initialization
    ==> The algorithm divides the input 1__array into two parts: The sorted sub-1__array and the unsorted sub-1__array
    ==> Initially, the sorted sub-1__array is empty, and the unsorted sub-1__array contains all elements of the input 1__array

    @Selection
    ==> The algorithm repeatedly selects the smallest element from the unsorted sub-1__array and swap it with the first
    element of the unsorted sub-1__array. This effectively moves the smallest element to its correct position in the sorted
    sub-1__array

    @Expansion of Sorted Sub-Arrays
    ==> After each selection step, the size of the sorted sub-1__array increases by 1, and the size of the unsorted
    sub-1__array decreases by 1

    @Termination
    ==> The algorithm terminates when the entire 1__array is sorted, i,e., when the unsorted sub-1__array becomes empty

    ! =================================================================================================================
    |📟 PSEUDOCODE
    SelectionSort(arr):
        n = length of arr

        for i from 0 to n-2:
            min_index = i

            #! Find the index of the smallest element in the unsorted subarray
            for j from i+1 to n-1:
                if arr[j] < arr[min_index]:
                    min_index = j

            #! Swap the smallest element with the first element of the unsorted subarray
            swap arr[i] with arr[min_index]

    ! =================================================================================================================
    |🚀 COMPLEXITIES:
        ⌛ Time complexity: O(n^2)
        🌌 Space complexity: O(1)

    ! =================================================================================================================
    |📌 NOTE
    @Advantages
    => Simple and easy to understand
    => Works well with small datasets

    @Disadvantages
    => Time complexity is O(n^2) in the worst case and average case
    => Does not work with large datasets
    => Does not preserve the relative order of items with equal keys which means it is not stable.

    @FAQs
    ! =========================
    🙋 Is Selection Sort Algorithm stable?
    -> The default implementation of the Selection Sort Algorithm is not stable. Because it Does not preserve the
    relative order of items with equal keys which means it is not stable.

    ! =========================
    🙋 Is Selection Sort Algorithm in-place?
    -> Yes, Selection Sort Algorithm is in-place and it does not require extra space.

    ! =================================================================================================================
    |🖇️ REFERENCES
    => geeksforgeeks: https://www.geeksforgeeks.org/selection-sort/

"""
# ! ===================================================================================================================
import unittest


def sort__using_selection(arr: list) -> list:
    for i in range(len(arr)):
        min_idx = i

        for j in range(i + 1, len(arr)):
            if arr[j] < arr[i]:
                min_idx = j

        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return arr


class TestSuite(unittest.TestCase):
    def test_sorting_an_array(self):
        arr = [1, 4, 3, 2, 0]
        expected = [0, 1, 2, 3, 4]
        actual = sort__using_selection(arr)

        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
