"""
Given a string representing a hexadecimal number (base 16), return its decimal (base 10) value as an integer.

Hexadecimal is a number system that uses 16 digits:

0-9 represent values 0 through 9.
A-F represent values 10 through 15.
Here's a partial conversion table:

Hexadecimal	Decimal
0	0
1	1
...	...
9	9
A	10
...	...
F	15
10	16
...	...
9F	159
A0	160
...	...
FF	255
100	256
The string will only contain characters 0–9 and A–F.
"""


def hex_to_decimal(hex):
    hex = hex.upper()
    hex_list = "0123456789ABCDEF"
    val = 0

    for i, digit in enumerate(reversed(hex)):
        value = hex_list.index(digit)
        val += value * (16 ** i)

    return val
print(hex_to_decimal("A"))