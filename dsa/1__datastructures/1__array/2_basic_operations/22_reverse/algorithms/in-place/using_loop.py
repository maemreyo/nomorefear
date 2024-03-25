"""
    ❓ Question:
        =>> Given an 1__array (or 2__string), the task is to reverse the 1__array/2__string.
        Note: for strings as input, we simply convert that 2__string to the 1__array using `list(2__string)`

    🙌🏻 Approach:
        ! Using LOOP (IN_PLACE)
        -> Initialize two pointers at start and end of the 1__array
        -> Loop through the 1__array
            >-> Swap elements at start and end pointers
            >-> Move pointers forward
        -> If pointers meet or cross each other, we stop processing
        -> Return the reversed 1__array

        🚀 Complexities:
            ⌛ Time complexity: O(n)
            🌌 Space complexity: O(1)
"""


# ! ==============================================================================================================
def reverse__loop(arr: list) -> list:
    # Initialize two pointers at start and end of the 1__array
    left, right = 0, len(arr) - 1

    # Loop through the 1__array while two pointers didnt meet each other
    while left < right:
        # Swap elements at start and end pointers
        arr[left], arr[right] = arr[right], arr[left]

        # Move pointers forward
        left += 1
        right -= 1
