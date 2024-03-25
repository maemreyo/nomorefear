"""
    |❓ PROBLEM
        =>> Swap characters in a String
        Given a String S of length N, two integers B and C, the task is to traverse characters starting from the beginning, swapping a character with the character after C places from it
        Swap characters at position i and (i + C)%N. Repeat this process B times, advancing one position at a time. Your task is to find the final String after B swaps.

    ! =================================================================================================================
    |🗳️ EXAMPLE
        Input : S = "ABCDEFGH", B = 4, C = 3;
        Output:  DEFGBCAH
        Explanation:
                 after 1st swap: DBCAEFGH i = 0, C = 3, N = 8 => A <=> D
                 after 2nd swap: DECABFGH i = 1, C = 3, N = 8 => B <=> E
                 after 3rd swap: DEFABCGH i = 2, C = 3, N = 8 => C <=> F
                 after 4th swap: DEFGBCAH i = 3, C = 3, N = 8 => A <=> G

        Input : S = "ABCDE", B = 10, C = 6;
        Output : ADEBC
        Explanation:
                 after 1st swap: BACDE
                 after 2nd swap: BCADE
                 after 3rd swap: BCDAE
                 after 4th swap: BCDEA
                 after 5th swap: ACDEB
                 after 6th swap: CADEB
                 after 7th swap: CDAEB
                 after 8th swap: CDEAB
                 after 9th swap: CDEBA
                 after 10th swap: ADEBC

    ! =================================================================================================================
    |🙌🏻 APPROACHES
        @Approach 1:
            ! Using Naive Approach
            -> Loop B times
                -> Modulo C to N: C = C % N
                -> Find i and (i + C)%N elements
                -> Swap them


        |🚀 COMPLEXITIES:
            ⌛ Time complexity: O(B)
            🌌 Space complexity: O(1)

"""
import unittest


# ! ===================================================================================================================
# ! Approach 1
def swap_chars(s, B, C):
    N = len(s)
    C = C % N
    s = list(s)

    for i in range(B):
        s[i], s[(i + C) % N] = s[(i + C) % N], s[i]

    return ''.join(s)


class TestSuite(unittest.TestCase):
    def test_swap_chars__naive_approach(self):
        s = "ABCDEFGH"
        B = 4
        C = 3

        expected = "DEFGBCAH"

        self.assertEqual(expected, swap_chars(s, B, C))


if __name__ == "__main__":
    unittest.main()
