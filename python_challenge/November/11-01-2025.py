"""
Given a message string, a secret key string, and a signature number, determine if the signature is valid using this encoding method:

Letters in the message and secret key have these values:
a to z have values 1 to 26 respectively.
A to Z have values 27 to 52 respectively.
All other characters have no value.
Compute the signature by taking the sum of the message plus the sum of the secret key.
For example, given the message "foo" and the secret key "bar", the signature would be 57:
"""


def verify(message, key, signature):
    chars = {
        **{chr(i + 96): i for i in range(1, 27)},
        **{chr(i + 64): i + 26 for i in range(1, 27)}
    }

    if sum(chars.get(c, 0) for c in message) + sum(chars.get(c, 0) for c in key) != signature:
        return False

    return True


print(verify("foo", "bar", 57)) 
print(verify("Hello, World!", "SecretKey", 319))  
print(verify("freeCodeCamp", "Rocks", 238))