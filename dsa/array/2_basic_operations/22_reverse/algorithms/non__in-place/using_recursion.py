"""
    ❓ Question:
        =>> Given an array (or string), the task is to reverse the array/string.
        Note: for strings as input, we simply convert that string to the array using `list(string)`

    🙌🏻 Approach:
        ! Using RECURSION (NOT IN-PLACE)
        -> Base case: If the array is empty or has only one element, return the array itself
        -> Recursive case: Reverse the sub-array excluding the first element, and concatenate the first element at the
        end of the reversed sub-array

        🚀 Complexities:
            ⌛ Time complexity: O(n)
            🌌 Space complexity: O(n)
"""


# ! ==============================================================================================================
def reverse__recursion(arr: list) -> list:
    # Base case: If the array is empty or has only one element, return the array itself
    if len(arr) <= 1:
        return arr

    # Recursive case: Reverse the sub-array excluding the first element,
    # and concatenate the first element at the end of the reversed sub-array
    return reverse__recursion(arr[1:]) + [arr[0]]
