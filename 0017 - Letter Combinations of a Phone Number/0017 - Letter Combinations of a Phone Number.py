from typing import List

def letter_combinations(digits: str) -> List[str]:
    """
    Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.

    A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

    Example:
    Input: "23"
    Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

    Note:

    Although the above answer is in lexicographical order, your answer could be in any order you want.


    >>> letter_combinations('')
    []

    >>> letter_combinations('23')
    ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']

    """
    if not digits:
        return []
    #

    DIGIT_LETTER_MAP = {'2': ['a', 'b', 'c'],
                        '3': ['d', 'e', 'f'],
                        '4': ['g', 'h', 'i'],
                        '5': ['j', 'k', 'l'],
                        '6': ['m', 'n', 'o'],
                        '7': ['p', 'q', 'r', 's'],
                        '8': ['t', 'u', 'v'],
                        '9': ['w', 'x', 'y', 'z']}
    res = ['']
    for digit in digits:
        chars = DIGIT_LETTER_MAP[digit]
        res = [r + c for r in res for c in chars]
    #
    return res
#


if __name__ == '__main__':
    import doctest

    doctest.testmod()
