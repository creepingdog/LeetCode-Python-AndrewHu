def longestCommonPrefix(strs: List[str]) -> str:
    """
    Write a function to find the longest common prefix string amongst an array of strings.

    If there is no common prefix, return an empty string "".

    Example 1:
    Input: ["flower","flow","flight"]
    Output: "fl"

    Example 2:
    Input: ["dog","racecar","car"]
    Output: ""
    Explanation: There is no common prefix among the input strings.

    Note:
    All given inputs are in lowercase letters a-z.

    >>> longestCommonPrefix(["flower","flow","flight"])
    'fl'
    >>> longestCommonPrefix(["dog","racecar","car"])
    ''
    >>> longestCommonPrefix(["aa","a"])
    'a'
    """

    if not strs:
        return ""
    #
    lens = [len(x) for x in strs]
    size = min(lens)
    if size == 0:
        return ''
    #

    for i in range(size):
        c = strs[0][i]
        for j in range(1, len(strs)):
            if c != strs[j][i]:
                return strs[0][:i]
            #
        #
    #
    return strs[0][:size]
#


if __name__ == '__main__':
    import doctest

    doctest.testmod()

