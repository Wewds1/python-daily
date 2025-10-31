"""
Given a string representing a variable name, convert it to "spooky case" using the following constraints:

Replace all underscores (_), and hyphens (-) with a tilde (~).
Capitalize the first letter of the string, and every other letter after that. Ignore the tilde character when counting. Make all other letters lowercase.
For example, given hello_world, return HeLlO~wOrLd.


"""


def spookify(boo):
    boo = boo.replace("_", "~").replace("-", "~")
    is_cap = True
    word = []
    for bo in boo:
        if bo.isalpha() and is_cap:
            word.append(bo.upper())
            is_cap = False
            
        elif bo.isalpha() and not is_cap:
            word.append(bo.lower())
            is_cap = True
        else:
            word.append(bo)

    return "".join(word)

print(spookify("TRICK-or-TREAT"))