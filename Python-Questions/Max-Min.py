gfg_list = [8, 1, 7, 10, 5]
# min and max indexes are taken 1st element
# In some cases list might be a single element
min_ele, max_ele = gfg_list[0], gfg_list[0]

for i in range(1, len(gfg_list)):
	if gfg_list[i] < min_ele:
		min_ele = gfg_list[i]
		
	if gfg_list[i] > max_ele:
		max_ele = gfg_list[i]
		
print('Minimum Element in the list', gfg_list, 'is', min_ele)
print('Maximum Element in the list', gfg_list, 'is', max_ele)

# # function to find minimum and maximum position in list
def minimum(a, n):
	# inbuilt function to find the position of minimum
	minpos = a.index(min(a))

	# inbuilt function to find the position of maximum
	maxpos = a.index(max(a))

	# printing the position
	print("The maximum is at position", maxpos + 1)
	print("The minimum is at position", minpos + 1)

# driver code
a = [3, 4, 1, 3, 4, 5]
minimum(a, len(a))
