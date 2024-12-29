import re

# Path to the input file
file_path = 'python/day3/day3_input.txt'

# Read the content of the file
with open(file_path, 'r') as file:
    content = file.read()

# Clean the content to remove unnecessary characters and normalize spacing
content = re.sub(r'\s+', '', content)  # remove spaces

# Regex pattern to match mul, do, and don't instructions
pattern = r"(mul\((\d+),(\d+)\)|do\(\)|don't\(\))"

# Find all matches including mul, do, and don't
instructions = re.findall(pattern, content)

# Initialize the total and the state of whether mul is enabled
total = 0
mul_enabled = True

# Iterate over each instruction
for full_match, x, y in instructions:
    if full_match.startswith("do()"):
        mul_enabled = True
    elif full_match.startswith("don't()"):
        mul_enabled = False
    elif full_match.startswith("mul"):
        if mul_enabled:
            total += int(x) * int(y)

print(total)
