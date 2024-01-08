# Python3 code to demonstrate working of 
# Extract elements with Frequency greater than K
# Using count() + loop

# initializing list
# test_list = [4, 6, 4, 3, 3, 4, 3, 7, 8, 8]

# # printing string
# print("The original list : " + str(test_list))

# # initializing K 
# K = 2

# res = [] 
# for i in test_list: 
	
# 	# using count() to get count of elements
# 	freq = test_list.count(i) 
	
# 	# checking if not already entered in results
# 	if freq > K and i not in res: 
# 		res.append(i)

# # printing results 
# print("The required elements : " + str(res))

# Method-2

# Python3 code to demonstrate working of 
# Extract elements with Frequency greater than K
# Using list comprehension + Counter()
from collections import Counter

# initializing list
test_list = [4, 6, 4, 3, 3, 4, 3, 7, 8, 8]

# printing string
print("The original list : " + str(test_list))

# initializing K 
K = 2

# using list comprehension to bind result
res = [ele for ele, cnt in Counter(test_list).items() if cnt > K]

# printing results 
print("The required elements : " + str(res))


# Method-3

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

# Method-4

# Python3 code to demonstrate working of
# Extract elements with Frequency greater than K
import operator as op

# initializing list
test_list = [4, 6, 4, 3, 3, 4, 3, 7, 8, 8]

# printing string
print("The original list : " + str(test_list))

# initializing K
K = 2
unique_elements = set(test_list)
res = []
for i in unique_elements:

	# using operatorcountOf() to get count of elements
	if op.countOf(test_list, i) > K:
		res.append(i)

# printing results
print("The required elements : " + str(res))
