# Python program to create a list of tuples
# from given list having number and
# its cube in each tuple

# creating a list
list1 = [1, 2, 5, 6]

# using list comprehension to iterate each
# values in list and create a tuple as specified
res = [(val, pow(val, 3)) for val in list1]

# print the result
print(res)


# Method-2

# Python program to create a list of tuples
# from given list having number and
# its cube in each tuple

# creating a list
list1 = [1, 2, 5, 6]

# using list comprehension to iterate each
# values in list and create a tuple as specified
res = [(val, val**3) for val in list1]

# print the result
print(res)



# Method-3

"""
1. Create an empty list named res to store the result.
2. Use a for loop to iterate over each value in list1.
3. Inside the for loop, create a tuple named tup that contains the current value from list1 and its cube (val**3).
4. Append the tup tuple to the res list.
5. After the for loop completes, print the res list that contains tuples with each value from list1 and its cube.
"""

# creating a list
list1 = [1, 2, 5, 6]

# creating an empty list to store the result
res = []

# iterating through each value in the list
for val in list1:
	# creating a tuple of the value and its cube
	tup = (val, val**3)
	# adding the tuple to the result list
	res.append(tup)

# print the result
print(res)
