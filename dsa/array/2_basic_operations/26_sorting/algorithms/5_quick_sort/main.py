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
            -> Best case: O(n*log(n))
            -> Average case: O(n*log(n))
            -> Worst case: O(n^2)
        🌌 Space complexity:
            -> Average case: O(log(n))
            -> Worst case: O(n)

    ! =================================================================================================================
    |📌 NOTE
    @Advantages
    => It is a divide-and-conquer algorithm that makes it easier to solve problems.
    => It is efficient on large data sets.
    => It has a low overhead, as it only requires a small amount of memory to function.

    @Disadvantages
    => It has a worst-case time complexity of O(N2), which occurs when the pivot is chosen poorly.
    => It is not a good choice for small data sets.
    => It is not a stable sort, meaning that if two elements have the same key, their relative order will not be preserved in
    the sorted output in case of quick sort, because here we are swapping elements according to the pivot’s position (without considering their original positions).

    ! =================================================================================================================
    |👀 FAQs
    ! =========================
    Q. What are the Boundary Cases of the Quick Sort Algorithm?
    -> Quick Sort takes the maximum time to sort if the chosen pivot divides the array into extremely unbalanced
    partitions, such as the smallest or largest element as the pivot.
    -> It takes minimum time O(n) when the chosen pivot consistently divides the array into roughly equal-sized
    partitions.

    ! =========================
    Q. What is the Algorithmic Paradigm of the Quick Sort Algorithm?
    -> The Quick Sort Algorithm follows "Divide and Conquer" paradigm

    ! =========================
    Q. Is Quick Sort Algorithm an in-place sorting algorithm?
    -> Yes, the Quick Sort algorithm is typically implemented as an in-place sorting algorithm.

    ! =========================
    Q. Is Quick Sort Algorithm a stable algorithm?
    -> No, the Quick Sort algorithm is not stable.
        Quick Sort, however, does not guarantee stability. During the partitioning process, Quick Sort may reorder equal
    elements (those with the same value) arbitrarily, depending on the choice of pivot and the partitioning logic. As a
    result, the relative order of equal elements in the input array may not be preserved in the sorted output.

    ! =========================
    Q. When is the Quick Sort Algorithm used?
    -> It is commonly used in various scenarios where efficient sorting of large arrays is required:
        -> General sorting for large datasets
            Quick Sort is one of the most efficient general-purpose sorting algorithms, particularly for large arrays.
            Its average-case time complexity of O(n log n) makes it suitable for sorting large datasets quickly.
        -> Applications requiring in-place sorting
            Quick Sort's ability to perform sorting in place, with a relatively small amount of additional memory,
            makes it well-suited for applications with limited memory resources.
        -> Implementing libraries and frameworks
            Quick Sort is often used as the default sorting algorithm in libraries and frameworks due to its efficiency
            and versatility. Many programming languages and standard libraries include Quick Sort implementations for
            sorting arrays and collections.
        -> Real-time systems
            In applications requiring fast response times and low latency, such as real-time data processing and
            embedded systems, Quick Sort's efficient average-case performance can be advantageous.
        -> Parallel processing
            Quick Sort can be parallelized effectively, allowing multiple processors or threads to sort different parts
            of the array concurrently. This parallelization can lead to significant performance gains on multi-core
            processors or distributed systems.
        -> Educational Purposes
            Quick Sort is frequently taught in computer science courses and textbooks due to its elegance, simplicity,
            and importance in understanding fundamental sorting algorithms and principles of algorithm design.

    ! =================================================================================================================
    |🖇️ REFERENCES
    + QuickSort Algorithm by Abdul Bari: https://www.youtube.com/watch?v=7h1s2SojIRw&ab_channel=AbdulBari
    + Geeksforgeeks: https://www.geeksforgeeks.org/quick-sort/

"""
# ! ===================================================================================================================
import unittest


def quick_sort(arr):
    # Helper function to perform the partitioning
    def partition(arr, low, high):
        # Choose the pivot element (the first element)
        pivot = arr[low]
        i = low + 1
        j = high

        while True:
            # Move the left pointer to the right until finding an element greater than the pivot
            while i <= j and arr[i] <= pivot:
                i += 1

            # Move the right pointer to the left until finding an element smaller than the pivot
            while j >= i and arr[j] >= pivot:
                j -= 1

            # If the pointers have crossed, break the loop
            if i > j:
                break

            # Swap the elements at the left and right pointers
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1

        # Swap the pivot with the element at the right pointer's position
        arr[low], arr[j] = arr[j], arr[low]

        # Return the index of the pivot element
        return j

    # Recursive function to perform the quick sort
    def quick_sort_recursive(arr, low, high):
        if low < high:
            # Partition the array and get the pivot index
            pivot_index = partition(arr, low, high)

            # Recursively sort the sub-arrays on the left and right of the pivot
            quick_sort_recursive(arr, low, pivot_index - 1)
            quick_sort_recursive(arr, pivot_index + 1, high)

    # Call the recursive function with the initial low and high indices
    quick_sort_recursive(arr, 0, len(arr) - 1)


class TestSuite(unittest.TestCase):
    def test_sorting_an_array(self):
        arr = [1, 4, 3, 2, 0]
        expected = [0, 1, 2, 3, 4]

        quick_sort(arr)

        self.assertEqual(expected, arr)


if __name__ == '__main__':
    unittest.main()
