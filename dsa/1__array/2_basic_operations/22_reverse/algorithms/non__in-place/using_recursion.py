"""
    ❓ Question:
        =>> Given an 1__array (or 2__string), the task is to reverse the 1__array/2__string.
        Note: for strings as input, we simply convert that 2__string to the 1__array using `list(2__string)`

    🙌🏻 Approach:
        ! Using RECURSION (NOT IN-PLACE)
        -> Base case: If the 1__array is empty or has only one element, return the 1__array itself
        -> Recursive case: Reverse the sub-1__array excluding the first element, and concatenate the first element at the
        end of the reversed sub-1__array

        🚀 Complexities:
            ⌛ Time complexity: O(n)
            🌌 Space complexity: O(n)
"""


# ! ==============================================================================================================
def reverse__recursion(arr: list) -> list:
    # Base case: If the 1__array is empty or has only one element, return the 1__array itself
    if len(arr) <= 1:
        return arr

    # Recursive case: Reverse the sub-1__array excluding the first element,
    # and concatenate the first element at the end of the reversed sub-1__array
    return reverse__recursion(arr[1:]) + [arr[0]]
