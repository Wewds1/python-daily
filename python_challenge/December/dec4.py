"""
Symmetric Difference
Given two arrays, return a new array containing the symmetric difference of them.

The symmetric difference between two sets is the set of values that appear in either set, but not both.
Return the values in the order they first appear in the input arrays.
"""

def difference(arr1, arr2):

    arr = list(set(arr1) - set(arr2) | set(arr2) - set(arr1))
    new = [array for array in arr1 + arr2 if array in arr]

    return new

print(difference([1, 2, 3], [3, 4, 5]))
print(difference([1, 3, 5, 7, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9]))


"""
Passed:1. difference([1, 2, 3], [3, 4, 5]) should return [1, 2, 4, 5].
Passed:2. difference(["a", "b"], ["c", "b"]) should return ["a", "c"].
Passed:3. difference([1, "a", 2], [2, "b", "a"]) should return [1, "b"].
Passed:4. difference([1, 3, 5, 7, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9]) should return [2, 4, 6, 8].
"""