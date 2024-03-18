"""
    ❓ Question:
        =>> Given an array arr[] of size N, the task is to printing K largest (or smallest) elements in an array. Elements in output array can be in any order

    🗳️ Example:
        Input:  [1, 23, 12, 9, 30, 2, 50], K = 3
        Output: 50, 30, 23

        Input:  [11, 5, 12, 9, 44, 17, 2], K = 2
        Output: 44, 17

    🙌🏻 Approach:

        ! ==============================================================================================================
        =>> Approach 1: (Using SORTING)
            -> Sorting the input array by ASCENDING (or DESCENDING)
            -> Easily pick k largest or smallest element in the sorted array


        🚀 Complexities:
            ⌛ Time complexity: O(n)
            🌌 Space complexity: O(1)

        ! ==============================================================================================================
        =>> Approach 2: (Using BINARY SEARCH)
            -> Find the max and min elements of the input array
            -> Apply BINARY SEARCH for this range of (min, max)
            -> While left (min) < right (max), we iterate
                -> Find the mid point of the range
                -> Count the number that greater or equal to the mid point
                -> If count < k, we continue searching for the range (min, mid)
                -> If count > k, we continue searching for the range (mid + 1, max)
            -> return left


        🚀 Complexities:
            ⌛ Time complexity: O(n * log(m)) where m is the range from min to max
            🌌 Space complexity: O(1)

        ! ==============================================================================================================

====================================================================================================================================================================
"""

from typing import List


# ! Approach 1
def find_k_est_1st(arr, k):
    # Sort the given array arr in reverse order.
    ans = []
    arr.sort(reverse=True)
    # Print the first kth largest elements
    for i in range(k):
        print(arr[i], end=" ")
        ans.append(arr[i])

    return ans


# ! ==============================================================================================================
# ! Approach 2


def find_k_est_2nd(arr: List[int], k: int) -> int:
    left, right = min(arr), max(arr)  # O(n)
    if k == len(arr):
        return left

    while left < right:  # O(log(m)) where m is the range from min to max
        mid = left + (right - left) // 2
        count = count_larger_or_equal(arr, mid)  # O(n)

        if count < k:
            right = mid - 1
        else:
            left = mid + 1

    return left - 1


def count_larger_or_equal(arr: List[int], target: int) -> int:
    count = 0

    for num in arr:
        if num >= target:
            count += 1

    return count


def print_kth_est(arr: List[int], kth: int):
    k_est = []
    for num in arr:
        if num >= kth:
            k_est.append(num)

    print(f"K-est: {k_est}")
    return k_est
