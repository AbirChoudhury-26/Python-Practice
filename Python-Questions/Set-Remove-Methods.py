# 1st Approach- Using Pop method- Select Min among the all and pops out

def Remove(initial_set):
	while initial_set:
		initial_set.pop()
		print(initial_set)


initial_set = set([12, 10, 13, 15, 8, 9])
Remove(initial_set)

# Using 2nd Approach- Remove The Max among all and remove it .

my_set = set([12, 10, 13, 15, 8, 9])


while my_set:
	my_set.discard(max(my_set))
	print(my_set)

# Using 3rd Approach- Remove elements from the set in order of which they are present
	
	my_set = set([12, 10, 13, 15, 8, 9])

for i in range(len(my_set)):
	my_set.remove(next(iter(my_set)))
	print(my_set)
	
	
