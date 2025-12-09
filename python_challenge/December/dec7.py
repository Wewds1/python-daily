"""
String Compression
Given a string sentence, return a compressed version of the sentence where consecutive duplicate words are replaced by the word followed with the number of times it repeats in parentheses.

Only consecutive duplicates are compressed.
Words are separated by single spaces.
For example, given "yes yes yes please", return "yes(3) please".
"""

from collections import Counter
def compress_string(sentence):
    splits = sentence.split(" ")
    counter = Counter(splits)
    word = ""
    for count in counter:
        if counter[count] > 1:
            word += f"{count}({counter[count]}) "

        else:
            word += f"{count} "
        

    return word.rstrip()

print(compress_string("yes yes yes please"))


"""
. compress_string("yes yes yes please") should return "yes(3) please".
Passed:2. compress_string("I have have have apples") should return "I have(3) apples".
Passed:3. compress_string("one one three and to the the the the") should return "one(2) three and to the(4)".
Passed:4. compress_string("route route route route route route tee tee tee tee tee tee") should return "route(6) tee(6)".
"""