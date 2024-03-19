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
        * Approach 1
            ! Naive Approach
            -> Loop through an array
            -> For each element, check if it is in two remaining arrays

        🚀 Complexities:
            ⌛ Time complexity: O(n1 * (n2 + n3)
            🌌 Space complexity: O(min(n1, n2, n3))

        ! ==============================================================================================================
        * Approach 2
            ! Finding the intersection of two arrays
            -> Initialize two pointers to point to two first arrays
            -> While both two pointers didnt reach the last element
                >-> If arr1[i] is less than arr2[j], increment i by 1.
                >-> If arr2[j] is less than arr1[i], increment j by 1.
                >-> If arr1[i] is equal to arr2[j]:
                >-> Add arr1[i] to the common list.
                >-> Increment both i and j by 1.
            -> Return the common list containing the common elements of the two arrays.

        🚀 Complexities:
            ⌛ Time complexity: 0(min(n, m) + min(min(n, m), k))
            🌌 Space complexity: O(min(min(n, m), k))
"""


# ! ==============================================================================================================
# ! Approach 1
def find_common_in_sorted_arrays__naive(arr1: list[int], arr2: list[int], arr3: list[int]) -> list[int]:
    # Check if arrays are valid
    if len(arr1) == 0 or len(arr2) == 0 or len(arr3) == 0:
        return []

    ans = []

    # Check if the element in arr1 is in both the remaining arrays or not
    for i in range(len(arr1)):  # * O(n1 * (n2 + n3)
        if arr1[i] in arr2 and arr1[i] in arr3:
            ans.append(arr1[i])

    return ans


# ! Approach 2
def find_common_in_sorted_arrays__intersection_pair(arr1: list[int], arr2: list[int], arr3: list[int]) -> list[int]:
    n = len(arr1)
    m = len(arr2)
    k = len(arr3)

    # Check if arrays are valid
    if n == 0 or m == 0 or k == 0:
        return []

    temp = find_intersection(arr1, arr2)  # * 0(min(n, m))
    return find_intersection(temp, arr3)  # * 0(min(min(n, m), k))


def find_intersection(arr1: list[int], arr2: list[int]) -> list[int]:
    i, j = 0, 0
    ans = []

    n = len(arr1)
    m = len(arr2)

    while i < n and j < m:  # * 0(min(n, m))
        if arr1[i] < arr2[j]:
            i += 1
        elif arr2[j] < arr1[i]:
            j += 1
        else:
            ans.append(arr1[i])
            i += 1
            j += 1

    return ans
