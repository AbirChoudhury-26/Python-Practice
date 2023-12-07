def symmetryCheck(a):
    
    n=len(a)
    flag=1
    if n%2==0:
        mid=n//2+1
    else :
        mid=n//2

    start1=0
    start2=mid

    while(start1 <mid  and start2 <n):
        if(a[start1]==a[start2]):
            start1=start1+1
            start2=start2+1
        else:
            f=0
            break

    if flag==1:
         print("The entered string is symmetrical")
    else:
        print("The entered string is not symmetrical")

         
string=input("Enter any string: ")
symmetryCheck(string)
