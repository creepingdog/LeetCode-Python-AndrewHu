from typing import List


def two_sum(nums: List[int], start: int, target: int) -> List[List[int]]:
    num_dict = dict()
    seen_dict = dict()
    res = list()
    for num in nums[start:]:
        if num in seen_dict:
            continue
        #
        comp = target - num
        if comp in num_dict:
            res.append([num, comp])
            seen_dict[num] = 1
            seen_dict[comp] = 1
        #
        num_dict[num] = 1
    #
    return res
#


def three_sum(nums: List[int]) -> List[List[int]]:
    """
    Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

    Note:

    The solution set must not contain duplicate triplets.

    Example:

    Given array nums = [-1, 0, 1, 2, -1, -4],

    A solution set is:
    [
      [-1, 0, 1],
      [-1, -1, 2]
    ]

    >>> three_sum([-1, 0, 1, 2, -1, -4])
    [[-1, 0, 1], [-1, -1, 2]]

    """

    size = len(nums)
    res = list()
    if size < 3:
        return res
    #

    nums.sort()
    seen_dict = dict()
    for i in range(size - 2):
        num = nums[i]
        if num in seen_dict:
            continue
        #
        seen_dict[num] = 1
        two_sum_res = two_sum(nums, i + 1, -num)
        for item in two_sum_res:
            item.append(num)
            item.sort()
            res.append(item)
        #
    #
    return res
#


if __name__ == '__main__':
    import doctest

    doctest.testmod()
