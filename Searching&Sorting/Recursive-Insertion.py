# # Recursive Python program for insertion sort

# # Recursive function to sort an array using insertion sort
# def insertionSortRecursive(arr, n):
# 	# base case
# 	if n <= 1:
# 		return

# 	# Sort first n-1 elements
# 	insertionSortRecursive(arr, n - 1)

# 	# Insert last element at its correct position in sorted array.
# 	last = arr[n - 1]
# 	j = n - 2

# 	# Move elements of arr[0..i-1], that are
# 	# greater than key, to one position ahead
# 	# of their current position
# 	while (j >= 0 and arr[j] > last):
# 		arr[j + 1] = arr[j]
# 		j = j - 1
# 	arr[j + 1] = last


# # Driver program to test insertion sort
# if __name__ == '__main__':
# 	A = [-7, 11, 6, 0, -3, 5, 10, 2]
# 	n = len(A)
# 	insertionSortRecursive(A, n)
# 	print(A)



# Using Divide & Conquer Method


def insertion_sort_recursive(arr):
	# base case: return when array has only one element
	if len(arr) <= 1:
		return arr

	# recursively sort the first half of the array
	mid = len(arr) // 2
	left_half = insertion_sort_recursive(arr[:mid])

	# recursively sort the second half of the array
	right_half = insertion_sort_recursive(arr[mid:])

	# merge the sorted halves into a sorted array
	i, j = 0, 0
	sorted_arr = []
	while i < len(left_half) and j < len(right_half):
		if left_half[i] < right_half[j]:
			sorted_arr.append(left_half[i])
			i += 1
		else:
			sorted_arr.append(right_half[j])
			j += 1
	# This part is used to add the other remaining elements if any part gets finished first 
	sorted_arr += left_half[i:]  
	sorted_arr += right_half[j:]

	return sorted_arr
arr = [5, 2, 4, 6, 1, 3]
sorted_arr = insertion_sort_recursive(arr) 
print(sorted_arr) # Output: [1, 2, 3, 4, 5, 6]
