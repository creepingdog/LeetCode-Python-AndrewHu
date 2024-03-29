def my_atoi(str: str) -> int:
    """
    Implement atoi which converts a string to an integer.

    The function first discards as many whitespace characters as necessary until the first non-whitespace character is found. Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits as possible, and interprets them as a numerical value.

    The string can contain additional characters after those that form the integral number, which are ignored and have no effect on the behavior of this function.

    If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.

    If no valid conversion could be performed, a zero value is returned.

    Note:

    Only the space character ' ' is considered as whitespace character.
    Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. If the numerical value is out of the range of representable values, INT_MAX (231 − 1) or INT_MIN (−231) is returned.

    Example 1:
    Input: "42"
    Output: 42

    Example 2:

    Input: "   -42"
    Output: -42
    Explanation: The first non-whitespace character is '-', which is the minus sign.
                 Then take as many numerical digits as possible, which gets 42.

    Example 3:

    Input: "4193 with words"
    Output: 4193
    Explanation: Conversion stops at digit '3' as the next character is not a numerical digit.

    Example 4:

    Input: "words and 987"
    Output: 0
    Explanation: The first non-whitespace character is 'w', which is not a numerical
                 digit or a +/- sign. Therefore no valid conversion could be performed.

    Example 5:

    Input: "-91283472332"
    Output: -2147483648
    Explanation: The number "-91283472332" is out of the range of a 32-bit signed integer.
                 Thefore INT_MIN (−231) is returned.

    >>> my_atoi("  -0012a42")
    -12

    >>> my_atoi("42")
    42

    >>> my_atoi("+36")
    36

    >>> my_atoi("    -42")
    -42

    >>> my_atoi("4193 with words")
    4193

    >>> my_atoi("-91283472332")
    -2147483648

    >>> my_atoi("91283472332")
    2147483647
    """

    if not str:
        return 0
    #

    NUM_CHARS = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
    INT_MIN = pow(2, 31)
    INT_MAX = INT_MIN - 1

    str = str.lstrip(' ')
    if not str:
        return 0
    #
    negative = False
    if str[0] == '-':
        negative = True
        str = str[1:]
    elif str[0] == '+':
        negative = False
        str = str[1:]
    elif str[0] not in NUM_CHARS:
        return 0
    #

    res = 0
    ORD_ZERO = ord('0')
    for c in str:
        if c not in NUM_CHARS:
            break
        #
        tmp = ord(c) - ORD_ZERO
        res = res * 10 + tmp
        if negative:
            if res >= INT_MIN:
                return -INT_MIN
        else:
            if res >= INT_MAX:
                return INT_MAX
            #
        #
    #
    return -res if negative else res
#


if __name__ == '__main__':
    import doctest

    doctest.testmod()
