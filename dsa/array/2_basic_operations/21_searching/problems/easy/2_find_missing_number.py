"""
    ❓ Question:
        =>> Given an array arr[] of size n-1 with integers in the range [1, n], the task is to find the missing number from the first n integers. Assume there are no duplicated in the list.

    🚀 Expected Complexities:
        ⌛ Time complexity: O(n)
        🌌 Space complexity: O(1)

    🗳️ Example:
        Input: arr[] = [1, 2, 4, 6, 3, 7, 8]
        Output: 5
        Explanation: Here the size of the array is 7, so the range will be [1, 8]. The missing number between 1 to 8 is 5
        
        Input: arr[] = [1, 2, 3, 5]
        Output: 4
        Explanation: Here the size of the array is 4, so the range will be [1, 5]. The missing number between 1 to 5 is 4

    🙌🏻 Approaches:
        =>> Approach 1: O(2n)
        - Find the sum of the range from 1 to n named `ideal_sum`. Find the sum of the arr named `actual_sum`
        - Take ideal_sum - actual_sum
        - Return the result
        
        =>> Approach 2
        - Initialize an arr [1, len(arr)] named base_range
        - Sort the input arr
        - Loop through the input arr
            -> If we found the element (has index a) in the range [0, len(arr) - 1] => return base_range[a]
            -> If we didnt find => return the last element of base_range
        
        =>> Approach 3
        

====================================================================================================================================================================
"""

# * Approach 1
def _sum(arr: list):
    # Initial a variable to hold the sum
    sum = 0

    # Loop through the list of elements and plus that element to the `sum` variable 
    for i in arr:
        sum = sum + i
    
    return sum

def find_missing_number_approach_1(arr: list):
    arr_len = len(arr)
    ideal_arr = list(range(1, arr_len + 2))
    ideal_sum = _sum(ideal_arr)

    actual_sum = _sum(arr)

    return ideal_sum - actual_sum

# * Approach 2
def find_missing_number_approach_2(arr: list):
    arr_len = len(arr)
    base_range = list(range(1, arr_len + 2))

    arr.sort()

    for idx, x in enumerate(arr):
        if arr[idx] != base_range[idx]:
            return base_range[idx]

    return base_range[-1]

# Example
arr = [1, 2, 4, 6, 3, 7, 5]
result = find_missing_number_approach_2(arr)

print(f"Missing number is {result}")