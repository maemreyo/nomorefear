"""
    ❓ Question:
        =>> Given an array (or string), the task is to reverse the array/string.
        Note: for strings as input, we simply convert that string to the array using `list(string)`

    🙌🏻 Approach:
        ! Using STACK (NOT IN-PLACE)
        -> Simply push the first element of the array to the stack
        -> After all the elements are pushed to the stack
        -> Pop the first element from the stack until we don't have anything in the stack
        -> Return the reversed array

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

    # Pop elements from the stack to reverse the array
    for i in range(len(arr)):
        arr[i] = stack.pop()

    return arr
