# # print(12345678)
# print("18")

# print(12345678)

#  Taking user Input


# a=input("Enter the first Number:")
# b=input("Enter the second number:")
# c=input("Enter your name:")
# print(int(a)+int(b))
# print('My name is ',c," I work at AppPerfect")

#  MultiLine

# apple= '''Hello
# world
# I am in 
# Apperfect working as 
# SDE'''

# print(apple)

# print("Let use For loop")

# for x in apple:
#     print(x)


#  String Slicing
#  Strings are iimutable , means they will create a new string but not change the existing one

# names="Hello , My name is Abir"
# print(names[0:5])

# print(len(names ))

# print(names.upper())
# print(names.lower())

#  String Methods

# x="Hello is the  World!!!!"

# print(x.replace("Hello","My"))
# print(x.split(" "))
# print(x.endswith("h"))
# print(x.find("is"))
# print(x.isalpha())


#  If-else

# number=int(input("Enter your age:"))

# if(number<0):
#     print("Number is Negative")
# elif(number==1000):
#     print("Specail Number ")
# else:
#     print("Number is Positive")
#     print("Yayyyyy!!!")

# x=int(input("Enter any number: "))

# match x:
#  case 0:
#   print("Hello")
#  case 1:
#   print("World")

# name="Abhishek"

# for i in name:
#     print(i, end='-')
#     if(i =='b'):
#         print("It is a special Character")
#     elif(i=='A'):
#         print("It is starting character")

# for i in range(1,10,2):
#     if(i%2==0):
#         print("Even")
#     else:
#         print("Odd")

# for i in range(12):
#     if(i==10):
#         continue
#     print("5 X ",i+1,'= ',5*(i+1))
# print("Out of Loop")

# Functions

# def calGmean(a,b):
#     mean=(a*b)/(a+b)
#     print(mean)

# calGmean(4,5)
# calGmean(9,10)
# calGmean(4,8)


# LIst 
#  Mutuable & any data type
# mark=[2,3,"4","Harry",True]

# print(mark)
# print(type(mark))
# print(mark[4])

# if "4" in mark:
#     print("Yes")
# else:
#     print("No")

#     # List Comprehension

# lst=[i*i  for i in range(10) if i%2!=0]
# print(lst)

# List methods

# l= [1,23,4,5,64,7,8,90,20]
# print(l)

# l.sort(reverse=True)
# print(l)

# m=l.copy()
# m[0]=0
# print(m)

# l.insert(3,9000)
# print(l)

# m=[1223,1345,88787]
# l.extend(m)
# print(l)

#  Tuples- Immutable

# tup=(1,5,6,7,9,10)
# print(type(tup))
# print(tup)

# if 5 in tup:
#     print("Yes present")

# tup2=tup[1:4]
# print(tup2)
# print(len(tup))

# Tuple Methods:

# countries=("India","Australia","South Africa","USA","New Zealand")

# print(countries)
# print(type(countries))
# temp=list(countries)
# print(temp)
# print(type(temp))

# temp[1]="Brazil"
# print(temp)

# countries2=("India","Australia","South Africa","USA","New Zealand")
# new=("Srilanka","Bangladesh","Japan")

# asianCountry= countries2+new
# print(asianCountry)

# tuple1=(0,1,2,3,1,2,1,3,1,2,3)
# res=tuple1.count(1)
# print(tuple1.index(3))
# print(res)
# #  Index baswd
# print(tuple1.index(3,4,8))
#  First is the number to be searched and then the range in whoch we want to search

#  String Formatting

# statement="Hey my name is {} and I am from {}"
# country="India"
# name="Abir"

# print(statement.format(name,country))

#  f-string

# print(f"My name is {name} and I am from {country}")
# price=45.9878977
# txt=f"only for {price:.4f} dollars"

# print(txt)

#  Doc Strings

# def square(n):
#     '''Takes a number and return a square '''
#     print(n**2)

# square(5)    
# print(square.__doc__ )

#  Use of Functions and Reccursion:

# def factorial(n):
#     if(n==0 or n==1):
#         return 1

#     return n*factorial(n-1)

# print(factorial(5))

#  Fibonacci Series
#  Simple steps

# userInput= int(input("Enter any number:"))

# f1,f2=0,1
# print(f1,f2,end=" ")

# for i in range (userInput):
#     next_number=f1+f2
#     f1=f2
#     f2=next_number
#     print(next_number,end=" ")
#     i+=1

