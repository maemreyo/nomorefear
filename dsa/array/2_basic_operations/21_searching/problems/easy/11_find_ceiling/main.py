"""
    ❓ Question:
        =>> Given a sorted array and a value x, the ceiling of x is the smallest element in an array greater than or
        equal to x, and the floor is the greatest element smaller than or equal to x.
        Assume that the array is sorted in non-decreasing order. Write efficient functions to find the floor and ceiling
        of x.

    🗳️ Example:
        Input: arr = [1, 2, 8, 10, 10, 12, 19]
        Output:
            -> For x = 0: floor doesn't exist in array - ceil = 1
            -> For x = 1: floor = 1 and ceil = 1
            -> For x = 5: floor = 2 and ceil = 8
            -> For x = 20: floor = 19 and ceil doesn't exist in array

    🙌🏻 Approach:
        ! ==============================================================================================================
        * Approach 1:
            ! Using LINEAR SEARCH
            -> If x is smaller than the first element in the array then return 0 (index of the first element)
            -> Else linearly search for an index i such that x lies between arr[i] and arr[i+1]
            -> If we do not find an index i in step 2, then return -1

        🚀 Complexities:
            ⌛ Time complexity: O(n)
            🌌 Space complexity: O(1)

        ! ==============================================================================================================

        * Approach 2:
            ! Using


        🚀 Complexities:
            ⌛ Time complexity: O()
            🌌 Space complexity: O()
"""


# ! ==============================================================================================================
# ! Approach 1
def find_ceiling__linear_search(arr, x, low, high) -> int:
    # If x is smaller than the first element in the array then return 0 (index of the first element)
    if x < arr[low]:
        return 0

    # Else linearly search for an index i such that x lies between arr[i] and arr[i+1]
    for i in range(high):
        if arr[i] == x:
            return i

        if arr[i] < x <= arr[i + 1]:
            return i + 1

    return -1
