import numpy as np

def find_word_in_direction(grid, start_row, start_col, delta_row, delta_col, word):
    """ Check for the word in a specific direction """
    n_rows, n_cols = grid.shape
    end_row = start_row + delta_row * (len(word) - 1)
    end_col = start_col + delta_col * (len(word) - 1)

    # Ensure the end position is within the grid boundaries
    if 0 <= end_row < n_rows and 0 <= end_col < n_cols:
        current_word = ''
        for i in range(len(word)):
            row = start_row + i * delta_row
            col = start_col + i * delta_col
            current_word += grid[row, col]
        if current_word == word:
            return 1
    return 0

def count_word_occurrences(grid, word):
    n_rows, n_cols = grid.shape
    count = 0
    # Directions: (row_increment, col_increment)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]

    for row in range(n_rows):
        for col in range(n_cols):
            for delta_row, delta_col in directions:
                count += find_word_in_direction(grid, row, col, delta_row, delta_col, word)
    return count

def load_grid_from_file(file_path):
    """ Load the grid from the file """
    with open(file_path, 'r') as file:
        lines = file.read().splitlines()
        print(type(lines))
        print(lines[0][0])
    return np.array([list(line) for line in lines])

# Path to the input file
file_path = r'C:\Users\murra\Advent-Of-Code-2024\python\day4\day4_input.txt'
grid = load_grid_from_file(file_path)
word = "XMAS"

# Count occurrences
occurrences = count_word_occurrences(grid, word)
print(f"XMAS appears {occurrences} times.")
