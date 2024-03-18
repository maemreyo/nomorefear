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
        =>> Approach 1: (Using Brute Force)
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


        🚀 Complexities:
            ⌛ Time complexity: O()
            🌌 Space complexity: O()

        ! ==============================================================================================================
"""
import heapq
from typing import List


# ! Approach 1
def find_k_th_smallest(arr: List[List[int]], n: int, k: int) -> int:
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
