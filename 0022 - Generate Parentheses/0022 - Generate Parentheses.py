from typing import List


# def generate_parenthesis_recu(n: int, results: set) -> set:
#     if n==1:
#         return set(['()'])
#     #
#     res = set()
#     for item in generate_parenthesis_recu(n-1, results):
#         res.add('()'+item)
#         res.add('(' + item+')')
#         res.add(item + '()')
#     #
#     return res
# #


def generate_parenthesis(n: int) -> List[str]:
    """
     Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

    For example, given n = 3, a solution set is:

    [
      "((()))",
      "(()())",
      "(())()",
      "()(())",
      "()()()"
    ]

    >>> generate_parenthesis(0)
    ['']
    >>> generate_parenthesis(1)
    ['()']
    >>> generate_parenthesis(2)
    ['(())', '()()']
    >>> generate_parenthesis(3)
    ['((()))', '(()())', '(())()', '()(())', '()()()']
    >>> generate_parenthesis(4)
    ['(((())))', '((()()))', '((())())', '((()))()', '(()(()))', '(()()())', '(()())()', '(())(())', '(())()()', '()((()))', '()(()())', '()(())()', '()()(())', '()()()()']
    """
    if not n: return ['']
    res = []

    for c in range(n):
        for left in generate_parenthesis(c):
            for right in generate_parenthesis(n - 1 - c):
                res.append('({}){}'.format(left, right))
            #
        #
    #
    res.sort()
    return res
#


if __name__ == '__main__':
    import doctest

    doctest.testmod()

