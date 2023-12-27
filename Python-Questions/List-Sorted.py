# Python3 code to demonstrate 
# to check if list is sorted
# using naive method 

# initializing list
test_list = [1, 4, 5, 8, 10]

# printing original list 
print ("Original list : " + str(test_list))

# using naive method to 
# check sorted list 
flag = 0
i = 1
while i < len(test_list):
	if(test_list[i] < test_list[i - 1]):
		flag = 1
	i += 1
	
# printing result
if (not flag) :
	print ("Yes, List is sorted.")
else :
	print ("No, List is not sorted.")


# Method 2 : Using sort() The new list can be made as a copy of the original list, sorting the new list and comparing with the old list will give us the result if sorting was required to get sorted list or not. 

# Python3 code to demonstrate 
# to check if list is sorted
# using sort()

# initializing list
test_list = [10, 4, 5, 8, 10]

# printing original list 
print ("Original list : " + str(test_list))

# using sort() to 
# check sorted list 
flag = 0
test_list1 = test_list[:]
test_list1.sort()
if (test_list1 == test_list):
	flag = 1
	
# printing result
if (flag) :
	print ("Yes, List is sorted.")
else :
	print ("No, List is not sorted.")

