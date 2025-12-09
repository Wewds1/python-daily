"""
Most Frequent
Given an array of elements, return the element that appears most frequently.

There will always be a single most frequent element.





Passed:1. most_frequent(["a", "b", "a", "c"]) should return "a".
Passed:2. most_frequent([2, 3, 5, 2, 6, 3, 2, 7, 2, 9]) should return 2.
Passed:3. most_frequent([True, False, "False", "True", False]) should return False.
Passed:4. most_frequent([40, 20, 70, 30, 10, 40, 10, 50, 40, 60]) should return 40."""


from collections import Counter
def most_frequent(arr):

    counter = Counter(arr)


    return counter.most_common(1)[0][0]

print(most_frequent([True, False, "False", "True", False]))
