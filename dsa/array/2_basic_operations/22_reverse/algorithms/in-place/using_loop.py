"""
    ❓ Question:
        =>> Given an array (or string), the task is to reverse the array/string.
        Note: for strings as input, we simply convert that string to the array using `list(string)`

    🙌🏻 Approach:
        ! Using LOOP (IN_PLACE)
        -> Initialize two pointers at start and end of the array
        -> Loop through the array
            >-> Swap elements at start and end pointers
            >-> Move pointers forward
        -> If pointers meet or cross each other, we stop processing
        -> Return the reversed array

        🚀 Complexities:
            ⌛ Time complexity: O(n)
            🌌 Space complexity: O(1)
"""


# ! ==============================================================================================================
def reverse__loop(arr: list) -> list:
    # Initialize two pointers at start and end of the array
    left, right = 0, len(arr) - 1

    # Loop through the array while two pointers didnt meet each other
    while left < right:
        # Swap elements at start and end pointers
        arr[left], arr[right] = arr[right], arr[left]

        # Move pointers forward
        left += 1
        right -= 1

    return arr
