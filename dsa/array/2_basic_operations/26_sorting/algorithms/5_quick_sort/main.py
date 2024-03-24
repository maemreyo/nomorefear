"""
    |〽️ QUICK SORT

    ! =================================================================================================================
    |🔎 GENERAL
    ==> Quick Sort is a sorting algorithm based on the Divide and Conquer algorithm that picks an element as a pivot
    and partitions the given array around the picked pivot by placing the pivot in its correct position in the sorted
    array.

    ! =================================================================================================================
    |⚙️ HOW IT WORKS?
    @Choose a Pivot
    -> Select a pivot element from the array.
    -> The pivot can be chosen in various ways, such as selecting the first element, last element, median-of-three, or
    a random element. The choice of pivot affects the performance of the algorithm.

    @Partitioning
    -> Reorder the array so that all elements less than the pivot come before it, and all elements greater than the
    pivot come after it.
    -> After this partitioning step, the pivot element is in its final sorted position. This process is sometimes called
    partitioning around a pivot"

    @Recursively Sort Sub-arrays
    -> Recursively apply the Quick Sort algorithm to the sub-arrays formed by the partitioning step.
    -> This process continues until the  base case is reached, where the sub-array has zero or one element (which is
    already sorted)

    @Combine Sorted Sub-arrays
    -> As the recursion unwinds, the sorted sub-arrays are combined to produce the final sorted array. Since the pivot
    elements are already in their correct positions after partitioning, no additional work is needed to merge the \
    sub-arrays.

    ! =================================================================================================================
    |📟 PSEUDOCODE
    QuickSort(arr, low, high):
        if low < high:
            # Partition the array
            pivot_index = Partition(arr, low, high)

            # Recursively sort the left and right sub-arrays
            QuickSort(arr, low, pivot_index - 1)
            QuickSort(arr, pivot_index + 1, high)

    Partition(arr, low, high):
        # Choose the pivot element (e.g., the last element)
        pivot = arr[high]

        # Initialize the index of the smaller element
        smaller_index = low - 1

        # Partition the array around the pivot
        for j from low to high - 1:
            if arr[j] <= pivot:
                # Increment the index of the smaller element
                smaller_index++
                # Swap arr[smaller_index] and arr[j]
                Swap(arr, smaller_index, j)

        # Swap the pivot element into its correct position
        Swap(arr, smaller_index + 1, high)

        # Return the index of the pivot element
        return smaller_index + 1

    Swap(arr, i, j):
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp

    ! =================================================================================================================
    |🚀 COMPLEXITIES:
        ⌛ Time complexity:
            -> Average case: O(n*log(n))
            -> Worst case: O(n^2)
        🌌 Space complexity:
            -> Average case: O(log(n))
            -> Worst case: O(n)

    ! =================================================================================================================
    |📌 NOTE
    @xxx
    =>

    ! =================================================================================================================
    |👀 FAQs
    ! =========================
    Q. xxx
    ->

    ! =========================
    Q. xxx
    ->

    ! =================================================================================================================
    |🖇️ REFERENCES


"""
# ! ===================================================================================================================
import unittest


def quick_sort(arr: list) -> list:
    # Helper function to perform the partitioning
    def partition(arr, low, high):
        # Choose the pivot element
        pivot = arr[high]
        i = low - 1

        # Partition the array around the pivot
        for j in range(low, high):
            if arr[j] < pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]  # Swap elements

        # Place the pivot element in its correct position
        arr[i + 1], arr[high] = arr[high], arr[i + 1]

        return i + 1

    # Recursive function to perform the quick sort
    def recursive(arr, low, high):
        if low < high:
            # Partition the array and get the pivot index
            pivot_index = partition(arr, low, high)

            # Recursively sort the sub-arrays on the left and right of the pivot
            recursive(arr, low, pivot_index - 1)
            recursive(arr, pivot_index + 1, high)

    recursive(arr, 0, len(arr) - 1)


class TestSuite(unittest.TestCase):
    def test_sorting_an_array(self):
        arr = [1, 4, 3, 2, 0]
        expected = [0, 1, 2, 3, 4]
        actual = quick_sort(arr)

        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
