import numpy as np

def count_word_occurrences(grid, word=False):
    n_rows, n_cols = grid.shape
    print(f"n_rows = {n_rows}")
    print(f"n_cols = {n_cols}")
    count = 0
    # Directions: (row_increment, col_increment)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]

    for row in range(n_rows):
        for col in range(n_cols):
            for delta_row, delta_col in directions:
                print(row, col, delta_row, delta_col)
    return count

def load_grid_from_file(file_path):
    """ Load the grid from the file """
    with open(file_path, 'r') as file:
        lines = file.read().splitlines()
        print(type(lines))
        print(lines[0][0])
    return np.array([list(line) for line in lines])

# Path to the input file
file_path = r'C:\Users\murra\Advent-Of-Code-2024\python\day4\scratch_input.txt'
grid = load_grid_from_file(file_path)

# Count occurrences
occurrences = count_word_occurrences(grid)
print(f"XMAS appears {occurrences} times.")



