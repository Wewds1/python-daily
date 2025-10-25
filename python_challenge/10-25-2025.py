"""
Complementary DNA
Given a string representing a DNA sequence, return its complementary strand using the following rules:

DNA consists of the letters "A", "C", "G", and "T".
The letters "A" and "T" complement each other.
The letters "C" and "G" complement each other.
For example, given "ACGT", return "TGCA".
"""

def complementary_dna(strand):
    dna = []

    for char in strand:
        if char == 'A':
            dna.append('T')
        elif char == 'T':
            dna.append('A')
        elif char == 'C':
            dna.append('G')
        elif char == 'G':
            dna.append('C')
        else:
            dna.append(char)

    return ''.join(dna)


print(complementary_dna("ACGT"))