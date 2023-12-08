tup = (5, 20, 3, 7, 6, 8)
k = 2

max_k_elements = []
min_k_elements = []

for elem in tup:
	max_k_elements.append(elem)
	max_k_elements.sort(reverse=True)
	if len(max_k_elements) > k:
		max_k_elements.pop()
	
	min_k_elements.append(elem)
	min_k_elements.sort()
	if len(min_k_elements) > k:
		min_k_elements.pop()

print("Maximum", k, "elements:", max_k_elements)
print("Minimum", k, "elements:", min_k_elements)
