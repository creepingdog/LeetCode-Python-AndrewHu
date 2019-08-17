from typing import List


def search_insert(nums: List[int], target: int) -> int:
    """
    Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

    You may assume no duplicates in the array.

    Example 1:
    Input: [1,3,5,6], 5
    Output: 2

    Example 2:
    Input: [1,3,5,6], 2
    Output: 1

    Example 3:
    Input: [1,3,5,6], 7
    Output: 4

    Example 4:
    Input: [1,3,5,6], 0
    Output: 0

    >>> search_insert([1,3,5,6], 0)
    0
    >>> search_insert([1,3,5,6], 1)
    0
    >>> search_insert([1,3,5,6], 2)
    1
    >>> search_insert([1,3,5,6], 3)
    1
    >>> search_insert([1,3,5,6], 4)
    2
    >>> search_insert([1,3,5,6], 5)
    2
    >>> search_insert([1,3,5,6], 6)
    3
    >>> search_insert([1,3,5,6], 7)
    4
    >>> search_insert([1], 2)
    1
    >>> search_insert([1], 0)
    0
    """
    if not nums:
        return 0
    #
    size = len(nums)
    if size == 1:
        return 0 if target <= nums[0] else 1
    #
    left, right = 0, size - 1
    while True:
        mid = left + int((right - left) / 2)
        # print('left={}, right={}, mid={}'.format(left, right, mid))
        if nums[mid] == target:
            return mid
        #
        if nums[mid] < target:
            left = mid + 1
        else:
            right = max(0, mid - 1)
        #
        if left >= right:
            return right if nums[right] >= target else (right + 1)
        #
    #
#


if __name__ == '__main__':
    import doctest

    doctest.testmod()
