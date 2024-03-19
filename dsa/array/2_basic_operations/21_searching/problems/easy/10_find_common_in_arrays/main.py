"""
    ❓ Question:
        =>> Given three Sorted arrays in non-decreasing order, print all common elements in these arrays.

    🗳️ Example:
        Input:
            ar1[] = {1, 5, 10, 20, 40, 80}
            ar2[] = {6, 7, 20, 80, 100}
            ar3[] = {3, 4, 15, 20, 30, 70, 80, 120}
        Output: 20, 80

        Input:
            ar1[] = {1, 5, 5}
            ar2[] = {3, 4, 5, 5, 10}
            ar3[] = {5, 5, 10, 20}
        Output: 5, 5

    🙌🏻 Approach:
        ! ==============================================================================================================
        =>> Approach 1:
            ! Naive Approach
            -> Loop through an array
            -> For each element, check if it is in two remaining arrays


        🚀 Complexities:
            ⌛ Time complexity: O()
            🌌 Space complexity: O()

        ! ==============================================================================================================

        =>> Approach 2:
            ! Using


        🚀 Complexities:
            ⌛ Time complexity: O()
            🌌 Space complexity: O()
"""


# ! ==============================================================================================================
# ! Approach 1
def find_common_in_sorted_arrays__naive(arr1: list[int], arr2: list[int], arr3: list[int]) -> list[int]:
    ans = []

    # Check if arrays are valid
    if len(arr1) == 0 or len(arr2) == 0 or len(arr3) == 0:
        return []
    # Check if the element in arr1 is in both the remaining arrays or not
    for i in range(len(arr1)):
        if arr1[i] in arr2 and arr1[i] in arr3:
            ans.append(arr1[i])

    return ans
