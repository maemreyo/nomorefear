"""
    |❓ PROBLEM
        =>> Reverse a string

    ! =================================================================================================================
    |🗳️ EXAMPLE
        Input: original_string[] = Geeks
        Output: string_reversed[] = skeeG

        Input: original_string[] = GeeksForGeeks
        Output: string_reversed[] = skeeGroFskeeG

    ! =================================================================================================================
    |🙌🏻 APPROACHES
        @Approach 1:
            ! Using LOOP
            -> Initialize an empty string
            -> Loop through the input string from the end
                -> Concat each character to the empty string

        |🚀 COMPLEXITIES:
            ⌛ Time complexity: O(n)
            🌌 Space complexity: O(n)

        ! =============================================================================================================
        @Approach 2:
            ! Using BUILTIN method
            -> Using method like: reverse()

        |🚀 COMPLEXITIES:
            ⌛ Time complexity: O(n)
            🌌 Space complexity: O(1), or can be O(n) if the programming language requires the StringBuffer

        ! =============================================================================================================
        @Approach 3:
            ! Using RECURSION
            -> Base case: if the pointer i > len(str) // 2, we return
            -> We recursive call the reverse function
                -> Swap two chars at i and n - i - 1
                -> Call the reverse function with i + 1

        |🚀 COMPLEXITIES:
            ⌛ Time complexity: O(n)
            🌌 Space complexity: O(n)

        ! =============================================================================================================
        @Approach 4:
            ! Using TWO POINTERS
            -> Initialize two pointers at left-most and right-most of the string
            -> While left < right
                -> Swap two chars at two pointers repeatedly
                -> Increase left pointer and decrease right pointer



        |🚀 COMPLEXITIES:
            ⌛ Time complexity: O(n)
            🌌 Space complexity: O(1)

        ! =============================================================================================================
        @Approach 5:
            ! Using STACK
            -> Initialize a stack and an empty result string
            -> Loop through the input string
                -> Push each character to the stack
            -> Loop through the stack
                -> Concat each char at the top of stack to the result string

        |🚀 COMPLEXITIES:
            ⌛ Time complexity: O(n)
            🌌 Space complexity: O(n)

"""
# ! ===================================================================================================================
