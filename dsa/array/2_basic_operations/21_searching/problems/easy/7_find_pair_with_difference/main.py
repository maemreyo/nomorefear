"""
    ❓ Question:
        =>> Given an unsorted array and a number n, find if there exists a pair of elements in the array whose difference is n

    🗳️ Example:
        Input: arr[] = {5, 20, 3, 2, 50, 80}, n = 78
        Output: Pair Found: (2, 80)

        Input: arr[] = {90, 70, 20, 80, 50}, n = 45
        Output: No Such Pair

    🙌🏻 Approach:
! ==============================================================================================================
        =>> Approach 1: (Using two loops to calc differences)

        🚀 Complexities:
            ⌛ Time complexity: O(n^2)
            🌌 Space complexity: O(1)

! ==============================================================================================================
        =>> Approach 2: (Using SORTED ARRAY to find the element which it plus with n equal to elements in the array)
            -> Sorted the array
            -> Initialize two pointers (left and right), and then do the BINARY SEARCH

        🚀 Complexities:
            ⌛ Time complexity: O(log n) + tcomp of sorting method
            🌌 Space complexity: O()

! ==============================================================================================================

====================================================================================================================================================================
"""

from typing import List, Optional


def find_pair_with_difference_1st(arr: list, n: int) -> Optional[List[tuple[int, int]]]:
    # Check if the array is valid
    if len(arr) < 2:
        return None

    ans = []

    for i in range(0, len(arr) - 1):
        for j in range(i + 1, len(arr)):
            diff = abs(arr[i] - arr[j])

            if diff == n:
                ans.append((arr[i], arr[j]))
            else:
                continue

    if ans == []:
        return None

    return ans

find_pair_with_difference_1st([4, 2, 6, 8, 1], 2)
