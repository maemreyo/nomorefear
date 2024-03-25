"""
    |〽️ SLIDING WINDOW TECHNIQUE

    ! =================================================================================================================
    |🔎 GENERAL
    ==> Sliding Window problems are problems in which a fixed or variable-size window is moved through a data structure,
    typically an array or string, to solve problems efficiently based on continuous subsets of elements.

    ==> This technique is used when we need to find sub-arrays or sub-strings according to a give set of conditions.

    ! =================================================================================================================
    |⚙️ HOW IT WORKS?
    ==> A sliding window is a common technique used in various algorithms and applications, particularly in computer science
    and signal processing. It involves moving a fixed-size window (or a "window of interest") across a sequence of data
    points or elements, performing operations on the data within the window at each step.

    ==> Steps:
    @Define the Window size
        -> Start by determining the size of the window you want to use
        -> This size is usually fixed and determined based on the specific problem you're addressing or the
        characteristics of the data

    @Initialize the Window
        -> Position the window at the beginning of the data sequence

    @Process the Data
        -> At each step, the window moves forward (or slides) by one element
        -> The data within the window is then processed or analyzed according to the requirements of the problem

    @Output or Store Results
        -> After processing each window, you may output some result or store it for later use, depending on the
        application

    @Repeat
        -> Continue sliding the window across the entire data sequence until you have covered all relevant data points

    ! =================================================================================================================
    |📟 PSEUDOCODE
    function slidingWindow(data, windowSize):
        // Assuming 'data' is an array or a sequence of elements
        // 'windowSize' is the size of the sliding window

        // Initialize variables
        start = 0
        end = windowSize - 1

        // Process the first window
        while end < length(data):
            // Process data within the current window [start, end]
            processWindow(data[start:end+1])

            // Slide the window forward
            start++
            end++

    ! =================================================================================================================
    |📌 NOTE
    >> How to use Sliding Window Technique?
    1. Fixed Size Sliding Window
    The general steps to solve these questions by following below steps:
        -> Find the size of the window required, say K
        -> Compute the result for 1st window, i.e. include the first K elements of the data structure
        -> Then use a loop to slide the window by 1 and keep computing the result window by window

    2. Variable Size Sliding Window
    The general steps to solve these questions by following below steps:
        -> In this type of sliding window problem, we increase our right pointer one by one til our condition is true
        -> At any step if our condition does not match, we shrink the size of our window by increase left pointer
        -> Again, when our condition satisfies, we start increasing the right pointer and follow step 1
        -> We follow these steps until we reach to the end of the array

    >> How to identify Sliding Window Problems
    -> These problems generally require Finding Maximum/Minimum Sub-arrays, Sub-strings which satisfy some specific condition
    -> The size ò the sub-array or sub-string 'K' will be given in some of the problems
    -> These problems can easily be solved in O(n^2) time complexity using nested loops, using sliding window we can solve these in O(n) time complexity instead
    -> Required Time Complexity: O(N) or O(N*log(N))

    >> Use cases
    -> Find the maximum sum of all sub-arrays of size K
    -> Smallest sub-array with sum greater than a given value
    -> Find sub-array with sum in an array of non-negative integers
    -> Smallest window that contains all characters of string itself
    ! =================================================================================================================
    |👀 FAQs
    Q. What tasks should be solved by the Sliding Window technique?
        @Signal Processing
            -> Analyzing signals such as audio or video data by applying filters or feature extraction techniques within the sliding window.

        @Time Series Analysis
            -> Analyzing sequential data over time to identify patterns, trends, or anomalies.

        @String Matching
            -> Searching for patterns within a string by sliding a window across the text.

        @Data Compression
            -> Techniques such as Run-length Encoding or Sliding Window Compression utilize similar principles.

    ! =================================================================================================================
    |🖇️ REFERENCES
    + https://www.geeksforgeeks.org/window-sliding-technique/?ref=gcse
    + https://www.geeksforgeeks.org/sliding-window-problems-identify-solve-and-interview-questions/?ref=header_search
"""
