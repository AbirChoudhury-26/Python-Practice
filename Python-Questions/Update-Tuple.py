tl=[(1,2,3),(4,5,6),(7,8,9)]

print("The Original Tuple")

print(tl)

print("After Modification")
add=4
res=[tuple(map(lambda ele: ele+add,i))for i in tl]
print(res)

