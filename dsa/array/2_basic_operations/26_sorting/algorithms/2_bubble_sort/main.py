"""
    |〽️ BUBBLE SORT

    ! =================================================================================================================
    |🔎 GENERAL
    ==> Bubble Sort is the simplest sorting algorithm that works by repeatedly swapping the adjacent elements if they
    are in the wrong order.

    ! =================================================================================================================
    |⚙️ HOW IT WORKS?
    @Comparison and Swapping
    ==> Bubble sort starts at the beginning of the list and compares each pair of adjacent elements. If the elements are
    in the wrong order (for example: the left item is greater than the right item for sorting in ascending order), the
    algorithm swaps them.

    @Passes through the list
    ==> After the first pass through the list, the largest (or the smallest) element will have "bubbled up" to the end
    of the list.
    ==> In subsequent passes, the algorithm works on the remaining unsorted portions of the list.

    @Termination
    ==> The algorithm terminates when no more swaps are needed during a pass through the list, indicating that the list
    is sorted.

    ! =================================================================================================================
    |📟 PSEUDOCODE
    BubbleSort(arr):
        n = length of arr
        swapped = True

        while swapped is True:
            swapped = False

            for i from 0 to n-2:
                if arr[i] > arr[i+1]:
                    swap arr[i] with arr[i+1]
                    swapped = True

    ! =================================================================================================================
    |🚀 COMPLEXITIES:
        + ⌛ Time complexity: O(n^2)
        + 🌌 Space complexity: O(1)

    ! =================================================================================================================
    |📌 NOTE
    @Advantages
    => Easy to understand and implement.
    => Does not require any additional memory space.
    => It is a stable sorting algorithm, meaning that elements with the same key value maintain their relative order in
    the sorted output.

    @Disadvantages
    => Time complexity is O(n^2) => slow for large datasets
    => Is a comparison-based sorting algorithm, which means that it requires a comparison operator to determine the
    relative order of elements in the input dataset => Limit the efficiency of the algorithm in certain cases.

    @FAQs
    ! =========================
    🙋 What is the Boundary Case for Bubble Sort?
    ==> Bubble Sort takes minimum time (Order of n) when elements are already sorted. Hence it is best to check if the
    array is already sorted or not beforehand, to avoid O(n^2) time complexity.

    ! =========================
    🙋 Does sorting happen in-place in Bubble Sort?
    ==> Yes, Bubble Sort performs the swapping of adjacent pairs without the use of any major data structure. Hence it
    is an in-place algorithm

    ! =========================
    🙋 Is the Bubble Sort algorithm stable?
    ==> Yes, it is stable.
    A sorting algorithm is considered stable if it preserves the relative order of equal elements in the input array. In
    other words, if two elements have the same value and the first one appears before the second one in the input array,
    they should also appear in the same order in the sorted array.

    Bubble sort satisfies this property because it only swaps adjacent elements if they are out of order. When two
    adjacent elements have the same value, bubble sort does not swap them, which ensures that their relative order
    remains unchanged. As a result, the original order of equal elements is preserved in the sorted array.

    For example, consider the input array [3, 2, 1, 2]. After sorting using bubble sort, the array becomes [1, 2, 2, 3].
    The two 2 elements in the input array appear in the same order in the sorted array, demonstrating the stability of
    the bubble sort algorithm.

    ! =========================
    🙋 Where is the Bubble Sort algorithm used?
    ==> Due to its simplicity, bubble sort is often used to introduce the concept of a sorting algorithm. In computer
    graphic, it is popular for its capabilities to detect a tiny error (like a swap of just two elements) in
    sorted-arrays and fix it with just linear complexity (2n).

    ! =================================================================================================================
    |🖇️ REFERENCES
    => geeksforgeeks: https://www.geeksforgeeks.org/bubble-sort/
    => Recursive Bubble Sort: https://www.geeksforgeeks.org/recursive-bubble-sort/
    => Coding practice for sorting: https://www.geeksforgeeks.org/explore?page=1&category=Sorting&sortBy=submissions&itm_source=geeksforgeeks&itm_medium=main_header&itm_campaign=practice_header
    => Quiz on Bubble Sort: https://www.geeksforgeeks.org/top-mcqs-on-bubblesort-algorithm-with-answers/
    => Complexity Analysis of Bubble Sort: https://www.geeksforgeeks.org/time-and-space-complexity-analysis-of-bubble-sort/

"""
# ! ===================================================================================================================
import unittest


def bubble_sort(arr: list) -> list:
    n = len(arr)
    is_swapped = True

    while is_swapped is True:
        is_swapped = False

        for i in range(n - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]

                is_swapped = True

    return arr


class TestSuite(unittest.TestCase):
    def test_sorting_an_array(self):
        arr = [1, 4, 3, 2, 0]
        expected = [0, 1, 2, 3, 4]
        actual = bubble_sort(arr)

        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
