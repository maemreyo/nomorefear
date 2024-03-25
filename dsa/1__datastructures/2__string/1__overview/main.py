"""
    |〽️ STRING

    ! =================================================================================================================
    |🔎 GENERAL
    In most programming languages, strings are treated as a distinct data type. This means that strings have their own set of operations and properties. They can be declared and manipulated using
    specific string-related functions and methods
    >> What is String?
    Strings are considered a data type in general and are typically represented as arrays of bytes (or words) that store a sequence of characters. Strings are defined as an array of characters. The
    difference between a character array and a string is the string is terminated with a special character ‘\0’

    >> String Operations and Special Strings
    String support a wide range of operations, including concatenation, substring extraction, length calculation, and more.
    These operations allow developers to manipulate and process string data efficiently.
    @Concatenation
    => Combining two strings to create a new string

    @Length
    => Determining the number of characters in a string

    @Access
    => Accessing individual characters in a string by index

    @Substring
    => Extracting a portion of a string

    @Comparison
    => Comparing two strings to check for equality or order

    @Search
    => Finding the position of a specific substring within a string

    @Modification
    => Changing or replacing characters within a string
        -> Reverse
        -> Rotation
        -> Trim

    @Binary String
    -> A special kind of string made up of only two types of characters (0, 1)

    @Palindrome String
    -> A string is said to be a palindrome if the reverse of the string is the same as the string

    @Lexicographic Patterns
    -> Lexicographic patterns is the pattern based on the ASCII value or can be said in dictionary order.
    -> We consider the lexicographic order of characters as their order of ASCII value. Hence the lexicographical order of characters will be.
        -> ‘A’, ‘B’, ‘C’, …, ‘Y’, ‘Z’, ‘a’, ‘b’, ‘c’, …, ‘y’, ‘z’

    >> Applications
    => Plagiarism Checker
        -> Strings can be used to find Plagiarism in codes, and contents in a very little amount of time using string matching algorithms.
        -> Using this computer could easily tell us the percentage of code, and text written by any two users matches by how much percent.
    => Encoding/Decoding (Cipher Text Generation)
        -> Strings can be used for encoding and decoding for the safe transfer of data from sender to receiver to make sure no one in the way of transmission gets to read your data.
        -> The text you transfer as a message gets ciphered at the sender's end and decoded at the receiver's end.
    => Information Retrieval
        -> Help us to retrieve information from unknown data sources( large datasets used as input) along with the help of string matching/retrieval module helps us to retrieve important information.
    => Improved Filters For The Approximate Suffix-Prefix Overlap Problem
        -> Strings and its algorithms applications help us to provide improved Filters for the Approximate Suffix-Prefix Overlap Problem.
        -> The approximate suffix-prefix overlap problem is to find all pairs of strings from a given set such that a prefix of one string is similar to a suffix of the other.
    => Network communication
        -> Strings are used to encode and decode data sent over networks, such as HTTP requests and responses.
    => File handling
        -> Strings are used to manipulate file paths and names, and to read and write files.
    => Data analysis
        -> Strings can be used to extract meaningful insights from large amounts of text data, such as natural language processing and sentiment analysis.

    >> Advantages
    => Text Processing
        -> Strings are used to represent text in programming languages.
        -> They can be used to manipulate and process text in various ways, such as searching, replacing, parsing, and formatting.
    => Data Representation
        -> Strings can be used to represent other data types, such as numbers, dates, and times.
        -> For example, you can use a string to represent a date in the format “YYYY-MM-DD”, or a time in the format “HH:MM:SS”.
    => Ease of Use
        -> Strings are easy to use and manipulate. They can be concatenated, sliced, and reversed, among other things.
        -> They also have a simple and intuitive syntax, making them accessible to programmers of all skill levels.
    => Compatibility
        -> Strings are widely used across programming languages, making them a universal data type.
        -> This means that strings can be easily transferred between different systems and platforms, making them a reliable and efficient way to communicate and share data.
    => Memory Efficiency
        -> Strings are usually stored in a contiguous block of memory, which makes them efficient to allocate and deallocate.
        -> This means that they can be used to represent large amounts of data without taking up too much memory.

    >> Disadvantages
    => Memory Consumption
        -> Strings can consume a lot of memory, especially when working with large strings or many strings.
        -> This can be a problem in memory-constrained environments, such as embedded systems or mobile devices.
    => Immutability
        -> In many programming languages, strings are immutable, meaning that they cannot be changed once they are created.
        -> This can be a disadvantage when working with large or complex strings that require frequent modifications, as it can lead to inefficiencies and memory overhead.
    => Performance Overhead
        -> String operations can be slower than operations on other data types, especially when working with large or complex strings.
        -> This is because string operations often involve copying and reallocating memory, which can be time-consuming.
    => Encoding and Decoding Overhead
        -> Strings can have different character encodings, which can lead to overhead when converting between them.
        -> This can be a problem when working with data from different sources or when communicating with systems that use different encodings.
    => Security Vulnerabilities
        -> Strings can be vulnerable to security vulnerabilities, such as buffer overflows or injection attacks, if not handled properly.
        -> This is because strings can be manipulated by attackers to execute arbitrary code or access sensitive data.

    ! =================================================================================================================
    |🖇️ REFERENCES
    + Introduction to Strings: https://www.geeksforgeeks.org/introduction-to-strings-data-structure-and-algorithm-tutorials/
    + Applications, Advantages and Disadvantages of String: https://www.geeksforgeeks.org/applications-advantages-and-disadvantages-of-string/

"""
# ! ===================================================================================================================
