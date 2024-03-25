"""
    |❓ PROBLEM
        =>> How to insert characters in a string at a certain position
        Given a string `s` and an array of indices `chars` that describes the indices in the original string where the characters will be added.

    ! =================================================================================================================
    |🗳️ EXAMPLE
        Input: str = “geeksforgeeks”, chars = [1, 5, 7, 9]
        Output: g*eeks*fo*rg*eeks
        Explanation: The indices 1, 5, 7, and 9 correspond to the bold characters in “geeksforgeeks”.

        Input: str = “spacing”, chars = [0, 1, 2, 3, 4, 5, 6]
        Output: “*s*p*a*c*i*n*g”

    ! =================================================================================================================
    |🙌🏻 APPROACHES
        @Approach 1:
            ! Naive Approach
            -> Initialize a new string to store the result named `ans`
            -> Loop through the range r = len(s)
            -> If i == chars[j]
                -> If so ans += '*' and j += 1
                -> If not, ans += s[i]
            -> Return the result



        |🚀 COMPLEXITIES:
            ⌛ Time complexity: O(N)
            🌌 Space complexity: O(N)

        ! =============================================================================================================
        @Approach 2:
            ! Using HANDLING SUB-STRING
            -> Initialize a variable to track how many units that the string is already increased when adding a char `*` into
            -> Loop through the characters array
                -> s = s[:stars[i] + k] + '*' + s[stars[i] + k:]
                -> Then increase k by 1 because we insert a char to the string
            -> Return the result


        |🚀 COMPLEXITIES:
            ⌛ Time complexity: O(N*K) (insert into a string take O(N))
            🌌 Space complexity: O(1)

"""

import unittest


# ! ===================================================================================================================

# ! Approach 1
def insert_chars__naive_approach(s: str, chars: list[int]) -> str:
    ans = ''
    j = 0

    for i in range(len(s)):
        if j < len(chars) and i == chars[j]:
            ans += '*'
            j += 1

        ans += s[i]

    return ans


def insert_chars__sub_strings(s: str, chars: list[int]) -> str:
    c = 0

    for i in range(len(chars)):
        s = s[:chars[i] + c] + '*' + s[chars[i] + c:]
        c += 1

    return s


class MyTestCase(unittest.TestCase):
    def test_insert_chars__naive_approach(self):
        s = "geeksforgeeks"
        chars = [1, 5, 7, 9]

        expected = "g*eeks*fo*rg*eeks"
        actual = insert_chars__naive_approach(s, chars)
        self.assertEqual(expected, actual)

    def test_insert_chars__sub_string(self):
        s = "geeksforgeeks"
        chars = [1, 5, 7, 9]

        expected = "g*eeks*fo*rg*eeks"
        actual = insert_chars__sub_strings(s, chars)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
