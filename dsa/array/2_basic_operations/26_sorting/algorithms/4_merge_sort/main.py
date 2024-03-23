"""
    |〽️ MERGE SORT

    ! =================================================================================================================
    |🔎 GENERAL
    ==> Merge sort is defined as a sorting algorithm that works by dividing an array into smaller sub-arrays, sorting
    each sub-array, and then merging the sorted sub-arrays back together to form the final sorted array.

    ==> We can say that the process of merge sort is to divide the array into two halves, sort each half, and then merge
    the sorted halves back together. This process is repeated until the entire array is sorted.

    ! =================================================================================================================
    |⚙️ HOW IT WORKS?
    MERGE SORT is a divide-and-conquer sorting algorithm that works as follows:
    @Divide
    ==> The input array is recursively divided into two halves until each sub-array contains only one element. This
    process continues until the sub-arrays are too small to be divided further.
        -> The input array is recursively divided into two halves
        -> The divide step is performed recursively on each half until each sub-array contains only one element

    @Conquer
    ==> The divided sub-arrays are then merged back together in a sorted order. During the merging process, elements
    from two sub-arrays are compared and merged into a single sorted array.
        -> Once the base case is reached (the sub-arrays contain only one element), the merge process begins
        -> During the merge process, adjacent sub-arrays are merged together in a sorted order
        -> This merging process is repeated recursively, merging larger and larger sub-arrays until the entire array is
        sorted

    @Merge
    ==> As the algorithm processes back up the recursion tree, the sorted sub-arrays are recursively merged into larger
    sorted sub-arrays until the entire array is sorted.
        -> To merge two sorted sub-arrays, a third array (the auxiliary array) is used
        -> Elements from the two sub-arrays are compared, and the smalled (or larger, depending on the desired sorting
        order) element is placed into the auxiliary array
        -> The process continues until all elements from both sub-arrays are merged into the auxiliary array
        -> Finally, the auxiliary array is copied back into the original array, effectively merging the two sorted
        sub-arrays into a single sorted array

    ! =================================================================================================================
    |📟 PSEUDOCODE
    MergeSort(arr):
        if length of arr is less than or equal to 1:
            return arr

        # Divide the array into two halves
        mid = length of arr / 2
        left_half = first half of arr
        right_half = second half of arr

        # Recursively sort the two halves
        left_half = MergeSort(left_half)
        right_half = MergeSort(right_half)

        # Merge the sorted halves
        sorted_arr = Merge(left_half, right_half)
        return sorted_arr

    Merge(left_half, right_half):
        merged_arr = empty array
        left_index = 0
        right_index = 0

        # Compare elements from the two halves and merge them into a single sorted array
        while left_index < length of left_half and right_index < length of right_half:
            if left_half[left_index] <= right_half[right_index]:
                append left_half[left_index] to merged_arr
                left_index++
            else:
                append right_half[right_index] to merged_arr
                right_index++

        # Append any remaining elements from the left half
        while left_index < length of left_half:
            append left_half[left_index] to merged_arr
            left_index++

        # Append any remaining elements from the right half
        while right_index < length of right_half:
            append right_half[right_index] to merged_arr
            right_index++

        return merged_arr

    ! =================================================================================================================
    |🚀 COMPLEXITIES:
        ⌛ Time complexity: O(n*log(n))
        🌌 Space complexity: O(n)

    ! =================================================================================================================
    |📌 NOTE
    @Advantages
    => Stability: Merge sort is a stable sorting algorithm, which means it maintains the relative order of equal
    elements in the input array.
    => Guaranteed worst-case performance: Merge sort has a worst-case time complexity of O(n*log(n)), which means it
    performs well even on large datasets.
    => Parallelism: Merge sort is a naturally parallelizable algorithm, which means it can be easily parallelized to
    take advantage of multiple processors or threads.

    @Disadvantages
    => Space complexity: Merge sort requires additional memory to store the merged sub-arrays during the sorting process.
    => Not in-place: Merge sort is not an in-place sorting algorithm, which means it requires additional memory to store
    the sorted data. This can be a disadvantage in applications where memory usage is a concern.
    => Not always optimal for small datasets: For small datasets, Merge sort has a higher time complexity than some
    other sorting algorithms, such as Insertion Sort. This can result in slower performance for very small datasets.

    @Applications
    => Sorting large datasets: Merge sort is particularly well-suited for sorting large datasets due to its guaranteed
    worst-case time complexity of O(n*log(n)).
    => External sorting: Merge sort is commonly used in external sorting, where the data to be sorted is too large to
    fit into memory.
    => Custom sorting: Merge sort can be adapted to handle different input distributions, such as partially sorted,
    nearly sorted, or completely unsorted data.
    => Inversion Count Problem

    ! =================================================================================================================
    |👀 FAQs
    ! =========================
    Q. What are the Boundary Cases of the Merge Sort Algorithm?
    -> Merge sort generally takes maximum time to sort when the input array is in reverse order or nearly reverse order.
    -> Merge sort typically takes minimum time to sort when the input array is already sorted or nearly sorted.

    ! =========================
    Q. What is the Algorithmic Paradigm of the Merge Sort Algorithm?
    -> Merge sort algorithm follows the "Divide-and-Conquer" paradigm
    -> The algorithm divides the input array into smaller sub-arrays recursively until each sub-array contains only one
    element
    -> It then merges the sorted sub-arrays back together to produce the final sorted array

    ! =========================
    Q. Is Merge Sort Algorithm an in-place sorting algorithm?
    -> No, Merge sort is not an in-place sorting algorithm
    -> It typically requires additional space proportional to the size of the input array for merging sub-arrays

    ! =========================
    Q. Is Merge Sort Algorithm a stable algorithm?
    -> Yes, it is a stable algorithm, it preserves the relative order of equal elements in the sorted array.

    ! =========================
    Q. When is the Merge Sort Algorithm used?
    -> Sorting large arrays efficiently
    -> Sorting linked lists, where random access is not efficient
    -> As a building block for other algorithms, such as External Sorting algorithms and Parallel algorithms
    -> Merge Sort's stable nature and efficient performance make it suitable for a wide range of sorting tasks,
    especially when the data size is large or when stability is required

    ! =================================================================================================================
    |🖇️ REFERENCES
    + geeksforgeeks: https://www.geeksforgeeks.org/merge-sort/
    + Inversion Count Problem: https://www.geeksforgeeks.org/inversion-count-in-array-using-merge-sort/
    + Recent Articles on Merge Sort: https://www.geeksforgeeks.org/tag/merge-sort/
    + Coding practice for sorting: https://www.geeksforgeeks.org/explore?page=1&category=Sorting&sortBy=submissions&itm_source=geeksforgeeks&itm_medium=main_header&itm_campaign=practice_header
    + Quiz on Merge Sort: https://www.geeksforgeeks.org/quiz-mergesort-gq/

"""
# ! ===================================================================================================================
import unittest


def merge_sort(arr: list) -> list:
    if len(arr) <= 1:
        return arr

    # Divide the array into two halves
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Recursively sort the two halves
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    # Merge the sorted halves
    return merge(left_half, right_half)


def merge(left_half, right_half):
    merged_arr = []
    left_index, right_index = 0, 0

    # Compare elements from the two halves and merge them into a single sorted array
    while left_index < len(left_half) and right_index < len(right_half):
        if left_half[left_index] <= right_half[right_index]:
            merged_arr.append(left_half[left_index])
            left_index += 1
        else:
            merged_arr.append(right_half[right_index])
            right_index += 1

    # Append any remaining elements from the left half
    while left_index < len(left_half):
        merged_arr.append(left_half[left_index])
        left_index += 1

    # Append any remaining elements from the right half
    while right_index < len(right_half):
        merged_arr.append(right_half[right_index])
        right_index += 1

    return merged_arr


class TestSuite(unittest.TestCase):
    def test_sorting_an_array(self):
        arr = [1, 4, 3, 2, 0]
        expected = [0, 1, 2, 3, 4]
        actual = merge_sort(arr)

        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
