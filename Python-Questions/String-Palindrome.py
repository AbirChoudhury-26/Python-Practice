def palindromeCheck(a):

    mid=(len(a)-1)//2
    start=0,
    last=len(a)-1
    flag=1

    while(start <= mid):
  
        # comparing letters from right
        # from the letters from left
        if (a[start]== a[last]):
             
            start += 1
            last -= 1
             
        else:
            flag = 1
            break
             
    # Checking the flag variable to 
    # check if the string is palindrome
    # or not
    if flag == 0:
        print("The entered string is palindrome")
    else:
        print("The entered string is not palindrome")
string=input("Enter any string: ")
palindromeCheck(string)