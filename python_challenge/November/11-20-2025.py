"""
longest Word

Given a sentence string, return the longest word in the sentence.

Words are separated by a single space.
Only letters (a-z, case-insensitive) count toward the word's length.
If there are multiple words with the same length, return the first one that appears.
Return the word as it appears in the given string, with punctuation removed.
"""

def longest_word(sentence):
    s = sentence.replace(".","").replace("?","").replace("!","").replace("'","").split(" ")
    word = ""
    for i in s:
        if i.isalpha():
            if len(i) > len(word):
                word = i

            
            

    return word

print(longest_word("Hello coding challenge"))