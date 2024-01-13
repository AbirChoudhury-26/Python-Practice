# Using Slicing Method

def reverseArrayUptoK(input, k):
	print (input[k-1::-1] + input[k:])

# Driver program
if __name__ == "__main__":
	input = [1, 2, 3, 4, 5, 6]
	k = 4
	reverseArrayUptoK(input, k)
