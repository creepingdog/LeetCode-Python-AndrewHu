def divide(dividend: int, divisor: int) -> int:
    """
    Given two integers dividend and divisor, divide two integers without using multiplication, division and mod operator.

    Return the quotient after dividing dividend by divisor.

    The integer division should truncate toward zero.

    Example 1:

    Input: dividend = 10, divisor = 3
    Output: 3

    Example 2:

    Input: dividend = 7, divisor = -3
    Output: -2

    Note:

        Both dividend and divisor will be 32-bit signed integers.
        The divisor will never be 0.
        Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 231 − 1 when the division result overflows.


    >>> divide(10, 3)
    3
    >>> divide(7, -3)
    -2
    >>> divide(-7, 3)
    -2
    >>> divide(-7, -3)
    2
    >>> divide(1, 1)
    1
    >>> divide(-2147483648, -1)
    2147483647
    """
    INT_MAX = 2147483647
    INT_MIN = -2147483648

    if dividend < INT_MIN or dividend > INT_MAX or divisor < INT_MIN or divisor > INT_MAX:
        return INT_MAX
    #
    if (dividend == INT_MIN) and (divisor == -1):
        return INT_MAX
    if divisor == 1:
        return dividend
    if divisor == -1:
        return -dividend
    #
    positive = dividend ^ divisor >= 0
    dividend = abs(dividend)
    divisor = abs(divisor)

    res = 0
    while dividend >= divisor:
        temp = 0
        while dividend >= divisor << temp:
            dividend -= divisor << temp
            res += 1 << temp
            temp += 1
        #
    #

    # res = 0
    # while dividend >= divisor:
    #     tmp = divisor
    #     quotient = 1
    #     while tmp + tmp < dividend:
    #         tmp += tmp
    #         quotient += quotient
    #         # print('tmp={}, quotient={}'.format(tmp, quotient))
    #     #
    #     dividend -= tmp
    #     res += quotient
    #     # print('dividend={}, res={}'.format(dividend, res))
    # #

    return res if positive else -res
#