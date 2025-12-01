"""
Ball Trajectory
Today's challenge is inspired by the video game Pong, which was released November 29, 1972.

Given a matrix (array of arrays) that includes the location of the ball (2), and the previous location of the ball (1), return the matrix indices for the next location of the ball.

The ball always moves in a straight line.
The movement direction is determined by how the ball moved from 1 to 2.
The edges of the matrix are considered walls. If the balls hits a:
top or bottom wall, it bounces by reversing its vertical direction.
left or right wall, it bounces by reversing its horizontal direction.
corner, it bounces by reversing both directions.
"""


def get_next_location(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    # Find prev and current
    for row in range(rows):
        for col in range(cols):
            if matrix[row][col] == 1:
                prev_row, prev_col = row, col
            if matrix[row][col] == 2:
                curr_row, curr_col = row, col

    # Direction
    dir_row = curr_row - prev_row
    dir_col = curr_col - prev_col

    # Next Position Computation
    next_row = curr_row + dir_row
    next_col = curr_col + dir_col

    # Bounce vertical
    if next_row < 0 or next_row >= rows:
        dir_row = -dir_row
        next_row = curr_row + dir_row

    # Bounce horizontal
    if next_col < 0 or next_col >= cols:
        dir_col = -dir_col
        next_col = curr_col + dir_col

    return [next_row, next_col]


"""
Passed:1. get_next_location([[0,0,0,0], [0,0,0,0], [0,1,2,0], [0,0,0,0]]) should return [2, 3].
Passed:2. get_next_location([[0,0,0,0], [0,0,1,0], [0,2,0,0], [0,0,0,0]]) should return [3, 0].
Passed:3. get_next_location([[0,2,0,0], [1,0,0,0], [0,0,0,0], [0,0,0,0]]) should return [1, 2].
Passed:4. get_next_location([[0,0,0,0], [0,0,0,0], [2,0,0,0], [0,1,0,0]]) should return [1, 1].
Passed:5. get_next_location([[0,0,0,0], [0,0,0,0], [0,0,1,0], [0,0,0,2]]) should return [2, 2].
"""