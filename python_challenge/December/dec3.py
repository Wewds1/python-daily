"""
Permutation Count
Given a string, return the number of distinct permutations that can be formed from its characters.

A permutation is any reordering of the characters in the string.
Do not count duplicate permutations.
If the string contains repeated characters, repeated arrangements should only be counted once.
The string will contain only letters (A-Z, a-z).
For example, given "abb", return 3 because there's three unique ways to arrange the letters: "abb", "bab", and "bba".
"""

import math
from collections import Counter

def count_permutations(s):

    n = len(s)
    counter = Counter(s)

    num = math.factorial(n)

    den = 1

    for c in counter.values():
        den *= math.factorial(c)

    return num // den
            

    
        
print(count_permutations("abb"))
# print(count_permutations("abc"))
# print(count_permutations("racecar"))


"""
1. count_permutations("abb") should return 3.
Passed:2. count_permutations("abc") should return 6.
Passed:3. count_permutations("racecar") should return 630.
Passed:4. count_permutations("freecodecamp") should return 39916800.
"""