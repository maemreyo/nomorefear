"""
    ❓ Question:
        =>> Given an array (or string), the task is to reverse the array/string.
        Note: for strings as input, we simply convert that string to the array using `list(string)`

    🙌🏻 Approach:
        ! Using BUILT-IN METHOD (NOT IN-PLACE)

        🚀 Complexities:
            ⌛ Time complexity: O(n)
            🌌 Space complexity: O(n)
"""


# ! ==============================================================================================================
def reverse__builtin(arr: list) -> list:
    return list(reversed(arr))
