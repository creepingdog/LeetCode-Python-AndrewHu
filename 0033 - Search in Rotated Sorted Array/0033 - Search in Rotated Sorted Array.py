from typing import List


def bisearch(nums: List[int], target: int, left: int, right: int) -> int:
    if left == right - 1:
        return left if nums[left] == target else right if nums[right] == target else -1
    #
    if (nums[left] < nums[right]) and (target < nums[left] or target > nums[right]):
        return -1
    #
    mid = left + int((right - left) / 2)
    index = bisearch(nums, target, left, mid)
    return index if index != -1 else bisearch(nums, target, mid, right)
#

def search(nums: List[int], target: int) -> int:
    """
    Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

    (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

    You are given a target value to search. If found in the array return its index, otherwise return -1.

    You may assume no duplicate exists in the array.

    Your algorithm's runtime complexity must be in the order of O(log n).

    Example 1:

    Input: nums = [4,5,6,7,0,1,2], target = 0
    Output: 4

    Example 2:

    Input: nums = [4,5,6,7,0,1,2], target = 3
    Output: -1

    >>> search([4,5,6,7,0,1,2], 0)
    4
    >>> search([4,5,6,7,0,1,2], 3)
    -1
    """
    if not nums:
        return -1
    #
    size = len(nums)
    if size == 1:
        return 0 if nums[0] == target else -1
    #
    return bisearch(nums, target, 0, size - 1)
#


if __name__ == '__main__':
    import doctest

    doctest.testmod()
