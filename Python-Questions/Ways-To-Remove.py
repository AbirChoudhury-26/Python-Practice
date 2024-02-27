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


