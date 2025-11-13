"""
Array Shift
Given an array and an integer representing how many positions to shift the array, return the shifted array.

A positive integer shifts the array to the left.
A negative integer shifts the array to the right.
The shift wraps around the array.
For example, given [1, 2, 3] and 1, shift the array 1 to the left, returning [2, 3, 1].
"""


def shift_array(arr, n):
    new_arr = n % len(arr)


    return arr[new_arr:] + arr[:new_arr]