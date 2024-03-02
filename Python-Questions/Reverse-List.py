# Method-1

"""Reversing a list using slicing technique"""
def Reverse(lst):
    new_lst = lst[::-1]
    return new_lst


lst = [10, 11, 12, 13, 14, 15]
print(Reverse(lst))

# Method-2

"""  Reverse List by Swapping"""
#Python program to reverse an array
def list_reverse(arr,size):

	#if only one element present, then return the array
	if(size==1):
		return arr
	
	#if only two elements present, then swap both the numbers.
	elif(size==2):
		arr[0],arr[1],=arr[1],arr[0]
		return arr
	
	#if more than two elements presents, then swap first and last numbers.
	else:
		i=0
		while(i<size//2):

	#swap present and preceding numbers at time and jump to second element after swap
			arr[i],arr[size-i-1]=arr[size-i-1],arr[i]
	
	#skip if present and preceding numbers indexes are same
			if((i!=i+1 and size-i-1 != size-i-2) and (i!=size-i-2 and size-i-1!=i+1)):
				arr[i+1],arr[size-i-2]=arr[size-i-2],arr[i+1]
			i+=2
		return arr

arr=[1,2,3,4,5]
size=5
print('Original list: ',arr)
print("Reversed list: ",list_reverse(arr,size))

# Method-3

"""  Reverse List Using the Reversed() and Reverse() Built-In Function"""
lst = [10, 11, 12, 13, 14, 15]
lst.reverse()
print("Using reverse() ", lst)

print("Using reversed() ", list(reversed(lst)))

# Method-4

"""Using 2-Pointer Approach"""

# Reversing a list using two-pointer approach
def reverse_list(arr):
	left = 0
	right = len(arr)-1
	while (left < right):
		# Swap
		temp = arr[left]
		arr[left] = arr[right]
		arr[right] = temp
		left += 1
		right -= 1

	return arr

arr = [1, 2, 3, 4, 5, 6, 7]
print(reverse_list(arr))
