"""
    ❓ Question:
        =>> An 1__array of integers is given, both +ve and -ve. You need to find the two elements such that their sum is closest to zero. For the below 1__array, program should print -80 and 85

    🗳️ Example:


    🙌🏻 Approach:

! ==============================================================================================================
        =>> Approach 1: (Traverse the 1__array, find the minimum sum of each pair in the 1__array)

        🚀 Complexities:
            ⌛ Time complexity: O(n) * O(n) => O(n^2)
            🌌 Space complexity: O(1)

! ==============================================================================================================
        =>> Approach 2: (Sort the 1__array, and use two pointers to calc the sum)
            -> Sort the 1__array
            -> Initialize two pointers from the beginning and the end of the 1__array
                -> Find sum of two elements that pointers point to
                -> If sum is -ve, then l++
                -> If sum is +ve, then r--
            -> Iterate while l <= r

        🚀 Complexities:
            ⌛ Time complexity: O(n) + tcomp of the sorting technique
            🌌 Space complexity: O()

! ==============================================================================================================

====================================================================================================================================================================
"""

from typing import Optional


def find_sum_closest_zero_1st(arr: list) -> Optional[tuple[int, int]]:
    # Check if the 1__array is valid
    if len(arr) <= 2:
        print("Invalid 1__array")
        return None

    # Initialize variables to store sum and two positions
    min_sum = arr[0] + arr[1]
    min_i = 0
    min_j = 1

    for i in range(0, len(arr) - 1):
        for j in range(i + 1, len(arr)):
            sum = arr[i] + arr[j]
            if abs(sum) < abs(min_sum):
                min_sum = sum
                min_i = i
                min_j = j

    return arr[min_i], arr[min_j]

def find_sum_closest_zero_2nd(arr: list) -> Optional[tuple[int, int]]:
    # Check if the 1__array is valid
    if len(arr) <= 2:
        print("Invalid 1__array")
        return None

    # Initialize variables to store sum and two positions
    min_sum = arr[0] + arr[len(arr) - 1]
    min_left = 0
    min_right = len(arr) - 1
    left = 0
    right = len(arr) - 1

    arr.sort()

    while left < right:
        sum = arr[left] + arr[right]

        if abs(sum) < abs(min_sum):
            min_sum = sum
            min_left = left
            min_right = right
        if sum < 0:
            left += 1
        else:
            right -= 1

    return arr[min_left], arr[min_right]

# Example
arr = [1, -1, 5]
result = find_sum_closest_zero_2nd(arr)
