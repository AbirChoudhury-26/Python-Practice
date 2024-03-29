# Using Slicing Method

# def reverseArrayUptoK(input, k):
# 	print (input[k-1::-1] + input[k:])

# # Driver program
# if __name__ == "__main__":
# 	input = [1, 2, 3, 4, 5, 6]
# 	k = 4
# 	reverseArrayUptoK(input, k)

# Using 2 Pointer 
	
def reverseArray(arr, k):
    start = 0
    end = k-1
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1
    return arr
arr=[1, 2, 3, 4, 5, 6]
k = 4
print(reverseArray(arr, k))


import numpy as np

# function to reverse array upto given position
def reverseArrayUptoK(arr, k):
	
	# reverse subarray upto position k
	arr[0:k] = np.flip(arr[0:k], axis=0)
	
	return arr

# driver code
if __name__ == "__main__":
	arr = [1, 2, 3, 4, 5, 6]
	k = 4
	print(reverseArrayUptoK(arr, k))

