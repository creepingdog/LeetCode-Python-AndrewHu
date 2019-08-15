from typing import List


def find_substring(s: str, words: List[str]) -> List[int]:
    """
    You are given a string, s, and a list of words, words, that are all of the same length. Find all starting indices of substring(s) in s that is a concatenation of each word in words exactly once and without any intervening characters.

    Example 1:
    Input:
      s = "barfoothefoobarman",
      words = ["foo","bar"]
    Output: [0,9]
    Explanation: Substrings starting at index 0 and 9 are "barfoor" and "foobar" respectively.
    The output order does not matter, returning [9,0] is fine too.

    Example 2:
    Input:
      s = "wordgoodgoodgoodbestword",
      words = ["word","good","best","word"]
    Output: []

    >>> find_substring('barfoothefoobarman', ['foo', 'bar'])
    [0, 9]
    >>> find_substring('wordgoodgoodgoodbestword', ['word', 'good', 'best', 'word'])
    []
    >>> find_substring('wordgoodgoodgoodbestword', ['word', 'good', 'best', 'good'])
    [8]
    """
    if not s or not words:
        return list()
        #
    length = len(words[0])
    size = len(s)
    if size < length:
        return list()
    #
    WORD_DICT = dict()
    for word in words:
        WORD_DICT[word] = WORD_DICT.get(word, 0) + 1
    #
    # print(WORD_DICT)
    num_words = len(words)
    res = list()
    word_dict = dict()
    for i in range(size - length * num_words + 1):
        word_dict.update(WORD_DICT)
        for j in range(i, i + (num_words - 1) * length + 1, length):
            word_to_test = s[j:(j + length)]
            # print('j={}, word_to_test={}'.format(j, word_to_test))
            if word_to_test in word_dict:
                word_dict[word_to_test] = word_dict[word_to_test] - 1
                if word_dict[word_to_test] == 0:
                    del word_dict[word_to_test]
                #
            #
        #
        if not word_dict:
            res.append(i)
        #
    #
    return res
#


if __name__ == '__main__':
    import doctest

    doctest.testmod()


