# python 3 code to print inverted star
# pattern 

# n is the number of rows in which
# star is going to be printed.
n=11

# i is going to be enabled to
# range between n-i t 0 with a
# decrement of 1 with each iteration.
# and in print function, for each iteration,
# ” ” is multiplied with n-i and ‘*’ is
# multiplied with i to create correct
# space before of the stars.
for i in range (n, 0, -1):
	print((n-i) * ' ' + i * '*')


# Recursive Method
	
def inverted_star_pattern_recursive(height):
	if height > 0:
		print("*" * height)
		inverted_star_pattern_recursive(height - 1)

height = 5
inverted_star_pattern_recursive(height)
