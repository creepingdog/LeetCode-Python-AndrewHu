def expand(s: str, size: int, left: int, right: int) -> (int, int, int):
    left_mark, right_mark, max_len = left, right, 0
    while left >= 0 and right < size and s[left] == s[right]:
        left -= 1
        right += 1
    #

    length = right - left - 1
    if length > max_len:
        max_len = length
        left_mark = left + 1
        right_mark = right - 1
    #
    return (max_len, left_mark, right_mark)


#

def longest_palindrome(s: str) -> str:
    """
    Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

    Example 1:
    Input: "babad"
    Output: "bab"
    Note: "aba" is also a valid answer.

    Example 2:
    Input: "cbbd"
    Output: "bb"

    >>> longest_palindrome('babad')
    'bab'
    >>> longest_palindrome('cbbd')
    'bb'
    >>> longest_palindrome('babad')
    'bab'
    """

    size = len(s)
    left_mark, right_mark, max_len = 0, 0, 0

    for i, c in enumerate(s):
        max_len1, left_mark1, right_mark1 = expand(s, size, i, i)
        # print('i={}, c={}, max_len1={}, left_mark1={}, right_mark1={}'.format(i, c, max_len1, left_mark1, right_mark1))
        max_len2, left_mark2, right_mark2 = expand(s, size, i, i + 1)
        # print('i={}, c={}, max_len2={}, left_mark2={}, right_mark2={}'.format(i, c, max_len2, left_mark2, right_mark2))
        if max_len1 > max_len:
            left_mark = left_mark1
            right_mark = right_mark1
            max_len = max_len1
        #
        if max_len2 > max_len:
            left_mark = left_mark2
            right_mark = right_mark2
            max_len = max_len2
        #
    #
    return s[left_mark:(right_mark + 1)]
#


if __name__ == '__main__':
    import doctest

    doctest.testmod()