from typing import List


def max_area(height: List[int]) -> int:
    """
    Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

    Note: You may not slant the container and n is at least 2.

    The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

    Example:
    Input: [1,8,6,2,5,4,8,3,7]
    Output: 49

    >>> max_area([1,8,6,2,5,4,8,3,7])
    49
    """

    total_len = len(height)
    max_area, left, right = 0, 0, total_len - 1
    # res_left, res_right = 0, total_len-1
    while left < right:
        area = (right - left) * min(height[left], height[right])
        # if area > max_area:
        #     # res_left, res_right = left, right
        #     max_area = area
        # #
        max_area = max(max_area, area)
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
        #
    #
    return max_area
    # return res_left, res_right
#


if __name__ == '__main__':
    import doctest

    doctest.testmod()