#  Using Recursion

# def Fibonacci(num):
#     n=num
#     f1,f2=0,1
#     print(f1,f2,end=" ")
#     for i in range (num):
#         next_number=f1+f2
#         f1=f2
#         f2=next_number
#         print(next_number,end=" ")
#     print("\nThis is the fibonacii series upto",n," terms")
    

# userInput= int(input("Enter any number:"))
# Fibonacci(userInput)

#Sets

# s={2,3,4,5,6,2,1,3,4,5,6}
# print(s)

# info={"Hello",1,2,3,4,"World",True}
# print(info)

# abir=set()   # for calling an empty set 
# print(type(abir))

# for i in info:
#     print(i)

  #  Sets Methods

# s1={1,2,3,4}
# s2={6,7,8,9}

# s3=(s1.union(s2))
# print(s3)

# s1.update(s2)
# print(s1)

# print(s1.intersection(s2))
# print(s1.issuperset(s2))

# s1.add(900988)
# print(s1)
# s1.discard(4)
# print(s1)

# del s1
# print(s1)

#  Dictionary

# dic={
#     "harry":"Human Being",
#     "Spoon":"Object",
#     "age":16,
#     "boolean":True,
#     "Age":"MALE",
#     "Class":8
# }

# print(dic["harry"])

# for i in dic.keys():
#      print(dic[i])

# for i in dic:
#     print(f"The value corresponding to the key {i} is : {dic[i]}")

# for key,value in dic.items():    # .items() it works with key value pair and w ecan perform any operation in key-value pair.
#     print(key," : ",value) 

# s1={222:21,444:67,900:87}
# s2={123:24,789:67,345:90}

# s1.update(s2)

# Use of else with Loops


# print(s1)
# s1.popitem()   # Only removes item from back
# print(s1)

# del s1[222]
# print(s1)

# for i in []:
#     print(i)
#     if i==4:
#         break

# else:
#     print("I am done with the loop")

# i=0
# while i < 7:
#     print(i)
#     i+=1

# else:
#     print("I am done with the loop")

#  Prgm to print a table usign f string method


# a= int(input("Enter any number: "))

# print(f"Mutiplication of {a} is: ")

# for i in range(1,11):
#     print(f"{a} x {i} = {a*i}")

#  Exectuion of Try-Catch block

# a= (input("Enter any number: "))
# print(f"Mutiplication of {a} is: ")

# try:
#     for i in range(1,11):
#      print(f"{int(a)} x {i} = {int(a)*i}")
# except:
#     print("Invalid Output")
 
# print("Lines of code are executed")

# Finally with Try-catch
#  Usful in case of functions,where we always want to return the value
# def func1():

#     try:
#         l=[1,2,3,4]
#         index=int(input("Enter the index: "))
#         print(l[index])
#         return 1
#     except:
#         print("Some error")
#         return 0

#     finally:
#         print("Always executed")

# x=func1()
# print(x)


# Short hand if-else

# a=7687
# b=2233
# print("A is greater ") if a>b else print("=") if a==b else print("B")

# c=90 if a>b else 0
# print(c)

# Enumerate function

# marks=[344,6566,7898,12,67,89]

# for index,number in enumerate(marks,start=1):
#      print(number)
#      if(index==3):
#          print("Awesome!!!!")

# Import function

# from math import sqrt,pi

# result= sqrt(9)*pi
# print(result)


# from math import pow as h

# ans= h(2,3)
# print(ans)

# import math

# print(dir(math))

# import abir 

# # a.hello()
# # print(a.name)

# Use of __name__

   # If imported from another file and then executed the __name__ ,it has the type of file name ,i.e .__name__!=__main.Hence it doesnt excute the main function anfd avoid any ,mistake
# import abir



# OS MOdule in python

import os

#  To create a directory ,if not exist in the folder 
if(not os.path.exists("Tutorial Practice")):
    os.mkdir("Tutorial Practice")

# If exist ,then make directory inside the Main 
# for i in range(0,100):
#     os.mkdir(f"Tutorial Practice/Day{i+1}")

# Renaming an Existing file

# for i in range(0,100):
#     os.rename(f"Tutorial Practice/Day{i+1}", f"Tutorial Practice/Tutorial {i+1}" )


# Getting the Directory list

# folders= os.listdir("Tutorial Practice")
# print(folders)

# print(os.getcwd())

