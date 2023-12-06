n=int(input("Enter any number: "))

num=n
f=True
for i in range(2,num):
    if num%i==0:
        f=False
        break

if f==True:
    print("Prime Number")
else:
    print("Not a prime number")
