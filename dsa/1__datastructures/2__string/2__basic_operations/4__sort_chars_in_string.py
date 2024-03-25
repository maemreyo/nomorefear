"""
    |❓ PROBLEM
        =>> Given a string of lowercase characters from ‘a’ – ‘z’. We need to write a program to print the characters of this string in sorted order.

    ! =================================================================================================================
    |🗳️ EXAMPLE
        Input : bbccdefbbaa
        Output : aabbbbccdef
        Input : geeksforgeeks
        Output : eeeefggkkorss

    ! =================================================================================================================
    |🙌🏻 APPROACHES
        @Approach 1:
            ! Using BUILT-IN METHOD

        |🚀 COMPLEXITIES:
            ⌛ Time complexity: O(N*log(N))
            🌌 Space complexity: O(1)

        ! =============================================================================================================
        @Approach 2:
            ! Using HASHING
            -> Initialize a new hashing map to count the occurrences of each characters in the input string
            -> Loop through the input string and count the occurrences of each character
            -> Loop through the alphabet characters (a -> z) and print the sorted string

        |🚀 COMPLEXITIES:
            ⌛ Time complexity: O(N)
            🌌 Space complexity: O(1)

"""
import unittest


# ! ===================================================================================================================
# ! Approach 1
def sort_alphabet_string__builtin_method(input_string: str) -> str:
    input_string = ''.join(sorted(input_string))
    return input_string


# ! Approach 2
def sort_alphabet_string__hashing(input_string: str) -> str:
    # Initialize a new hash map
    char_count = {}

    # Count the occurrences of characters in the input string
    for char in input_string:
        char_count[char] = char_count.get(char, 0) + 1

    # Print the sorted string
    sorted_string = ''
    for char in 'abcdefghijklmnopqrstuvwxyz':
        if char in char_count:
            sorted_string += char * char_count[char]

    return sorted_string


class TestSuite(unittest.TestCase):
    def test_sort_alphabet__builtin_methods(self):
        input = "bbccdefbbaa"

        expected = "aabbbbccdef"
        actual = sort_alphabet_string__builtin_method(input)

        self.assertEqual(expected, actual)

    def test_sort_alphabet__hashing(self):
        input = "bbccdefbbaa"

        expected = "aabbbbccdef"
        actual = sort_alphabet_string__hashing(input)

        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
