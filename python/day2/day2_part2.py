def is_safe(report):
    # Determine the direction: increasing or decreasing
    first = report[0]
    last = report[-1]

    # If first == last, it can't be strictly increasing or decreasing
    if first == last:
        return False

    # Increasing if the last is greater than the first
    increasing = last > first

    # Check all adjacent differences
    for i in range(len(report) - 1):
        diff = report[i+1] - report[i]

        # Check if differences align with increasing/decreasing pattern
        if increasing and diff <= 0:
            return False
        if not increasing and diff >= 0:
            return False

        # Check difference magnitude constraint
        if not (1 <= abs(diff) <= 3):
            return False

    return True

def is_safe_with_one_removal(report):
    # Check if already safe without removal
    if is_safe(report):
        return True

    # Try removing each level once and check if the resulting report is safe
    for i in range(len(report)):
        modified_report = report[:i] + report[i+1:]
        if is_safe(modified_report):
            return True

    return False

# Reading and parsing the file
with open(r"python\day2\day2_input.txt", "rb") as file:
    data = file.read()

decoded_data = data.decode("utf-8")
rows = decoded_data.strip().split("\r\n")
data_as_rows = [list(map(int, row.split())) for row in rows]

# Count how many reports are safe with one possible removal
safe_count_with_removal = sum(is_safe_with_one_removal(row) for row in data_as_rows)
print(safe_count_with_removal)


def is_m_greater_than_n(m, n):
    if m > n:
        return True
    else:
        return False

# List of (m, n) pairs
pairs = [(3, 2), (1, 4), (5, 5), (6, 2), (3, 3)]

# Sum up all the True values
true_count = sum(is_m_greater_than_n(m, n) for m, n in pairs)

print("Number of times m > n:", true_count)
