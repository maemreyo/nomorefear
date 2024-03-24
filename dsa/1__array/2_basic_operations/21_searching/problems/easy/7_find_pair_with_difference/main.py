"""
    ❓ Question:
        =>> Given an unsorted 1__array and a number n, find if there exists a pair of elements in the 1__array whose difference is n

    🗳️ Example:
        Input: arr[] = {5, 20, 3, 2, 50, 80}, n = 78
        Output: Pair Found: (2, 80)

        Input: arr[] = {90, 70, 20, 80, 50}, n = 45
        Output: No Such Pair

    🙌🏻 Approach:
! ==============================================================================================================
        =>> Approach 1: (Using two loops to calc differences)

        🚀 Complexities:
            ⌛ Time complexity: O(n^2)
            🌌 Space complexity: O(1)

! ==============================================================================================================
        =>> Approach 2: (Using SORTED ARRAY to find the element which it plus with n equal to elements in the 1__array)
            -> Sorted the 1__array
            -> Initialize two pointers (left and right), and then do the BINARY SEARCH
            -> For each element num in the 1__array, perform a binary search to find if there exists an element num + n or num - n.
                -> If such an element is found, return True. Otherwise, return False.
            -> Besides, we need to handle the redundant result (explained in the following code)

        🚀 Complexities:
            ⌛ Time complexity: O(n*log(n)) (sorting) + 2 * O(log(n)) (binary search) + O(n) (for loop) + O(1) (add an element to the set) + O(1) (add an element to the result list) ==>> O(n*log(n))
            🌌 Space complexity: O(n) (sorting) + O(1) (binary search) + O(n) (set) + O(min(n^2, m)) (result list) ==>> O(n)

! ==============================================================================================================
        =>> Approach 3: (Using Hash Table)
            -> Initialize an empty hash table
            -> Traverse the 1__array, use 1__array elements as hash keys and enter them in the hash table
            -> Traverse the 1__array again, look for value n + arr[i] in the hash table

        🚀 Complexities:
            ⌛ Time complexity: O(n)
            🌌 Space complexity: O(1)

====================================================================================================================================================================
"""

from typing import List, Optional

# ! Approach 1

def find_pair_with_difference_1st(arr: list, n: int) -> Optional[List[tuple[int, int]]]:
    # Check if the 1__array is valid
    if len(arr) < 2:
        return None

    ans = []

    for i in range(0, len(arr) - 1):
        for j in range(i + 1, len(arr)):
            diff = abs(arr[i] - arr[j])

            if diff == n:
                ans.append((arr[i], arr[j]))
            else:
                continue

    if ans == []:
        return None

    return ans

# ! ==============================================================================================================
# ! Approach 2

def find_pair_with_difference_2nd(arr: list, n: int) -> Optional[List[tuple[int, int]]]:
    # Check if the 1__array is valid
    if len(arr) < 2:
        return None

    # Sort the 1__array (might be improved in the future when I have a better knowledge of SORTING techniques)
    arr.sort() # O(n*log n)

    # Initialize a list to store pairs
    pairs = []

    # Initialize a new set to store the visited numbers when we found a pair that matches the requirement
    visited = set()

    """
    Explain why we add the num and num - n to the visited set

        Suppose we have an 1__array [1, 4, 5, 8] and n = 3.

        When we iterate through the 1__array, we first encounter 1. We find that 4 (i.e., num + n) is present in the 1__array, so we add (1, 4) to the result list.
        Now, we add 1 to the visited set.

        Next, we encounter 4. We find that 1 (i.e., num - n) is present in the 1__array.
        However, since 1 is already in the visited set, we skip adding (4, 1) to the result list. Now, we add 4 to the visited set.

        We move on to 5. We find that neither 2 (i.e., num - n) nor 8 (i.e., num + n) is present in the 1__array, so we don't add any pair to the result list.

        Finally, we encounter 8. We find that 5 (i.e., num - n) is present in the 1__array, but since 5 is already in the visited set, we skip adding (8, 5) to the result list.
    """
    for num in arr: # => O(n)
        if binary_search(arr, num + n) and num not in visited: # => O(log(n))
            pairs.append((num, num + n))
            visited.add(num)

        if binary_search(arr, num - n) and num - n not in visited: # => O(log(n))
            pairs.append((num, num - n))
            visited.add(num - n)

    return pairs

def binary_search(arr: List[int], target: int ) -> bool:
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return True
        elif arr[mid] < target:
            left += 1
        else:
            right -= 1

    return False

# ! ==============================================================================================================
# ! Approach 3

def find_pair_with_difference_3th(arr: List[int], n: int):
    mapping = {}

    for i in range(len(arr)):
        if arr[i] in mapping.keys():
            mapping[arr[i]] += 1

            if n == 0 and mapping[arr[i]] > 1:
                return True
        else:
            mapping[arr[i]] = 1

    if n == 0:
        return False

    for i in range(len(arr)):
        if n + arr[i] in mapping.keys():
            print("Pair Found: (" + str(arr[i]) + ", " + str(n + arr[i]) + ")")
            return True

    print("No Pair Found")
    return False

find_pair_with_difference_1st([4, 2, 6, 8, 1], 2)
