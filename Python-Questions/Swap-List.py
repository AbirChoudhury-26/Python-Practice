
def swapList(l):
    size=len(l)

    temp=l[0]
    l[0]=l[size-1]
    l[size-1]=temp

    return l

l=[12,4,5,87,31,90]
print(swapList(l))
