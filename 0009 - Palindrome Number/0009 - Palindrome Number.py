def is_palindrome(x: int) -> bool:
    """
    Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

    Example 1:
    Input: 121
    Output: true

    Example 2:
    Input: -121
    Output: false
    Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

    Example 3:
    Input: 10
    Output: false
    Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

    Follow up:
    Coud you solve it without converting the integer to a string?

    >>> is_palindrome(121)
    True
    >>> is_palindrome(-121)
    False
    >>> is_palindrome(10)
    False
    >>> is_palindrome(101)
    True
    >>> is_palindrome(21120)
    False

    """

    if x < 0:
        return False
    elif x <= 9:
        return True
        #
    quotient = x
    reverse = 0
    while quotient > 9:
        quotient, reminder = divmod(quotient, 10)
        if not reverse and not reminder:
            return False
        #
        # print(quotient, reminder, reverse)
        if quotient == reverse:
            return True
        reverse = reverse * 10 + reminder
        if reverse == quotient:
            return True
        #
    #
    return False
#


if __name__ == '__main__':
    import doctest

    doctest.testmod()
