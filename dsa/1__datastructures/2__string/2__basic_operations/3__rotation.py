"""
    |❓ PROBLEM
        =>> Rotation (Left and Right rotation)

    ! =================================================================================================================
    |🗳️ EXAMPLE
        Input : s = "GeeksforGeeks"
                d = 2
        Output : Left Rotation  : "eksforGeeksGe"
                 Right Rotation : "ksGeeksforGee"
        Input : s = "qwertyu"
                d = 2
        Output : Left rotation : "ertyuqw"
                 Right rotation : "yuqwert"

    ! =================================================================================================================
    |🙌🏻 APPROACHES
        @Approach 1:
            ! Naive Approach
            => For LEFT rotation
                -> Result = original_str[d : ] + original_str[0 : d]
            => For RIGHT rotation
                -> This is equivalent to rotate left len(str) - d times
                    -> Result = original_str[len(str) - d : ] + original_str[0 : len(str) - d]

        |🚀 COMPLEXITIES:
            ⌛ Time complexity: O(n)
            🌌 Space complexity: O(1)

        ! =============================================================================================================
        @Approach 2:
            ! Using DOUBLE STRING
            => For LEFT rotation
                -> First we double the input string
                -> Result should be equal to double_str = [d : d + len(str)]
            => For RIGHT rotation
                -> This is equivalent to rotate left len(str) - d times
                    -> left_rotation(str, len(str) - d)


        |🚀 COMPLEXITIES:
            ⌛ Time complexity: O(n)
            🌌 Space complexity: O(n)

"""

# ! ===================================================================================================================
import unittest


# ! Approach 1
def left_rotation__naive(input_str: str, d: int) -> str:
    return input_str[d:] + input_str[0:d]


def right_rotation__naive(input_str: str, d: int) -> str:
    return left_rotation__naive(input_str, len(input_str) - d)


# ! ===================================================================================================================
# ! Approach 2
def left_rotation__doubled_string(input_str: str, d: int) -> str:
    temp_str = input_str + input_str
    n = len(input_str)
    return temp_str[d:d + n]


def right_rotation__doubled_string(input_str: str, d: int) -> str:
    return left_rotation__doubled_string(input_str, len(input_str) - d)


class TestSuite(unittest.TestCase):
    def test_left_rotation__naive(self):
        input_str = "GeeksforGeeks"
        d = 2
        expected = "eksforGeeksGe"

        actual = left_rotation__naive(input_str, d)
        self.assertEqual(expected, actual)

    def test_left_rotation__doubled_string(self):
        input_str = "GeeksforGeeks"
        d = 2
        expected = "eksforGeeksGe"

        actual = left_rotation__doubled_string(input_str, d)
        self.assertEqual(expected, actual)

    def test_right_rotation__naive(self):
        input_str = "GeeksforGeeks"
        d = 2
        expected = "ksGeeksforGee"

        actual = right_rotation__naive(input_str, d)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
