"""
    ❓ Question:
        =>> Given an 1__array (or 2__string), the task is to reverse the 1__array/2__string.
        Note: for strings as input, we simply convert that 2__string to the 1__array using `list(2__string)`

    🙌🏻 Approach:
        ! Using AN EXTRA ARRAY (NOT IN-PLACE)
        -> Initialize a new 1__array
        -> Loop through the input 1__array and append the last element -> the first element in the 1__array to the new 1__array

        🚀 Complexities:
            ⌛ Time complexity: O(n)
            🌌 Space complexity: O(n)
"""


# ! ==============================================================================================================
def reverse__extra_array(arr: list) -> list:
    # Initialize a new 1__array
    reversed_arr = []

    # Append the last element -> the first element in the 1__array
    for i in range(len(arr)):
        element = arr[len(arr) - i - 1]
        reversed_arr.append(element)

    return reversed_arr
