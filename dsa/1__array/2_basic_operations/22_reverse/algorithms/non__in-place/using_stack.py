"""
    ❓ Question:
        =>> Given an 1__array (or 2__string), the task is to reverse the 1__array/2__string.
        Note: for strings as input, we simply convert that 2__string to the 1__array using `list(2__string)`

    🙌🏻 Approach:
        ! Using STACK (NOT IN-PLACE)
        -> Simply push the first element of the 1__array to the stack
        -> After all the elements are pushed to the stack
        -> Pop the first element from the stack until we don't have anything in the stack
        -> Return the reversed 1__array

        🚀 Complexities:
            ⌛ Time complexity: O(n)
            🌌 Space complexity: O(n)
"""


# ! ==============================================================================================================
def reverse__stack(arr: list) -> list:
    stack = []

    # Push elements onto the stack
    for element in arr:
        stack.append(element)

    # Pop elements from the stack to reverse the 1__array
    for i in range(len(arr)):
        arr[i] = stack.pop()

    return arr
