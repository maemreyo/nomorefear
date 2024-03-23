"""
    ❓ Question:
        =>> Given an array, generate all the possible sub-arrays of the given array using recursion.

    🗳️ Example:
        Input : [1, 2, 3]
        Output : [1], [1, 2], [2], [1, 2, 3], [2, 3], [3]

        Input : [1, 2]
        Output : [1], [1, 2], [2]

    🙌🏻 Approach:
        ! Using RECURSION
        -> Initialize two pointers start and end
        -> If end == len(arr), we stop recursion
        -> If start > end, we recursively call the generator with start = 0 and end + 1
        -> If start <= end, we append the sub-arrays from arr[start:end + 1]
            >-> and recursively call the generator with start = start + 1 and end = end

        🚀 Complexities:
            ⌛ Time complexity: O()
            🌌 Space complexity: O()

"""


# ! ==============================================================================================================
def find_sub_arrays__recursion(arr: list) -> list:
    sub_arrays = []

    def generator(start: int, end: int):
        # Base case: Stop if we have reached the end of the array
        if end == len(arr):
            return

        # If start index exceeds end index, move and index forward by 1
        elif start > end:
            return generator(0, end + 1)

        # Print the sub-arrays from start to end and move start index forward by 1
        else:
            sub_arrays.append(arr[start: end + 1])
            return generator(start + 1, end)

    generator(0, 0)

    return sub_arrays
