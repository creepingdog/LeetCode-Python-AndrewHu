from typing import List


def bisearch(nums: List[int], target: int, left: int, right: int) -> List[int]:
    if left==right-1:
        if nums[left]==target:
            return [left, right] if nums[right]==target else [left, left]
        else:
            return [right, right] if nums[right]==target else None
        #
    #
    if target<nums[left] or target>nums[right]:
        return None
    #
    mid = left + int((right-left)/2)
    indices = bisearch(nums, target, left, mid)
    if indices is None:
        return bisearch(nums, target, mid, right)
    #
    if indices[1]<mid:
        return indices
    #
    right_indices = bisearch(nums, target, mid, right)
    return [indices[0], right_indices[1]]
#


def search_range(nums: List[int], target: int) -> List[int]:
    """
    Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

    Your algorithm's runtime complexity must be in the order of O(log n).

    If the target is not found in the array, return [-1, -1].

    Example 1:
    Input: nums = [5,7,7,8,8,10], target = 8
    Output: [3,4]

    Example 2:
    Input: nums = [5,7,7,8,8,10], target = 6
    Output: [-1,-1]

    >>> search_range([5,7,7,8,8,10], 8)
    [3, 4]
    >>> search_range([5,7,7,8,8,10], 6)
    [-1, -1]
    """
    if not nums:
        return [-1, -1]
        #
    size = len(nums)
    if size == 1:
        return [0, 0] if nums[0] == target else [-1, -1]
    #
    res = bisearch(nums, target, 0, size - 1)
    return [-1, -1] if res is None else res
#


if __name__ == '__main__':
    import doctest

    doctest.testmod()

