# Using Merge Method:

""" we can use “|” operator to merge two dictionaries. It is a very convenient method to merge dictionaries."""

# code
# Python code to merge dict using a single 
# expression 
def Merge(dict1, dict2): 
	res = dict1 | dict2
	return res 
	
# Driver code 
dict1 = {'x': 10, 'y': 8} 
dict2 = {'a': 6, 'b': 4} 
dict3 = Merge(dict1, dict2) 
print(dict3)



# Using Keys and Loops

"""
For each key:
If the key already exists in dict1, update the value in dict1 with the value from dict2.
If the key does not exist in dict1, add the key-value pair from dict2 to dict1.
Return the modified dict1.
"""

# code
# Python code to merge dictionary
def Merge(dict1, dict2):
	for i in dict2.keys():
		dict1[i]=dict2[i]
	return dict1
	
# Driver code
dict1 = {'x': 10, 'y': 8}
dict2 = {'a': 6, 'b': 4}
dict3 = Merge(dict1, dict2)
print(dict3)

# This code is contributed by Bhavya Koganti

