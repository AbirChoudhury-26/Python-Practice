# Python program to find largest
# number in a list

# list of numbers
list1 = [10, 20, 4, 45, 99]

# sorting the list
list1.sort()

# printing the last element
print("Largest element is:", list1[-1])

# Python program to find largest
# number in a list

# List of numbers
list1 = [10, 20, 4, 45, 99]

# Printing the maximum element
print("Largest element is:", max(list1))

# Python program to find largest
# number in a list

# Without using Inbuilt Functions

def myMax(list1):

	# Assume first number in list is largest
	# initially and assign it to variable "max"
	max = list1[0]
# Now traverse through the list and compare
	# each number with "max" value. Whichever is
	# largest assign that value to "max'.
	for x in list1:
		if x > max:
			max = x

	# after complete traversing the list
	# return the "max" value
	return max


# Driver code
list1 = [10, 20, 4, 45, 99]
print("Largest element is:", myMax(list1))

# using a Dictionary

test_list = [4, 6, 4, 3, 3, 4, 3, 4, 6, 6]
k = 2
unique_elems = []
freq_dict = {}
output = []

# printing string
print("The original list : " + str(test_list))

for i in test_list:
	# Append in the unique element list
	if i not in unique_elems:
		unique_elems.append(i)
		freq_dict[i] = 1
	else:
		# increment the counter if element is duplicate
		freq_dict[i] += 1

	# Add in the output list only once
	if freq_dict[i] == k + 1:
		output.append(i)

print('The required elements : ', str(output))
