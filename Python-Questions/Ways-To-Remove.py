# Method-1 :  Using remove() 

# # Python code to demonstrate
# # element removal in list
# # using remove() method

# test_list1 = [1, 3, 4, 6, 3]
# test_list2 = [1, 4, 5, 4, 5]

# # Printing initial list
# print("The list before element removal is : "
# 	+ str(test_list1))

# # using remove() to remove list element3
# test_list1.remove(3)

# # Printing list after removal
# # only first occurrence deleted
# print("The list after element removal is : "
# 	+ str(test_list1))


# Method-2 :  Using set.disard()

# Python code to demonstrate
# element removal in list
# using discard() method

test_list1 = [1, 3, 4, 6, 3]
test_list2 = [1, 4, 5, 4, 5]

# Printing initial list
print("The list before element removal is : "
	+ str(test_list2))

# using discard() to remove list element 4
test_list2 = set(test_list2)
test_list2.discard(4)

test_list2 = list(test_list2)

# Printing list after removal
# removes element as distinct initially
print("The list after element removal is : "
	+ str(test_list2))


# Method-3 : Using Lambda Method

# Python code to demonstrate
# element removal in list
# using filter() + Lambda function

# test_list1 = [1, 3, 4, 6, 3]
# test_list2 = [1, 4, 5, 4, 5]

# # Printing initial list
# print("The list before element removal is : "
# 	+ str(test_list1))

# # using filter() + Lambda function
# # to remove list element 3
# test_list1 = list(filter(lambda x: x != 3, test_list1))

# # Printing list after removal
# print("The list after element removal is : "
# 	+ str(test_list1))

# Method-4 : Using List in Comprehension

# Python code to demonstrate
# element removal in list
# using List Comprehension

test_list1 = [1, 3, 4, 6, 3]
test_list2 = [1, 4, 5, 4, 5]

# Printing initial list
print("The list before element removal is : "
	+ str(test_list2))


# using List Comprehension
# to remove list element 4
test_list2 = [x for x in test_list2 if x != 4]

# Printing list after removal
print("The list after element removal is : "
	+ str(test_list2))


# Method-5 : Using Pop
"""
Approach:

Define a list named test_list1 containing some elements.
Print the initial list using the print() function.
Assign the value 4 to the variable rmv_element. This value represents the element that we want to remove from the list.
Use the if statement to check if the rmv_element is present in the list test_list1.
If the element is present, use the pop() method to remove the first occurrence of the element from the list. The index() method is used to find the index of the element to be removed.
Print the list after removal using the print() function. 

"""

# Python code to demonstrate
# element removal in list
# using pop() method

test_list1 = [1, 3, 4, 6, 3]

# Printing initial list
print("The list before element removal is : "
	+ str(test_list1))

rmv_element = 4

# using pop()
# to remove list element 4
if rmv_element in test_list1:
	test_list1.pop(test_list1.index(rmv_element))

# Printing list after removal
print("The list after element removal is : "
	+ str(test_list1))


# Method-6

""" Using Recursion"""

def remove_element(start, oldlist, newlist, element):
	if start == len(oldlist):
		return newlist # base condition
	if oldlist[start] == element:
		pass # checking if element is oldlist pass
	else:
		newlist.append(oldlist[start]) # appending oldlist element to new list
	return remove_element(start+1, oldlist, newlist, element)


# Driver code
newlist = [1, 2, 3, 29, 2, 13, 421, 31]
start = 0
element = 2 # element want to remove
print('The list Before removal: ', newlist)
print('The list After removal: ', remove_element(start, newlist, [], element))

