def reverse(x: int) -> int:
    """
    Given a 32-bit signed integer, reverse digits of an integer.

    Example 1:
    Input: 123
    Output: 321

    Example 2:
    Input: -123
    Output: -321

    Example 3:
    Input: 120
    Output: 21

    Note:
    Assume we are dealing with an environment which could only store integers within the 32-bit signed
    integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns
     0 when the reversed integer overflows.


    >>> reverse(123)
    321

    >>> reverse(-123)
    -321

    >>> reverse(120)
    21

    >>> reverse(1534236469)
    0

    """

    MAX_POS_INT = 2147483647
    MAX_NEG_INT = -2147483648

    if x < MAX_NEG_INT or x > MAX_POS_INT:
        return 0
    #
    if x < 0:
        negative = True
        x = -x
    else:
        negative = False
    #
    quotient, modulo = x, 0
    res = 0
    while quotient:
        quotient, modulo = divmod(quotient, 10)
        # print(quotient, modulo)
        res = res * 10 + modulo
    #
    if negative:
        res = -res
    #
    if res < MAX_NEG_INT or res > MAX_POS_INT:
        return 0
    #

    return res
#


if __name__ == '__main__':
    import doctest

    doctest.testmod()
