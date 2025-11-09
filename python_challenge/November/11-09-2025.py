"""
Word Search
Given a matrix (an array of arrays) of single letters and a word to find, return the start and end indices of the word in the matrix.

The given matrix will be filled with all lowercase letters (a-z).
The word to find will always be in the matrix exactly once.
The word to find will always be in a straight line in one of these directions:
left to right
right to left
top to bottom
bottom to top
For example, given the matrix:

[
  ["a", "c", "t"],
  ["t", "a", "t"],
  ["c", "t", "c"]
]
And the word "cat", return:

[[0, 1], [2, 1]]
Where [0, 1] are the indices for the "c" (start of the word), and [2, 1] are the indices for the "t" (end of the word).
"""

def find_word(matrix, word):
    rows = len(matrix)
    cols = len(matrix[0])

    #left to right
    for i in range(rows):
        row_word = "".join(matrix[i])
        if word in row_word:
            start = row_word.index(word)
            end = start + len(word) -1
            return [[i,start], [i, end]]
    #right to left
    for i in range(rows):
        row_word = "".join(matrix[i][::-1])
        if word in row_word:
            start = row_word.index(word)
            end = start + len(word) - 1
            start_col = cols - 1 - start
            end_col = cols - 1 - end
            return [[i, start_col], [i, end_col]]
    #top to bottom
    for j in range(cols):
        col_word = "".join(matrix[i][j] for i in range(rows))
        if word in col_word:
            start = col_word.index(word)
            end = start + len(word) - 1
            return [[start, j], [end, j]]

    #bottom to top
    for j in range(cols):
        col_word = "".join(matrix[i][j] for i in range(rows))[::-1]
        if word in col_word:
            start = col_word.index(word)
            end = start + len(word) -1
            start_row = rows - 1 - start
            end_row = rows - 1 - end
            return [[start_row, j], [end_row, j]]


print(find_word([["f", "x", "o", "x"], ["o", "x", "o", "f"], ["f", "o", "f", "x"], ["f", "x", "x", "o"]], "fox"))
