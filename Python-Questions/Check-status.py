a=-1
b=-1
flag=True

if(a>0 and b<0 ) or (a<0 and b>0) and not flag:
    print(True)
elif a<0 and b<0 and flag:
    print(True)
else:
    print(False)

