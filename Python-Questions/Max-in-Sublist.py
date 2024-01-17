# # Initialising List
# a = [[10, 13, 454, 66, 44], [10, 8, 7, 23]]
# lis = []

# # find max in list
# for p in a:
# 	lis.append(max(p))

# # Printing max
# print(lis)


# Initialising List
# a = [[10, 13, 454, 66, 44], [10, 8, 7, 23]]

# # find max in list
# b = [max(p) for p in a]

# # Printing max
# print(b)

# Initialising List
# a = [[10, 13, 454, 66, 44], [10, 8, 7, 23]]

# # find max in list
# ans = list(map(max, a))

# # Printing max
# print(ans)

# Get maximum number in each subist using Sort method

# Initialising List
# a = [[10, 13, 454, 66, 44], [10, 8, 7, 23]]
# lis = []

# # find max in list
# for p in a:
# 	p.sort()
# 	lis.append(p[-1])

# # Printing max
# print(lis)

# Max using MAP-Lambda Function

# First define a list of sublists a. Then, use the map() function to apply a lambda function to each sublist in a. The lambda function simply finds the maximum value in the sublist using the built-in max() function.
#Finally, we convert the result of the map() function to a list using the list() function, and assign it to the variable lis. Finally, we print the resulting list of maximum values

# define a list of sublists
a = [[10, 13, 454, 66, 44], [10, 8, 7, 23]]

# use the map function to apply a lambda function to each sublist in a
lis = list(map(lambda x: max(x), a))

# print the resulting list of maximum values
print(lis)

