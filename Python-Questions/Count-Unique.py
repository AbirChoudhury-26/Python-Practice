# taking an input list
input_list = [1, 2, 2, 5, 8, 4, 4, 8]

# taking an input list
l1 = []

# taking an counter
count = 0

# traversing the array
for item in input_list:
	if item not in l1:
		count += 1
		l1.append(item)

# printing the output
print("No of unique items are:", count)

# Method-2

# importing Counter module
from collections import Counter


input_list = [1, 2, 2, 5, 8, 4, 4, 8]

# creating a list with the keys
items = Counter(input_list).keys()
print("No of unique items in the list are:", len(items))
