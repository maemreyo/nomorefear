"""
    ❓ Question:
        =>> Given an array (or string), the task is to reverse the array/string.
        Note: for strings as input, we simply convert that string to the array using `list(string)`

    🙌🏻 Approach:
        ! Using AN EXTRA ARRAY (NOT IN-PLACE)
        -> Initialize a new array
        -> Loop through the input array and append the last element -> the first element in the array to the new array

        🚀 Complexities:
            ⌛ Time complexity: O(n)
            🌌 Space complexity: O(n)
"""


# ! ==============================================================================================================
def reverse__extra_array(arr: list) -> list:
    # Initialize a new array
    reversed_arr = []

    # Append the last element -> the first element in the array
    for i in range(len(arr)):
        element = arr[len(arr) - i - 1]
        reversed_arr.append(element)

    return reversed_arr
