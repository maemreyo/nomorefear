"""
    |❓ PROBLEM
        =>> Program to check if two strings are same or not
        Given two strings, the task is to check if these two strings are identical(same) or not.



    ! =================================================================================================================
    |🗳️ EXAMPLE
        Input: string1 = “GeeksforGeeks”, string2 = “GeeksforGeeks”
        Output: Yes
        Input: string1 = “Geeks for Geeks”, string2 = “Geeks for Geeks”
        Output: Yes
        Input: string1 = “GeeksforGeeks”, string2 = “Geeks”
        Output: No
        Input: string1 = “Geeks for Geeks”, string2 = “Geeks for geeks”
        Output: No

    ! =================================================================================================================
    |🙌🏻 APPROACHES
        @Approach 1:
            ! Using BRUTE FORCE
            -> Using some operators like: is (in Python), == (in Javascript)
            -> Using some not equal operators

        ! =============================================================================================================
        @Approach 2:
            ! Using TWO POINTERS
            -> Check if the length of two strings is equal or not
            -> If equal, we start using two pointers
                -> Increase two pointers by 1
                -> Check elements at each positions
                    -> If not equal -> return false
                    -> If two pointers reached to the end of each string -> return true


        |🚀 COMPLEXITIES:
            ⌛ Time complexity: O(N)
            🌌 Space complexity: O(1)

"""
# ! ===================================================================================================================
