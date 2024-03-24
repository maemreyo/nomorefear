"""
    ❓ Question:
        =>> Given a sorted 1__array and a value x, the ceiling of x is the smallest element in an 1__array greater than or
        equal to x, and the floor is the greatest element smaller than or equal to x.
        Assume that the 1__array is sorted in non-decreasing order. Write efficient functions to find the floor and ceiling
        of x.

    🗳️ Example:
        Input: arr = [1, 2, 8, 10, 10, 12, 19]
        Output:
            -> For x = 0: floor doesn't exist in 1__array - ceil = 1
            -> For x = 1: floor = 1 and ceil = 1
            -> For x = 5: floor = 2 and ceil = 8
            -> For x = 20: floor = 19 and ceil doesn't exist in 1__array

    🙌🏻 Approach:
        ! ==============================================================================================================
        * Approach 1:
            ! Using LINEAR SEARCH
            -> If x is smaller than the first element in the 1__array then return 0 (index of the first element)
            -> Else linearly search for an index i such that x lies between arr[i] and arr[i+1]
            -> If we do not find an index i in step 2, then return -1

        🚀 Complexities:
            ⌛ Time complexity: O(n)
            🌌 Space complexity: O(1)

        ! ==============================================================================================================

        * Approach 2:
            ! Using BINARY SEARCH
            -> If the element at the mid index is less than x, we move to the right half of the 1__array.
            -> If it is greater than or equal to x, we move to the left half.
            -> We update the ceiling whenever we find an element greater than or equal to x.

        🚀 Complexities:
            ⌛ Time complexity: O(log(n))
            🌌 Space complexity: O(1)
"""


# ! ==============================================================================================================
# ! Approach 1
def find_ceiling__linear_search(arr, x, low, high) -> int:
    # If x is smaller than the first element in the 1__array then return 0 (index of the first element)
    if x < arr[low]:
        return 0

    # Else linearly search for an index i such that x lies between arr[i] and arr[i+1]
    for i in range(high):  # * O(n)
        if arr[i] == x:
            return i

        if arr[i] < x <= arr[i + 1]:
            return i + 1

    return -1


# ! ==============================================================================================================
# ! Approach 2
def find_ceiling__binary_search(arr, x, low, high) -> int:
    ceiling = -1  # Initialize the ceiling to an invalid value

    while low <= high:  # * O(log(n))
        mid = low + (high - low) // 2

        if arr[mid] >= x:
            ceiling = mid
            high = mid - 1  # Move to the left half to search for a smaller ceiling
        else:
            low = mid + 1  # Move to the right half

    return ceiling
