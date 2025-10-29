"""
Given two strings, determine how many times the second string appears in the first.

The pattern string can overlap in the first string. For example, "aaa" contains "aa" twice.
 The first two a's and the second two.

"""


def count(text, parameter):

    param_count = 0
    for i in range(len(text) - len(parameter) + 1):
        if text[i:i+len(parameter)] == parameter:
            param_count += 1


    return param_count


print(count("aaa", "aa"))

