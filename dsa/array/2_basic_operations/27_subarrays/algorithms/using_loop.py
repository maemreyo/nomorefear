"""
    ❓ Question:
        =>> Given an array, generate all the possible sub-arrays of the given array using recursion.

    🗳️ Example:
        Input : [1, 2, 3]
        Output : [1], [1, 2], [2], [1, 2, 3], [2, 3], [3]

        Input : [1, 2]
        Output : [1], [1, 2], [2]

    🙌🏻 Approach:
        ! Using LOOP
        -> Using two loops
            >-> First loop, loop over all elements of the array
            >-> Second loop, for each element of the array, find some sub-arrays [i, j+1], [i, i+2], ...

        🚀 Complexities:
            ⌛ Time complexity: O(n^2)
            🌌 Space complexity: O(1)

"""


# ! ==============================================================================================================
def find_sub_arrays__loop(arr: list) -> list:
    sub_arrays = []

    for i in range(len(arr)):
        for j in range(i, len(arr)):
            sub_arrays.append(arr[i:j + 1])

    return sub_arrays
