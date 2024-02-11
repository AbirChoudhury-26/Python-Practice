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

# This code is contributed by virentanti16
