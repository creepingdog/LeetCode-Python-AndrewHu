def int_to_roman(num: int) -> str:
    """
    Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

    Symbol       Value
    I             1
    V             5
    X             10
    L             50
    C             100
    D             500
    M             1000

    For example, two is written as II in Roman numeral, just two one's added together. Twelve is written as, XII, which is simply X + II. The number twenty seven is written as XXVII, which is XX + V + II.

    Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

        I can be placed before V (5) and X (10) to make 4 and 9.
        X can be placed before L (50) and C (100) to make 40 and 90.
        C can be placed before D (500) and M (1000) to make 400 and 900.

    Given an integer, convert it to a roman numeral. Input is guaranteed to be within the range from 1 to 3999.

    Example 1:
    Input: 3
    Output: "III"

    Example 2:
    Input: 4
    Output: "IV"

    Example 3:
    Input: 9
    Output: "IX"

    Example 4:
    Input: 58
    Output: "LVIII"
    Explanation: L = 50, V = 5, III = 3.

    Example 5:
    Input: 1994
    Output: "MCMXCIV"
    Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

    >>> int_to_roman(3)
    'III'
    >>> int_to_roman(4)
    'IV'
    >>> int_to_roman(9)
    'IX'
    >>> int_to_roman(58)
    'LVIII'
    >>> int_to_roman(1994)
    'MCMXCIV'
    """

    if num < 1 or num > 3999:
        raise Exception('The input num should be in [1, 3999]')
    #

    res = ""
    quotient, reminder = divmod(num, 1000)
    if quotient > 0:
        res += 'M' * quotient
    #

    quotient, reminder = divmod(reminder, 100)
    if quotient == 9:
        res += 'CM'
    elif quotient == 5:
        res += 'D'
    elif quotient == 4:
        res += 'CD'
    elif quotient > 5:
        res += 'D'
        quotient -= 5
        res += 'C' * quotient
    else:
        res += 'C' * quotient
    #

    quotient, reminder = divmod(reminder, 10)
    if quotient == 9:
        res += 'XC'
    elif quotient == 5:
        res += 'L'
    elif quotient == 4:
        res += 'XL'
    elif quotient > 5:
        res += 'L'
        quotient -= 5
        res += 'X' * quotient
    else:
        res += 'X' * quotient
    #

    quotient = reminder
    if quotient == 9:
        res += 'IX'
    elif quotient == 5:
        res += 'V'
    elif quotient == 4:
        res += 'IV'
    elif quotient > 5:
        res += 'V'
        quotient -= 5
        res += 'I' * quotient
    else:
        res += 'I' * quotient
    #
    return res
#


if __name__ == '__main__':
    import doctest

    doctest.testmod()
