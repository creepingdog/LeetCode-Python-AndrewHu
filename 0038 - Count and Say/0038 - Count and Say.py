def count_and_say_a_num(num: int) -> int:
    """
    >>> count_and_say_a_num(21)
    1211
    """
    quotient, reminder = divmod(num, 10)
    curr_digit, count = reminder, 1
    res, power = 0, 0
    while quotient>9 or reminder!=0:
        # print('quotient={}'.format(quotient), end=', ')
        quotient, reminder = divmod(quotient, 10)
        # print('quotient={}, reminder={}'.format(quotient, reminder), end=', ')
        if reminder == curr_digit:
            count += 1
        else:
            res = count*pow(10, power+1) + curr_digit*pow(10, power) + res
            curr_digit = reminder
            count = 1
            power += 2
        #
        # print('curr_digit={}, count={}, res={}'.format(curr_digit, count, res))
    #
    return res
#

def count_and_say_a_num_str(num: str) -> str:
    """
    >>> count_and_say_a_num_str('21')
    '1211'
    """
    if not num:
        return ''
    #
    curr_digit = num[0]
    count = 0
    # res = ['']*(len(num)*2)
    # p = 0
    res = ''
    for digit in num:
        if digit==curr_digit:
            count += 1
        else:
            # res[p] = str(count)
            # res[p+1] = str(curr_digit)
            res += str(count)
            res += str(curr_digit)
            count = 1
            # p += 2
        #
        curr_digit = digit
    #
    # res[p] = count
    # res[p + 1] = curr_digit
    res += str(count)
    res += str(curr_digit)
    return res
#


def count_and_say(n: int) -> str:
    """
    The count-and-say sequence is the sequence of integers with the first five terms as following:

    1.     1
    2.     11
    3.     21
    4.     1211
    5.     111221

    1 is read off as "one 1" or 11.
    11 is read off as "two 1s" or 21.
    21 is read off as "one 2, then one 1" or 1211.

    Given an integer n where 1 ≤ n ≤ 30, generate the nth term of the count-and-say sequence.

    Note: Each term of the sequence of integers will be represented as a string.


    Example 1:
    Input: 1
    Output: "1"

    Example 2:
    Input: 4
    Output: "1211"

    >>> count_and_say(1)
    '1'
    >>> count_and_say(2)
    '11'
    >>> count_and_say(3)
    '21'
    >>> count_and_say(4)
    '1211'
    >>> count_and_say(5)
    '111221'
    >>> count_and_say(6)
    '312211'
    >>> count_and_say(7)
    '13112221'
    >>> count_and_say(8)
    '1113213211'
    """
    if n==1:
        return '1'
    #
    # prev = 1
    # for i in range(n-1):
    #     prev = count_and_say_a_num(prev)
    # #
    # return str(prev)

    res = '1'
    for i in range(n - 1):
        res = count_and_say_a_num_str(res)
    #
    return res
#


if __name__ == '__main__':
    import doctest

    doctest.testmod()
#