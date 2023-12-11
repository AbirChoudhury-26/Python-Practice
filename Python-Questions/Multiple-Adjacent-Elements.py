# Python3 code to demonstrate working of 
# Adjacent element multiplication 
# using for loop

# initialize tuple 
# test_tup = (1, 5, 7, 8, 10) 

# # printing original tuple 
# print("The original tuple : " + str(test_tup)) 

# # initialize an empty list to store the result
# res = []

# # iterate over the tuple and perform multiplication of adjacent elements
# for i in range(len(test_tup) - 1):
# 	res.append(test_tup[i] * test_tup[i+1])

# # convert the list to a tuple
# res = tuple(res)

# # printing result 
# print("Resultant tuple after multiplication : " + str(res)) 

# Using Lamda Method
# Python3 code to demonstrate working of 
# Adjacent element multiplication 
# using tuple() + map() + lambda 

# initialize tuple 
test_tup = (1, 5, 7, 8, 10) 

# printing original tuple 
print("The original tuple : " + str(test_tup)) 

# Adjacent element multiplication 
# using tuple() + map() + lambda 
res = tuple(map(lambda i, j : i * j, test_tup[1:], test_tup[:-1])) 

# printing result 
print("Resultant tuple after multiplication : " + str(res)) 


