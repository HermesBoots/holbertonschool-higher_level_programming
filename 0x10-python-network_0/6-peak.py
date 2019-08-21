#!/usr/bin/python3
"""Module to find a peak in a list of numbers"""


def do_find_peak(nums, left, right):
    """Recursive helper function for find_peak"""

    if left >= right:
        return nums[left]
    index = left + (right - left) // 2
    if (
        (index == len(nums) - 1 or nums[index + 1] < nums[index]) and
        (index == 0 or nums[index - 1] < nums[index])
    ):
        return nums[index]
    if index < len(nums) - 1 and nums[index + 1] > nums[index]:
        return do_find_peak(nums, index + 1, right)
    else:
        return do_find_peak(nums, left, index)

def find_peak(list_of_integers):
    """Find a peak in a list of integers"""

    length = len(list_of_integers)
    if length < 1:
        return None
    if length == 1:
        return list_of_integers[0]
    if length == 2:
        return max(list_of_integers)
    return do_find_peak(list_of_integers, 0, length)
