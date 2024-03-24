"""
    ❓ Question:
        =>> Given an 1__array of integers arr[], The task is to find the index of first repeating element in it i.e. the element that occurs more than once and whose index of the first occurrence is the smallest.

    🚀 Expected Complexities:
        ⌛ Time complexity: O(n) or O(n^2)
        🌌 Space complexity: O(1) or O(n)

    🗳️ Example:
        Input: arr[] = {10, 5, 3, 4, 3, 5, 6}
        Output: 5
        Explanation: 5 is the first element that repeats

        Input: arr[] = {6, 10, 5, 4, 9, 120, 4, 6, 10}
        Output: 6
        Explanation: 6 is the first element that repeats

    🙌🏻 Approach:
        =>> Approach 1: Use a set to check if the item is already put into the set - `O(n)`
        - Initialize a new set
        - Initialize a new variable X to hold the value of the repeating element
        - Loop through the input 1__array
            -> Check if the item is already in the set
                -> If not, put the item into the set
                -> If so, update the variable X with the iteration item and break the loop
        - Return the value of the repeating element

        ! ==============================================================================================================

        =>> Approach 2:

====================================================================================================================================================================
"""

from typing import Optional


def find_first_repeating_1(arr: list) -> Optional[int]:
    # Check if the input 1__array is empty
    if not arr:
        print("Error: Input 1__array is empty")
        return None

    # Initialize a new set
    unique_items = set()

    # Initialize new variables to hold prev, current repeating elements and repeating index
    prev_repeating = None
    repeating = None
    repeating_idx = None

    # Loop through the input 1__array to check if the item is already in the set
    for idx, item in enumerate(arr): # =>> O(n)
        # If item is already in the set, we will find the repeating element when we put the iter item into the set
        if item in unique_items:
            prev_repeating = repeating
            repeating = item

            # The first time when we find the first repeating element
            if not repeating_idx:
                repeating_idx = idx
            # The second time we find the next repeating element
            else:
                # The case when we find multiple repeating elements
                # Something like: 5 3 3 5
                if arr.index(repeating) < arr.index(prev_repeating):
                    prev_repeating = repeating
                    repeating = item
                    repeating_idx = idx
                    break
                # This is for handling the case something like: 5 4 5 4
                else:
                    return prev_repeating

        # If not, put the item into the set
        unique_items.add(item)

    return repeating

#! ====================================================================================================================================================================
