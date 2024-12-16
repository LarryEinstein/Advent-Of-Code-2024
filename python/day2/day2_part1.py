def is_safe(report):
    # Determine the direction: increasing or decreasing
    first = report[0]
    last = report[-1]

    if first == last:
        # If the start and end are the same, it can't be strictly increasing or decreasing
        return False

    # Increasing if the last is greater than the first
    increasing = last > first

    # Check all adjacent differences
    for i in range(len(report) - 1):
        diff = report[i+1] - report[i]

        # If we expect increasing, diff should be positive; if decreasing, diff should be negative
        if increasing and diff <= 0:
            return False
        if not increasing and diff >= 0:
            return False

        # Check if the absolute difference is between 1 and 3
        if not (1 <= abs(diff) <= 3):
            return False

    return True

# Reading and parsing the file
with open(r"python\day2\day2_input.txt", "rb") as file:
    data = file.read()

decoded_data = data.decode("utf-8")

# It's often safer to split on any newline character, but if you know it's \r\n, you can use that.
rows = decoded_data.strip().split("\r\n")

data_as_rows = [list(map(int, row.split())) for row in rows]

# Count how many reports are safe
safe_count = sum(is_safe(row) for row in data_as_rows)
print(safe_count)  # This will print how many reports are safe.
