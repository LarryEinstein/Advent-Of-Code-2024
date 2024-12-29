import re

# Path to the input file
file_path = 'python\day3\day3_input.txt'

# Read the content of the file
with open(file_path, 'r') as file:
    content = file.read()

# Regular expression to find all instances of mul(x,y) with no spaces
pattern = r"mul\((\d+),(\d+)\)"

# Find all matches
matches = re.findall(pattern, content)

# Print the matches
print("Found instances of mul(x,y):")
total = 0
for x, y in matches:
    print(x)
    print(y)
    print(f"mul({x},{y})")
    total += int(x)*int(y)
print(total)

