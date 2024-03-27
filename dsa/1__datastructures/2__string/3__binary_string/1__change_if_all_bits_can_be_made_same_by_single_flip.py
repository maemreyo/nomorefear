"""
    |❓ PROBLEM
        =>> Check if all bits can be made same by single flip
        Given a binary string, find if it is possible to make all its digits equal (either all 0's or all 1's) by flipping exactly one bit.

    ! =================================================================================================================
    |🗳️ EXAMPLE
        Input: 101
        Output: Yes
        Explanation: In 101, the 0 can be flipped to make it all 1

        Input: 11
        Output: No
        Explanation: No matter whichever digit you flip, you will not get the desired string.

        Input: 1
        Output: Yes
        Explanation: We can flip 1, to make all 0’s

    ! =================================================================================================================
    |🙌🏻 APPROACHES
        @Approach 1:
            ! Using COUNTING 0s and 1s
            => If a digits of a string can be made identical by doing exactly one flip, that means the string has all its digits equal to one another except this digit which has to be flipped.
            => This digit must be different than all other digits of the string.
            => Therefore, we only need to check whether the string has exactly one digit equal to zero/one digit.

        |🚀 COMPLEXITIES:
            ⌛ Time complexity: O()
            🌌 Space complexity: O()

"""

import unittest


# ! ===================================================================================================================
def flip_a_bit(bits: str) -> bool:
    zero_count = 0
    one_count = 0

    for i in range(len(bits)):
        if bits[i] == '0':
            zero_count += 1
        else:
            one_count += 1

    return zero_count == 1 or one_count == 1


class MyTestCase(unittest.TestCase):
    def test_flip_a_bit(self):
        input_str = '101'
        expected = True

        self.assertEqual(flip_a_bit(input_str), expected)


if __name__ == '__main__':
    unittest.main()
