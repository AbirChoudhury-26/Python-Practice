# Python program to check 
# if two lists have at-least 
# one element common
# using set and property

def common_member(a, b):
	#  Covertion of List into Set
	a_set = set(a)
	b_set = set(b)
	if (a_set & b_set): # Perform and Operation between sets to find the common
		return True
	else:
		return False
		

a = [1, 2, 3, 4, 5]
b = [5, 6, 7, 8, 9]
print(common_member(a, b))

a =[1, 2, 3, 4, 5]
b =[6, 7, 8, 9]  
print(common_member(a, b))



#  set’s intersection inbuilt function. a_set.intersection(b_set) returns a positive integer if there is at least one element in common, else it returns 0

# Python program to check 
# if two lists have at-least 
# one element common
# using set intersection

def common_member(a, b):
	a_set = set(a)
	b_set = set(b)
	if len(a_set.intersection(b_set)) > 0:
		return(True) 
	return(False) 

a = [1, 2, 3, 4, 5]
b = [5, 6, 7, 8, 9]
print(common_member(a, b))

a =[1, 2, 3, 4, 5]
b =[6, 7, 8, 9]
print(common_member(a, b))

