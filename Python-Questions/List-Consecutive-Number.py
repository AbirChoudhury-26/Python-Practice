# Approach #1 : using sorted() 

# Python3 Program to Create list 
# with integers within given range 

def checkConsecutive(l):
	return sorted(l) == list(range(min(l), max(l)+1))
	
# Driver Code
lst = [2, 3, 1, 4, 5]
print(checkConsecutive(lst))

#given list
lst = [2, 3, 1, 4, 5]

#sort the list
sorted_lst = sorted(lst)

#check if all elements are consecutive
is_consecutive = all(sorted_lst[i] == sorted_lst[i-1] + 1 for i in range(1, len(sorted_lst)))

#print the result
print(is_consecutive) # prints True
#This code is contributed by Edula Vinay Kumar Reddy

