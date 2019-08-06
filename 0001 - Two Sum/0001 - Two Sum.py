from typing import List


def two_sum(nums: List[int], target: int) -> List[int]:
    """
    Given an array of integers, return **indices** of the two numbers such that they add up to a specific target.

    You may assume that each input would have ***exactly*** one solution, and you may not use the *same* element twice.

    **Example:**

    ```
    Given nums = [2, 7, 11, 15], target = 9,

    Because nums[0] + nums[1] = 2 + 7 = 9,
    return [0, 1].
    ```

    >>> two_sum([2,7,11,15], 9)
    [0, 1]

    >>> two_sum([3, 5, 2, -4, 8, 11], 7)
    [1, 2]

    >>> two_sum([12,15,18,19], 9)

    """


    num_dict = dict()

    for i, num in enumerate(nums):
        diff = target - num

        if diff in num_dict:
            return [num_dict[diff], i]
        #
        num_dict[num] = i
        #
    #
#


if __name__ == '__main__':
    import doctest

    doctest.testmod()


