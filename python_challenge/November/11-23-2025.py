"""
Character Count
Given a sentence string, return an array with a count of each character in alphabetical order.

Treat upper and lowercase letters as the same letter when counting.
Ignore numbers, spaces, punctuation, etc.
Return the count and letter in the format "letter count". For instance, "a 3".
All returned letters should be lowercase.
Do not return a count of letters that are not in the given string.
"""


def count_characters(sentence):

    count_chars = {}
    sentence = sentence.lower()

    for char in sentence:
        if char.isalpha():
            count_chars[char] = count_chars.get(char, 0) + 1

    sorted_char = sorted(count_chars)
    arr = [
        f"{char} {count_chars[char]}" for char in sorted_char
    ]

    return arr
             

    

print(count_characters('hello world'))