"""
    ❓ Question:
        =>> Given a binary array arr[] of size N, which is sorted in non-increasing order, count the number of 1’s in it.

    🚀 Expected Complexities:
        ⌛ Time complexity: O()
        🌌 Space complexity: O()

    🗳️ Example:
        Input: arr[] = {1, 1, 0, 0, 0, 0, 0}
        Output: 2

        Input: arr[] = {1, 1, 1, 1, 1, 1, 1}
        Output: 7

        Input: arr[] = {0, 0, 0, 0, 0, 0, 0}
        Output: 0

    🙌🏻 Approach:
        ! ==============================================================================================================

        =>> Approach 1: Naive Approach - For KIDS
        - Traverse the non-increasing array
        - Initialize a new variable to count the number of 1s
        - If we find the iter item is 0
            -> Break the loop -> Return the counter

        ! ==============================================================================================================

        =>> Approach 2: Using Binary Search
        - Initialize two pointers `left` and `right`
        - Initialize a new variable to store the last 1s index named `last_one_index`
        - Loop through the non-increasing array when left <= right
            -> Calculate the mid = left + (right - left) // 2
            -> if arr[mid] == 1, then we will search for the right and the left if not.
        - After the loop, return the `last_one_index + 1` (the number of 1s number)

        ! ==============================================================================================================


====================================================================================================================================================================
"""

def count_1s_2nd(arr: list) -> int:
    # Initialize two pointers and a variable to store the position of the last 1s number
    left, right = 0, len(arr) - 1
    last_one_index = -1

    # Loop through the array while left <= right
    while left <= right:
        # Calculate the middle
        mid = left + (right - left) // 2

        if arr[mid] == 1:
            last_one_index = mid

            # Try to find the last 1s in the right side
            left = mid + 1
        # In the case, the middle is not equal to `1`, search the left side
        else:
            right = mid - 1

    return last_one_index + 1
