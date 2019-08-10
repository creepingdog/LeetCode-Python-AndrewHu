from typing import List


def three_sum_closest(nums: List[int], target: int) -> int:
    """
    Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

    Example:

    Given array nums = [-1, 2, 1, -4], and target = 1.

    The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

    >>> three_sum_closest([-1, 2, 1, -4], 1)
    2

    >>> three_sum_closest([6,-8,-50,-10,-3,4,-55,-96,69,75,-76,38,23,-38,49,-29,47,-19,-65,-56,10,96,-76,58,10,-40,76,78,22,-98,88,-58,-96,-98,38,29,81,80,13,32,36,75,16,-9,67,75,-32,-55,-42,88,72,95,-39,6,77,42,-43,23,-69,29,-71,22,-1,97,-96,-56,33,52,-90,57,-63,-11,-83,30,-99,86,-28,38,51,-72,50,-12,-43,88,88,-64,76,-21,41,42,42,-75,-1,32,-79,-31,30,-44,73,71,-7,77,-8,7,15,55,43,94,7,29,95,46,36,-63,53,-36,67,-10,-10,-90,-100,-16,-39,-52,1,64,8,87,99,53,82,45,-68,89,4,36,55,-11,28,6,45,91,-79,63,-59,-96], 67)
    67
    """

    size = len(nums)
    if size < 3:
        return None
    #
    nums.sort()
    sol_sum = 2 ** 30
    for i in range(size - 2):
        j = i + 1
        k = size - 1
        while j < k:
            s = nums[i] + nums[j] + nums[k]
            if s == target:
                return target
            elif abs(s - target) < abs(sol_sum - target):
                sol_sum = s
            #
            if s > target:
                k -= 1
            elif s < target:
                j += 1
            #
        #
    #
    return sol_sum
#


if __name__ == '__main__':
    import doctest

    doctest.testmod()
