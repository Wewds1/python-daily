"""
Matrix Builder
Given two integers (a number of rows and a number of columns), return a matrix (an array of arrays) filled with zeros (0) of the given size.

For example, given 2 and 3, return:
[
  [0, 0, 0],
  [0, 0, 0]
]
"""

def build_matrix(rows, cols):
    return [[0 for c in range(cols)] for r in range(rows)]



"""
Perfect Square
Given an integer, determine if it is a perfect square.

A number is a perfect square if you can multiply an integer by itself to achieve the number. For example, 9 is a perfect square because you can multiply 3 by itself to get it.

"""

import math
def is_perfect_square(n):
    if n < 0:
        return False
    if math.sqrt(n) % 1 == 0:
        return True

    return False

def is_perfect_square_new(n):

    if n < 0:
        return False
    number = int(n**0.5)

    if number * number == n:
        return True

    else:
        return False


print(is_perfect_square(9))


