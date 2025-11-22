"""
LCM Calculation
Given two integers, return the least common multiple (LCM) of the two numbers.

The LCM of two numbers is the smallest positive integer that is a multiple of both numbers. For example, given 4 and 6, return 12 because:

Multiples of 4 are 4, 8, 12 and so on.
Multiples of 6 are 6, 12, 18 and so on.
12 is the smallest number that is a multiple of both.
"""


def lcm(a, b):

    higher = a if a > b else b
    ans = 0

    for i in range(1, higher+1):
        ans = a * i
        if ans % b == 0:
            break
    return ans

print(lcm(10,10))