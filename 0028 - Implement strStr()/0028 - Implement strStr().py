def str_str(haystack: str, needle: str) -> int:
    """
    Implement strStr().

    Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

    Example 1:
    Input: haystack = "hello", needle = "ll"
    Output: 2

    Example 2:
    Input: haystack = "aaaaa", needle = "bba"
    Output: -1

    Clarification:
    What should we return when needle is an empty string? This is a great question to ask during an interview.
    For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().

    >>> str_str('hello', 'll')
    2
    >>> str_str('aaaaa', 'bba')
    -1
    >>> str_str('test', '')
    0
    >>> str_str('', 'new')
    -1
    >>> str_str('new', 'this')
    -1
    """
    if not needle:
        return 0
    #
    if not haystack:
        return -1
    #
    size_needle = len(needle)
    size_haystack = len(haystack)
    for i in range(size_haystack - size_needle + 1):
        if haystack[i:(i + size_needle)] == needle:
            return i
        #
    #
    return -1
#


if __name__ == '__main__':
    import doctest

    doctest.testmod()
