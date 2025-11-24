"""
Message Validator
Given a message string and a validation string, determine if the message is valid.

A message is valid if each word in the message starts with the corresponding letter in the validation string, in order.
Letters are case-insensitive.
Words in the message are separated by single spaces.
"""


def is_valid_message(message, validation):
    new_mess = message.lower().split(" ")

    if len(new_mess) != len(validation):
        return False

    for i in range(len(new_mess)):
        if new_mess[i][0] != validation.lower()[i]:
            return False
        
    return True
        


print(is_valid_message("The quick brown fox jumps over the lazy dog.", "TQBFJOTLD"))

"""
Passed:1. is_valid_message("hello world", "hw") should return True.
Passed:2. is_valid_message("ALL CAPITAL LETTERS", "acl") should return True.
Passed:3. is_valid_message("Coding challenge are boring.", "cca") should return False.
Passed:4. is_valid_message("The quick brown fox jumps over the lazy dog.", "TQBFJOTLD") should return True.
Passed:5. is_valid_message("The quick brown fox jumps over the lazy dog.", "TQBFJOTLDT") should return False.
"""