# Method-1 

""" Using None"""

# Python3 code to demonstrate 
# list slicing from K to end
# using None

# initializing list
test_list = [5, 6, 2, 3, 9]

# printing original list
print ("The original list is : " + str(test_list))

# index to begin slicing
K = 2

# using None 
# to perform list slicing from K to end
res = test_list[K : None]

# printing result 
print ("The sliced list is : " + str(res))


# Method-2

""" Method #2 : Leaving the last element empty """

# Python3 code to demonstrate 
# list slicing from K to end
# without specifying last element 

# initializing list
test_list = [5, 6, 2, 3, 9]

# printing original list
print ("The original list is : " + str(test_list))

# index to begin slicing
K = 2

# without specifying last element 
# to perform list slicing from K to end
res = test_list[K :]

# printing result 
print ("The sliced list is : " + str(res))


# Method-3

""" Method #3 : Using itertools """

from itertools import islice

# Initialize the list
test_list = [5, 6, 2, 3, 9]

# Index to begin slicing
K = 2

# Use islice() to slice the list from the Kth element to the last element
res = list(islice(test_list, K, None))

print(res) # [2, 3, 9]


# Method-4

""" Using a for loop to iterate over the list and append elements to a new list starting from the K index."""


# Python3 code to demonstrate 
# list slicing from K to end
# without specifying last element 

# initializing list
test_list = [5, 6, 2, 3, 9]

# printing original list
print ("The original list is : " + str(test_list))

# index to begin slicing
K = 2

# using for loop to slice list from K to end
res = []
for i in range(K, len(test_list)):
	res.append(test_list[i])

# printing result 
print ("The sliced list is : " + str(res))