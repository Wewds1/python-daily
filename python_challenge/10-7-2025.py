"""
In day four of Space Week, you are given a matrix of numbers (an array of arrays),
representing potential landing spots for your rover. Find the safest landing spot based on the following rules:

Each spot in the matrix will contain a number from 0-9, inclusive.
Any 0 represents a potential landing spot.
Any number other than 0 is too dangerous to land. The higher the number, the more dangerous.
The safest spot is defined as the 0 cell whose surrounding cells (up to 4 neighbors, ignore diagonals) 
have the lowest total danger.
Ignore out-of-bounds neighbors (corners and edges just have fewer neighbors).
Return the indices of the safest landing spot. There will always only be one safest spot.
For instance, given:

[
  [1, 0],
  [2, 0]
]
Return [0, 1], the indices for the 0 in the first array.
"""


def find_landing_spot(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    safest_spot = None
    lowest_danger = float('inf')

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 0:
                latest_danger = 0

                closest = [
                    (i - 1, j),
                    (i + 1, j),
                    (i, j - 1),
                    (i, j + 1 )]
                
                for close_row, close_col in closest:
                    if 0 <= close_row < rows and 0 <= close_col < cols:
                        latest_danger += matrix[close_row][close_col]

                if latest_danger < lowest_danger:
                    lowest_danger = latest_danger
                    safest_spot = i, j
    return list(safest_spot)