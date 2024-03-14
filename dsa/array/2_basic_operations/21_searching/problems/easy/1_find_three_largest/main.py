"""
    ❓ Question:
        =>> Given an array with all distinct elements, find the largest three elements.

    🚀 Expected Complexities:
        ⌛ Time complexity: O(n)
        🌌 Space complexity: O(1)

    🗳️ Example:
        Input: [10, 4, 3, 50, 23, 90]
        Output: 90, 50, 23

        Input: [6, 8, 1, 9, 2, 1, 10, 10]
        Output: 10, 10, 9

    🙌🏻 Approach:
        ==> Initial 3 values `first`, `second`, and `third` with (-inf)
        ==> Iterate through the Array
            -> if arr[i] > first ==> third = second, second = first, first = arr[i]
            -> if arr[i] > second && arr[i] != first ==> third = second, second = arr[i]
            -> if arr[i] > third && arr[i] != first && arr[i] != second => third = arr[i]
        ==> Print values
====================================================================================================================================================================
"""
from math import inf


def find_top_three_largest_elements(arr: list):
    arr_len = len(arr)

    if arr_len < 3:
        print("Invalid input")

    first = second = third = float(-inf)

    for i in range(arr_len):
        iter_item = arr[i]
        if arr[i] > first:
            third = second
            second = first
            first = arr[i]

        elif arr[i] > second and arr[i] != first:
            third = second
            second = arr[i]

        elif arr[i] > third and arr[i] != second and arr[i] != first:
            third = arr[i]

    print("Three largest elements:", first, second, third)

# Example
arr = [13, 1, 40, 10, 4, 9, 7, 11, 34]
find_top_three_largest_elements(arr)
