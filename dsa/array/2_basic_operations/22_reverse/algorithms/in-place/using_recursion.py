"""
    ❓ Question:
        =>> Given an array (or string), the task is to reverse the array/string.
        Note: for strings as input, we simply convert that string to the array using `list(string)`

    🙌🏻 Approach:
        ! Using RECURSION (IN-PLACE)
        -> If two pointers didnt meet each other
        -> Swap elements at start and end pointers
        -> Keep calling the reverse function with the input array and forwarded pointers

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
