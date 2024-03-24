"""
    ❓ Question:
        =>> Given an 1__array (or 2__string), the task is to reverse the 1__array/2__string.
        Note: for strings as input, we simply convert that 2__string to the 1__array using `list(2__string)`

    🙌🏻 Approach:
        ! Using BUILT-IN METHOD (NOT IN-PLACE)

        🚀 Complexities:
            ⌛ Time complexity: O(n)
            🌌 Space complexity: O(n)
"""


# ! ==============================================================================================================
def reverse__builtin(arr: list) -> list:
    return list(reversed(arr))
