"""
    |❓ PROBLEM
        =>> Given a string str, the task is to print the frequency of each of the characters of str in alphabetical order.

    ! =================================================================================================================
    |🗳️ EXAMPLE
        Input: str = “aabccccddd”
        Output: a2b1c4d3
        Since it is already in alphabetical order, the frequency
        of the characters is returned for each character.
        Input: str = “geeksforgeeks”
        Output: e4f1g2k2o1r1s2

    ! =================================================================================================================
    |🙌🏻 APPROACHES
        @Approach 1:
            ! Using HASHING
            -> Initialize a new hash map
            -> Loop through the input string to count the occurrences of each characters
            -> Loop through string from a to z and print the result


        |🚀 COMPLEXITIES:
            ⌛ Time complexity: O(N)
            🌌 Space complexity: O(1)

"""


# ! ===================================================================================================================
# ! Approach 1
def print_frequency_in_alphabetical_order__hashing(input_str: str):
    # Initialize a dictionary to count occurrences of each character
    char_count = {}

    # Count occurrences of each character in the input string
    for char in input_str:
        char_count[char] = char_count.get(char, 0) + 1

    # Iterate through the alphabet characters ('a' to 'z') and print their frequencies
    for char in 'abcdefghijklmnopqrstuvwxyz':
        if char in char_count:
            print(f"{char}: {char_count[char]}")
