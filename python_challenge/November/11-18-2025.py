
"""
100 Characters
Welcome to the 100th Daily Coding Challenge!

Given a string, repeat its characters until the result is exactly 100 characters long.
If your repetitions go over 100 characters, trim the extra so it's exactly 100.
"""



def one_hundred(chars):
    new_char = ""
    while len(new_char) < 100:
        new_char = new_char + chars

    if len(new_char) > 100:
        return new_char[:100]

    return new_char
        
def one_hundred_again(chars):

    total = 100 // len(chars)
    remainder = 100 % len(chars)

    output = chars * total + chars[:remainder]

    return output

print((one_hundred("One Hundred ")))







