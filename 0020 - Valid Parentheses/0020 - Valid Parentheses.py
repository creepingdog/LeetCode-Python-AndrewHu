def is_valid(s: str) -> bool:
    """
    Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

    An input string is valid if:

        Open brackets must be closed by the same type of brackets.
        Open brackets must be closed in the correct order.

    Note that an empty string is also considered valid.

    Example 1:
    Input: "()"
    Output: true

    Example 2:
    Input: "()[]{}"
    Output: true

    Example 3:
    Input: "(]"
    Output: false

    Example 4:
    Input: "([)]"
    Output: false

    Example 5:
    Input: "{[]}"
    Output: true

    >>> is_valid('()')
    True
    >>> is_valid('()[]{}')
    True
    >>> is_valid('(]')
    False
    >>> is_valid('([)]')
    False
    >>> is_valid('{[]}')
    True
    >>> is_valid('(')
    False
    """

    MATCH = {'(': ')',
             '[': ']',
             '{': '}'}

    expected = []
    for c in s:
        if c in MATCH:
            expected.append(MATCH[c])
        elif expected and c == expected[-1]:
            expected.pop()
        else:
            return False
        #
    #
    if expected:
        return False
    else:
        return True
    #
#


if __name__ == '__main__':
    import doctest

    doctest.testmod()
