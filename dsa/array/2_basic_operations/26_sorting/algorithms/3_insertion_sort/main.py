"""
    |〽️ INSERTION SORT

    ! =================================================================================================================
    |🔎 GENERAL
    ==> Insertion Sort is a simple sorting algorithm that works similarly to the way you sort playing cards in your
    hands. The array is virtually split into a sorted and an unsorted part. Values from the unsorted part are picked and
    placed in the correct position in the sorted part.

    ! =================================================================================================================
    |⚙️ HOW IT WORKS?
    @Initialization
    ==> The algorithm starts with the first element of the list considered as the only element in the sorted part of the
    list. The rest of the list is considered unsorted.

    @Iterative Sorting
    ==> For each element in the unsorted part of the list, the algorithm compares it with the elements in the sorted
    part of the list, starting from the end.
    It then shifts all the elements greater than the current element to the right to make space for the current element.
    This step effectively inserts the current element into its correct position in the sorted part of the list.

    @Termination
    ==> The algorithm continues this process until all elements have been considered and inserted into their correct
    positions. At this point, the entire array is sorted.

    ! =================================================================================================================
    |📟 PSEUDOCODE
        InsertionSort(arr):
            n = length of arr

            for i from 1 to n-1:
                key = arr[i]
                j = i - 1

                # Move elements of arr[0..i-1], that are greater than key, to one position ahead of their current position
                while j >= 0 and arr[j] > key:
                    arr[j + 1] = arr[j]
                    j = j - 1

                arr[j + 1] = key

    ! =================================================================================================================
    |🚀 COMPLEXITIES:
        ⌛ Time complexity: O(n^2)
        🌌 Space complexity: O(1)

    ! =================================================================================================================
    |📌 NOTE
    @Advantages
    => Simple implementation: straightforward to implement, making it a good choice for educational purposes.
    => Efficient for Small Datasets.
    => Adaptive: It performs well on nearly sorted arrays. When the input array is already partially sorted, insertion
    sort requires fewer comparisons and swaps, leading to improved performance.

    @Disadvantages
    => Inefficient for Large Datasets due to time complexity O(n^2).
    => Not stable for some implementations: generally considered a stable sorting algorithm, but some implementations
    may not preserve the relative order of equal elements.
    => Quadratic Time Complexity

    ! =================================================================================================================
    |👀 FAQs
    ! =========================
    Q. What are the Boundary Cases of the Insertion Sort Algorithm?
    -> Insertion Sort takes the maximum time to sort if elements are sorted in reverse order.
    -> It takes minimum time O(n) when elements are already sorted.

    ! =========================
    Q. What is the Algorithmic Paradigm of the Insertion Sort Algorithm?
    -> The Insertion Sort Algorithm follows `an incremental approach`
    Note: In this paradigm, the algorithm builds the final sorted sequence incrementally, by repeatedly inserting
    elements into their correct positions within the already sorted portion of the sequence.

    ! =========================
    Q. Is Insertion Sort Algorithm an in-place sorting algorithm?
    -> Yes, it is an in-place sorting algorithm

    ! =========================
    Q. Is Insertion Sort Algorithm a stable algorithm?
    -> Yes, in general, it is a stable algorithm

    ! =========================
    Q. When is the Insertion Sort Algorithm used?
    -> Insertion sort is used when number of elements is small. It can also be useful when the input array is almost
    sorted, and only a few elements are misplaced in a complete big array.

    ! =================================================================================================================
    |🖇️ REFERENCES
    + geeksforgeeks: https://www.geeksforgeeks.org/insertion-sort/

"""
# ! ===================================================================================================================
import unittest


def sort__using_insertion(arr: list) -> list:
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):

        key = arr[i]

        # Move elements of arr[0..i-1], that are greater than key, to one position ahead  of their current position
        j = i - 1
        while j >= 0 and key < arr[j]:
            # Move the greater one to the current position
            arr[j + 1] = arr[j]

            # Continue with the next position
            j -= 1

        # Insert the current element to the right position
        arr[j + 1] = key

    return arr


class TestSuite(unittest.TestCase):
    def test_sorting_an_array(self):
        arr = [1, 4, 3, 2, 0]
        expected = [0, 1, 2, 3, 4]
        actual = sort__using_insertion(arr)

        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
