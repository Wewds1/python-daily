"""

Fingerprint Test
Given two strings representing fingerprints, determine if they are a match using the following rules:

Each fingerprint will consist only of lowercase letters (a-z).
Two fingerprints are considered a match if:
They are the same length.
The number of differing characters does not exceed 10% of the fingerprint length.
"""

def is_match(fingerprint_a, fingerprint_b):
    if len(fingerprint_a) != len(fingerprint_b):
        return False

    length = len(fingerprint_a)

    differences = sum(1 for a, b in zip(fingerprint_a, fingerprint_b) if a != b)

    allowed_diff = length * 0.10

    return differences <= allowed_diff


print(is_match("helloworld", "jelloworlds"))
