#!/usr/bin/python3
"""Module to find a peak in a list of numbers"""


def find_peak(list_of_integers):
    """Find a peak in a list of integers"""

    subLen = len(list_of_integers)
    if subLen < 1:
        return None
    if subLen == 1:
        return list_of_integers[0]
    if subLen == 2:
        return max(list_of_integers)
    nums = [float('-inf')] + list_of_integers + [float('-inf')]
    left = 1
    right = subLen + 1
    index = subLen // 2
    while subLen > 0:
        if nums[index - 1] < nums[index] and nums[index + 1] < nums[index]:
            return nums[index]
        if nums[index + 1] > nums[index]:
            left = index + 1
            subLen = right - left
            index = left + subLen // 2
        else:
            right = index
            subLen = right - left
            index = left + subLen // 2
    return nums[index]
