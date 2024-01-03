# A Python list comprehension consists of brackets containing the expression, which is executed for each element along with the for loop to iterate over each element in the Python list. 

# Example-1

numbers = [12, 13, 14,] 
doubled = [x *2 for x in numbers] 
print(doubled)

# Example-2 

list = [i for i in range(11) if i % 2 == 0] 
print(list)

# Example-3:

# Matrix using List Comprehension
#In this example, we are assigning integers 0 to 2 to 3 rows of the matrix and printing it using List Comprehension.

matrix = [[j for j in range(3)] for i in range(3)] 
	
print(matrix)



# Difference Bewteen For Loop &  List Comprehension

# For Loop:
List = [] 
for character in 'Geeks 4 Geeks!': 
	List.append(character) 

print(List) 


# List Comprehension

# Using list comprehension to iterate through loop 
List = [character for character in 'Geeks 4 Geeks!']  
print(List) 



#Nested List Comprehensions
#Nested List Comprehensions are nothing but a list comprehension within another list comprehension which is quite similar to nested for loops.

matrix = [] 

for i in range(3): 

	# Append an empty sublist inside the list 
	matrix.append([]) 

	for j in range(5): 
		matrix[i].append(j) 

print(matrix) 

# Lanbda function 

# using lambda to print table of 10 
numbers = list(map(lambda i: i*10, [i for i in range(1, 6)])) 

print(numbers) 


# Conditional Statements in List Comprehension

lis = ["Even number" if i % 2 == 0
	else "Odd number" for i in range(8)] 
print(lis) 


# Reverse each string in tuple 
List = [string[::-1] for string in ('Geeks', 'for', 'Geeks')] 

# Display list 
print(List) 


# Nested if-else

lis = [num for num in range(100) 
	if num % 5 == 0 if num % 10 == 0] 
print(lis)