# os.chdir("/Users")
# print(os.getcwd())
# for files in folders:
#     print(files)

# for content in folders:
#     print(content)
#     print(os.listdir(f"Tutorial Practice/{content}"))


#  Short exercise to create a Python code for Encoding/ Decoding  a string

# message= input("Enter your string: ") # We need to perform encoding in each of the words of the string,i.e we will split
# words=message.split(" ")
# coding = input("Do you want to code or decode??")
# if(coding=="Coding"):
#     nencoding=[]
#     for word in words:
#         if(len(word)>=3):
#             r1="new"
#             r2="dog"
#             stNew=r1+word[1:]+word[0]+r2
#             nencoding.append(stNew)  # Appended in a list 
#         else:
#             nencoding.append(word[::-1]) # This means that to print the whole string but with a step of -1,hence in revrese order
#     # Now to convert the whole list in a string, we use join keyword ,with a seperator like " "
#     finalEncodedstring =" ".join(nencoding)
#     print(finalEncodedstring)
            
# else:
#     ndecoding=[]
#     for word in words:
#         if(len(word)>=3):
#             stNew= word[3:-3]
#             stNew= stNew[-1]+ stNew[:-1]
#             ndecoding.append(stNew)
#         else:
#             ndecoding.append(word[::-1])
    
#     finalDecodedString= " ".join(ndecoding)
#     print(finalDecodedString)



# Use of Local and Global Variables

# x=10
# def my_function():
#     global x
#     x=5
#     y=20
#     print(x)
# my_function()
# print(f"The value of x is: {x}")



# File Handling
 
#   Writing a file: Creates a new File even if no file is there

# f=open("myFile.txt","w")
# f.write("Hello to this World")

# Reading a file

# r=open("myFile.txt","r")
# text=r.read()
# print(text)
# r.close()

# Appending in a file

# a=open("myFile.txt","a")
# a.write(" I am Abir Choudhury")
# a.close()


# Readline in file handling

# f=open("myFile.txt","r")

# while True:
#     line = f.readline()
#     print(line)

#     if not line:
#         break


# Let suppose to print each of the marks of Student in  3 subject

#Readline,writeline


# i=0
# f=open("myFile.txt","r")
# while True:
#     i=i+1
#     line= f.readline()

#     if not line:
#         break
    
#     m1=line.split(",")[0]
#     m2=line.split(",")[1]
#     m3=line.split(",")[2]

#     print(f"Marks of Student {i} in English {m1}")
#     print(f"Marks of Student {i} in Hindi {m2}")
#     print(f"Marks of Student {i} in Maths {m3}")

#     print(line)

# f=open("myFile.txt","w")
# lines=["line1\n","line2\n","line3\n"]

# f.writelines(lines)
# f.close()


# Lambda Functions
  # They dont require toreturn and are calculatd at short hand function in temp form

# double =lambda x: x*2

# print(double(6)) 


# def val(fx,value):
#     return 6 + fx(value)

# cube = lambda x: x*x*x

# result=val(cube,2)
# print(result)

# def val(fx,value):
#     return 6 + fx(value)

# result=val(lambda x: x*x*x,2)
# print(result)

# avg= lambda x,y,z: (x+y+z)/3

# print(avg(3,5,10))



# Map , filters and Reduce

  # Map element applies to any function to be applied for each element & returns a sequence of transformed eleemnts

# def cube(x):
#     return x*x*x
# l=[1,2,3,4,5,6,7,2,3,4]

#  Without map,
 
# newlist=[]
# for i in l:
#     newlist.append(cube(i))

#print(newlist)

# MAP

# newl=[]
# newl=list(map(lambda x: x*x*x,l))
# print(newl)

# FILTER: FOR EACH VALUE Filtetr return true will remain in list else not

# def filter_function(a):
#     return a >3

# newl= list(filter(filter_function,l))
# print(newl)


# REDUCE : It always takes two arguments and returns a single value

#from functools import reduce

# def sum(x,y):
#     return x+y

# num=[1,2,3,5,6,7]

# result=reduce(sum,num)
# print(result)

# Creating of Virtul Environment
# 1. To create  Virtual Env. Packagage ,we write (For Macos & Linux):
#        python3 -m venv <file
# name>

# 2. To activate the package ,so to perform further activities ,we do:
#        source <filename>/bin/activate

# Creating Requirement file--> So that we can export all our dependencies to anyone without explicitly defining each of them
   # 3. pip3 freeze > requirements.txt