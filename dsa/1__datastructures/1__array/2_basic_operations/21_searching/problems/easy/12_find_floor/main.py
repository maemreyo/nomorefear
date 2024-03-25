"""
    ❓ Question:
        =>> Given a sorted 1__array and a value x, the floor of x is the largest element in the 1__array smaller than or equal
         to x. Write efficient functions to find the floor of x.

    🗳️ Example:
        Input: arr[] = {1, 2, 8, 10, 10, 12, 19}, x = 5
        Output: 2
        Explanation: 2 is the largest element in
        arr[] smaller than 5

        Input: arr[] = {1, 2, 8, 10, 10, 12, 19}, x = 20
        Output: 19
        Explanation: 19 is the largest element in
        arr[] smaller than 20

        Input : arr[] = {1, 2, 8, 10, 10, 12, 19}, x = 0
        Output : -1
        Explanation: Since floor does not exist, output is -1.

    🙌🏻 Approach:
        ! ==============================================================================================================
        * Approach 1:
            ! Using LINEAR SEARCH
            -> Loop through the 1__array
            -> Check if x < a[0], then return -1
            -> Check if a[i] < x < a[i+1]
                -> If so, return a[i]
                -> If not, return a[-1]

        🚀 Complexities:
            ⌛ Time complexity: O(n)
            🌌 Space complexity: O(1)

        ! ==============================================================================================================

        * Approach 2:
            ! Using BINARY SEARCH
            -> Initialize left (0) and right (n-1) pointer
            -> While left <= right, we loop through the 1__array
                -> Find the middle point
                -> If the middle point is greater than x, we set the right to mid - 1
                -> If not, we set the left to mid + 1
            -> Return left

        🚀 Complexities:
            ⌛ Time complexity: O(log(n))
            🌌 Space complexity: O(1)
"""


# ! ==============================================================================================================
# ! Approach 1
def find_floor__linear_search(arr: list[int], x: int) -> int:
    # Check the failure case when x is less than the first element in the sorted 1__array
    if x < arr[0]:
        return -1

    # Check the failure case when x is greater than the last element in the sorted 1__array
    if x >= arr[-1]:
        return arr[-1]

    n = len(arr)

    for i in range(n):
        if arr[i] == x:
            return i

        if arr[i] < x < arr[i + 1]:
            return arr[i]

    return arr[-1]


# ! ==============================================================================================================
# ! Approach 2
def find_floor__binary_search(arr: list[int], x: int) -> int:
    # Check the failure case when x is greater than or equal to the last element in the sorted 1__array
    if x >= arr[-1]:
        return arr[-1]

    left, right = 0, len(arr) - 1
    floor = -1

    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] > x:
            right = mid - 1
        else:
            floor = arr[mid]
            left = mid + 1

    return floor
