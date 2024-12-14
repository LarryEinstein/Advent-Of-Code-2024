import numpy as np

# Lists to store the numbers from each column
numbers_col1 = []
numbers_col2 = []


with open("python/day1_input.txt", "r") as file:
    for line in file:
        # Split each line on whitespace and convert to integers
        num1, num2 = map(int, line.strip().split())
        numbers_col1.append(num1)
        numbers_col2.append(num2)


# Convert lists to numpy arrays
list1 = np.array(numbers_col1)
list2 = np.array(numbers_col2)

list1_length = len(list1)

list2_length = len(list2)

if list1_length != list2_length:
    print("the list lengths don't match!")

sorted_list1 = np.sort(list1)

sorted_list2 = np.sort(list2)

difference1=sorted_list1[0]-sorted_list2[0]
difference2=sorted_list1[1]-sorted_list2[1]

difference = 0
difference_sum = 0
for i in range(0, list1_length):
    difference += abs(sorted_list1[i]- sorted_list2[i])
    
print(f"total difference =", {difference})