import numpy as np

example_list1 = [3, 4, 2, 1, 3, 3]
example_list2 = [4, 3, 5, 3, 9, 3]

count_of_3 = example_list1.count(3)

sorted_list1 = np.sort(example_list1)
sorted_list2 = np.sort(example_list2)

deduped_example_list1 = list(dict.fromkeys(sorted_list1))
print(deduped_example_list1)

count_from_dict_thing = deduped_example_list1.count(3)


sorted_list2 = list(sorted_list2)

difference_scalar = 0
for i in deduped_example_list1:
    if i in sorted_list2:
        m = sorted_list2.count(i)
        difference_scalar += i*m
    else:
        difference_scalar += 0

print(f"Example scalar dif", difference_scalar)

# ---------------------------------------------------------------------------------------------- #

# Lists to store the numbers from each column
numbers_col1 = []
numbers_col2 = []

with open("python\day1\day1_input.txt", "r") as file:
    for line in file:
        # Split each line on whitespace and convert to integers
        num1, num2 = map(int, line.strip().split())
        numbers_col1.append(num1)
        numbers_col2.append(num2)

# Convert lists to numpy arrays
list1 = np.array(numbers_col1)
list2 = np.array(numbers_col2)

sorted_list1 = np.sort(list1)
sorted_list2 = np.sort(list2)

deduped_example_list1 = list(dict.fromkeys(sorted_list1))


sorted_list2 = list(sorted_list2)

difference_scalar = 0
for i in deduped_example_list1:
    if i in sorted_list2:
        m = sorted_list2.count(i)
        difference_scalar += i*m
    else:
        difference_scalar += 0

print(f"final difference for advent = ",difference_scalar)
