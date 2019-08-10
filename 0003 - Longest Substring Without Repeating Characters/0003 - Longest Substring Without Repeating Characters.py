def length_of_longest_substring(s: str) -> int:
    """
    Given a string, find the length of the longest substring without repeating characters.

    Example 1:
    Input: "abcabcbb"
    Output: 3
    Explanation: The answer is "abc", with the length of 3.

    Example 2:
    Input: "bbbbb"
    Output: 1
    Explanation: The answer is "b", with the length of 1.

    Example 3:
    Input: "pwwkew"
    Output: 3
    Explanation: The answer is "wke", with the length of 3.
                 Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

    >>> length_of_longest_substring("abcabcbb")
    3
    >>> length_of_longest_substring("bbbbb")
    1
    >>> length_of_longest_substring("pwwkew")
    3
    >>> length_of_longest_substring("abba")
    2
    >>> length_of_longest_substring("au")
    2
    >>> length_of_longest_substring("")
    0
    """

    if not s:
        return 0
    #
    index_dict = dict()

    start, end, max_len = 0, 0, 1
    for i, c in enumerate(s):
        if c in index_dict:
            start = max(start, index_dict[c] + 1)
        #
        tmp = i+1
        length = tmp - start
        if length >= max_len:
            end = tmp
            max_len = length
        #
        index_dict[c] = i
    #
    return max_len
#


if __name__ == '__main__':
    import doctest

    doctest.testmod()
