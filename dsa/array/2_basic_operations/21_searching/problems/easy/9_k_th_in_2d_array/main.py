"""
    ❓ Question:
        =>> Given an n x n matrix, where every row and column is sorted in non-decreasing order. Find the kth smallest
        element in the given 2D array.

    🗳️ Example:
        Input: k = 3 and array =
                10, 20, 30, 40
                15, 25, 35, 45
                24, 29, 37, 48
                32, 33, 39, 50
        Output: 20
        Explanation: The 3rd smallest element is 20
        Input: k = 7 and array =
                10, 20, 30, 40
                15, 25, 35, 45
                24, 29, 37, 48
                32, 33, 39, 50
        Output: 30
        Explanation: The 7th smallest element is 30

    🙌🏻 Approach:
        ! ==============================================================================================================
        =>> Approach 1:
            ! Using BRUTE FORCE
            # * Why should we use Priority Queue here?
            # * For each element in the 2D array, it pushes the element onto the priority queue using heapq.heappush().
            # * This ensures that the smallest element encountered in the array is inserted into the priority queue,
            # * maintaining the min-heap property. However, it doesn't guarantee that the smallest element will be at
            # * the top of the priority queue at any given moment.
            -> Flatten the matrix using Priority Queue
            -> Initialize a counter, pop the queue k times

        🚀 Complexities:
            ⌛ Time complexity: O(n^2 * log(n^2))
            🌌 Space complexity: O(n^2)

        ! ==============================================================================================================
        =>> Approach 2:
            ! Using BINARY SEARCH
            -> Determine the range to take advantage of BINARY SEARCH: a[0][0] -> a[n-1][n-1]
            -> While left (a[0][0]) < right (a[n-1][n-1])
                >-> Calculate the middle point
                >-> Count the number which less than or equal to the middle point
                >-> Compare the count with k, if count < k
                    >-> If so, continue searching for the right side
                    >-> If not, continue searching for the left side
                >-> Return right

        🚀 Complexities:
            ⌛ Time complexity: O(log(max - min) * n)
            🌌 Space complexity: O(1)

        ! ==============================================================================================================
        =>> Approach 3:
            ! Using ARRAY
            -> Initialize a new array
            -> Copy all the elements of the matrix into that array
            -> Sort that array
            -> Find the k_th smallest element

        🚀 Complexities:
            ⌛ Time complexity: O(n^2 * time complexity of sorting technique)
            🌌 Space complexity: O(n*n)
"""
# ! ==============================================================================================================
# ! Approach 1

import heapq
from typing import List, TypeAlias

IntMatrix = List[List[int]]


def find_k_th_smallest_brute_force(arr: IntMatrix, n: int, k: int) -> int:
    pq = []
    for i in range(n):  # * O(n)
        for j in range(n):  # * O(n)
            heapq.heappush(pq, arr[i][j])  # * O(log(n^2))
    counter = 0
    while pq:  # * O(n * n)
        temp = heapq.heappop(pq)
        counter += 1
        if counter == k:
            return temp
    return -1


# ! ==============================================================================================================
# ! Approach 2
def find_k_th_smallest_binary_search(matrix: IntMatrix, n: int, k: int) -> int:
    left, right = matrix[0][0], matrix[n - 1][n - 1]

    while left < right:
        mid = left + (right - left) // 2
        count = count_less_equal(matrix, mid)
        if count < k:
            left = mid + 1
        else:
            right = mid
    return left


def count_less_equal(matrix: IntMatrix, target: int) -> int:
    count = 0
    n = len(matrix)
    i, j = n - 1, 0  # Start from the bottom-left corner
    while i >= 0 and j < n:
        if matrix[i][j] <= target:
            count += i + 1  # Count all elements in the current column
            j += 1  # Move to the next column
        else:
            i -= 1  # Move to the previous row
    return count


# ! ==============================================================================================================
# ! Approach 3
def find_k_th_smallest_sorted_array(matrix: IntMatrix, n: int, k: int) -> int:
    arr = [0 for z in range(n * n)]
    idx = 0

    for i in range(n):
        for j in range(n):
            arr[idx] = matrix[i][j]
            idx += 1

    arr.sort()
    return arr[k - 1]
