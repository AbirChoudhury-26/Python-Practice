# This code gets the index in the 
# list of objects by attribute. 

class X: 
	def __init__(self,val): 
		self.val = val 
		
def getIndex(li,target): 
	for index, x in enumerate(li): 
		if x.val == target: 
			return index 
	return -1

# Driver code 
li = [1,2,3,4,5,6] 

# Converting all the items in 
# list to object of class X 
a = list() 
for i in li: 
	a.append(X(i)) 
	
print(getIndex(a,3)) 

# List of Objects

# Python3 code here creating class
class geeks:
	def __init__(self, name, roll):
		self.name = name
		self.roll = roll

# creating list
list = []

# appending instances to list
list.append(geeks('Akash', 2))
list.append(geeks('Deependra', 40))
list.append(geeks('Reaper', 44))
list.append(geeks('veer', 67))

# Accessing object value using a for loop
for obj in list:
	print(obj.name, obj.roll, sep=' ')

print("")
# Accessing individual elements
print(list[0].name)
print(list[1].name)
print(list[2].name)
print(list[3].name)
