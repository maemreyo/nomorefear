"""
    ❓ Question:
        =>> Given an unsorted array of size n. Array elements are in the range of 1 to n. One number from set {1, 2, …n} is missing and one number occurs twice in the array. Find these two numbers.

    🚀 Expected Complexities:
        ⌛ Time complexity: O(n)
        🌌 Space complexity: O(1)

    🗳️ Example:
            Input: arr[] = {3, 1, 3}
            Output: Missing = 2, Repeating = 3
            Explanation: In the array, 2 is missing and 3 occurs twice 

            Input: arr[] = {4, 3, 6, 2, 1, 1}
            Output: Missing = 5, Repeating = 1

    🙌🏻 Approaches:
        =>> Approach 1: Using count array - `O(4n) -> O(n)`
        - Create a new array that contains full of 0 and have the length n
        - Loop through the input array
            -> If base_arr[arr[i] - 1] == 0 => base_arr[arr[i] - 1] += 1
            -> If base_arr[arr[i] - 1] == 1 => base_arr[arr[i] - 1] += 1
        - If arr[i] == 0 => The missing one
        - If arr[i] == 2 => The repeating one

        ! ==============================================================================================================
        =>> Approach 2: Using a set - `O(2n) -> O(n)`
        - Create a new set
        - Initialize a variable X to store the repeating variable
        - Loop through the input array
            -> Check if the iter-item is already in the set
                -> If so, update the X to that iter-item
                -> If not, add that iter-item to the set
        - We will take advantage of the previous iteration to know what the input array contains
        - Initialize the variable Y to store the missing variable
        - Loop through the base array that is the range from [1, len(arr) + 1]
            -> Check if the iter-item is not contained in the unique array

====================================================================================================================================================================
"""

from typing import Optional


def find_missing_repeating_1(arr: list) -> Optional[tuple[int, int]]:
    # Check if the input array is empty
    if not arr:
        print("Error: Input array is empty")
        return None

    # Create a new array that contains full of 0 and have the length n
    base_arr = [0] * (len(arr)) # n

    # Loop through the input array to count
    for i in arr: # n
        if base_arr[i - 1] == 0:
            base_arr[i - 1] += 1
            continue

        if base_arr[i - 1] == 1:
            base_arr[i - 1] += 1

    # Find the missing and repeating elements
    missing = None
    repeating = None

    # Filter the missing and repeating ones
    for idx, i in enumerate(base_arr): # n
        if i == 0:
            missing = idx + 1
            break

    for idx, i in enumerate(base_arr): # n
        if i == 2:
            repeating = idx + 1
            break

    # Check if missing or repeating elements were found
    if missing is None or repeating is None:
        print("Error: Missing or repeating element not found")
        return None

    return missing, repeating

#! ====================================================================================================================================================================
def find_missing_repeating_2(arr: list) -> Optional[tuple[int, int]]:
    # Check if the input array is empty
    if not arr:
        print("Error: Input array is empty")
        return None
    
    # Initialize the unique array that contains unique items
    unique_arr = set()
    
    # Initialize the repeating variable
    repeating = None
    
    # Loop through the input array
    for item in arr: # n
        if item in unique_arr:
            repeating = item
            break
        
        unique_arr.add(item)
    
    # We will take advantage of the previous iteration to know what the input array contains
    # Initialize the variable Y to store the missing variable
    missing = None
    
    # Loop through the base array and find the missing item
    for item in range(1, len(arr) + 1): # n
        if item not in unique_arr:
            missing = item
            break
    
    # Check if missing or repeating elements were found
    if missing is None or repeating is None:
        print("Error: Missing or repeating element not found")
        return None
    
    return missing, repeating

#! ====================================================================================================================================================================

# Example
arr = [3, 1, 3]
result = find_missing_repeating_2(arr)

if result:
    print(result)
else:
    print("Function returned None due to error")
