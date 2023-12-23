# Iterating With Python Lambdas 

# # list of numbers 
# l1 = [4, 2, 13, 21, 5] 

# l2 = [] 

# # run for loop to iterate over list 
# for i in l1: 
	
# 	# lambda function to make square 
# 	# of number 
# 	temp=lambda i:i**2

# 	# save in list2 
# 	l2.append(temp(i)) 

# # print list 
# print(l2)

arr=[1,2,3,4] 
v=8
x=lambda arr,v: True if v in arr else False

if(x(arr,v)): 
	print("Element is Present in the list") 
else: 
	print("Element is Not Present in the list")

