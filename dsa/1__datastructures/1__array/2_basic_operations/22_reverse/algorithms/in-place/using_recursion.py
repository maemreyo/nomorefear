"""
    ❓ Question:
        =>> Given an 1__array (or 2__string), the task is to reverse the 1__array/2__string.
        Note: for strings as input, we simply convert that 2__string to the 1__array using `list(2__string)`

    🙌🏻 Approach:
        ! Using RECURSION (IN-PLACE)
        -> If two pointers didnt meet each other
        -> Swap elements at start and end pointers
        -> Keep calling the reverse function with the input 1__array and forwarded pointers

        🚀 Complexities:
            ⌛ Time complexity: O(n)
            🌌 Space complexity: O(1)
"""


# ! ==============================================================================================================
def reverse__recursion(arr: list, start: int, end: int):
    # If two pointers meet each other, then we need to stop processing
    if start >= end:
        return

    # Swap elements at start and end pointers
    arr[start], arr[end] = arr[end], arr[start]

    # Recursively call the reverse function
    reverse__recursion(arr, start + 1, end - 1)
