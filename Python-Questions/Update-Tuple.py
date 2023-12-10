# tl=[(1,2,3),(4,5,6),(7,8,9)]

# print("The Original Tuple")

# print(tl)

# print("After Modification")
# add=4
# res=[tuple(map(lambda ele: ele+add,i))for i in tl]
# print(res)

#  Updating tuple usinf for loop
def updates_tuple(tup,newval):
    for i in range(len(tup)):
        x,y,z=tup[i];
        tup[i]=(newval,y,z)

    return tup
tup = [(1, 56, 'M'), (1, 14, 'F'), (2, 43, 'F'), (2, 10, 'M')]
new_val=5

print(updates_tuple(tup,new_val))
