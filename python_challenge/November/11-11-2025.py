"""
Vowels and Consonants
Given a string, return an array with the number of vowels and number of consonants in the string.

Vowels consist of a, e, i, o, u in any case.
Consonants consist of all other letters in any case.
Ignore any non-letter characters.
For example, given "Hello World", return [3, 7].
"""


def count(s):
    vowels = "AEIOUaeiou"
    vowel_count = 0
    cons_count = 0

    for i in s:
        if i.isalpha() and i in vowels :
            vowel_count += 1
        elif i.isalpha():
            cons_count += 1

    return [vowel_count, cons_count]


print(count("hatdog"))



"""
def count(s):
    vowels = set("aeiouAEIOU")
    vowel_count = sum(1 for ch in s if ch in vowels)
    cons_count = sum(1 for ch in s if ch.isalpha() and ch not in vowels)
    return [vowel_count, cons_count]

print(count("hatdog"))
"""