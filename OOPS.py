#  Classes and Objects 

# class Person:
#     name="Abir"
#     occupation="SDE"
#     salary=500000
#     def info(self): # Self means : The object for whcih the class Method is called
#         print(f"{self.name} is a {self.occupation}")


# a=Person()
# b=Person()
# a.name="Manash"
# a.occupation=" F& B Manager"

# b.name="Chandana"
# b.occupation="HR"
# a.info() # When a invokes then Self method is called for  object -a,hence name and ocup is of a
# b.info() # When b is invoked ,then Self Method is called for that object-b, hence name and ocup is of b

# #print(a.name," works as ",a.occupation)


# CONSTRUCTOR

 # Constructor is being called the moment the class object is being declared

# class Person:

#     def __init__(self,name=None,occ=None):  # helps in creating a Constructor
#         self.name=name
#         self.occupation=occ
#         if name is not None and occ is not None:  # -----> For Parametrized Constructor
#             print(f"{self.name} works as {self.occupation}")
#         else:                                      # ------> For Default Cosntructor
#             print("Nobody is there to work")

#     # def info(self):
#     #     print(f"{self.name} is an {self.occupation}")

# a=Person() 
# b= Person("Harry","SDE")  # Just passing the Paramters in the Constructor being called.
# c=Person("Abir","Product Manager")

# VVV. Imp:: In python only a single constructor is creted whether it is for  defualt or parametrized. We  can seperate their logiucs by using If-Else block of code


# DECORATORS

# def greet(fx):
#     def mfx():
#         print("Good Morning")

#         def nfx():
#             print("Hello ,How are you?")
#             fx()
#             print("I am fine,lets have our work start")
#         return nfx

#         print("Thanks for using the Function. have a great day!!")
#     return mfx

# def greet(fx):
#     def mfx():
#         print("Good Morning")
#         def nfx():
#             print("Hello, How are you?")
#             fx()
#             print("I am fine, let's have our work start")
#         return nfx()

#     print("Thanks for using the Function. Have a great day!!")
#     return mfx

# #@greet # -----> Use of Decorator function
# def hello():
#     print("Hi friend, I am fine ,how are you")

#hello() # In this case since @  Tag is used before a function to  make it decorated, so we can say that the decorator function will execute it line along with the function lines where it is being used in decoratore function
# greet(hello)()



# Getter and Setters in OOPS

# Note : For Getter we use @Property Decorator tag to Identify it.
# Note : For Setter we use <attribute>.setter tag to identify the seter method for the attribute


# class student:
#     def __init__(self,initialMarks=10):
#         self._mark=initialMarks

#     def show(self):
#         print(f"The Percentage of student is : {self._mark}")

#     @property
#     def mark(self):
#         print("Getting Student Percentage: ")
#         return self._mark

#     @mark.setter
#     def mark(self,newMarks):
#         self._mark= (newMarks/70)*100           # No return as we are only setting any value 


        
    
# myObj= student()

# # print(myObj.mark)  Here directly the obg called the mark method to retriev the valu, hence the getter invokes
# a= int(input("Enter the marks of student: "))
# print()
# myObj.mark=a  # --- > Here , we set the value of the object created and hence , at this point only the setter for mark method is invoked and performs the logic here
# # print(myObj.mark)
# myObj.show()   #-- > The show function is hence called to return the value of the  self attribute mark .


# INHERITANCE

# class Employee:
#     def __init__(self,name,id):
#         self.name=name
#         self.id=id
#     def showData(self):
#         print(f"The name of employee is : {self.name} and the ID is : {self.id}")


# class Manager(Employee):
#     def post(self):
#         print("I am in Manager post")


# # e=Employee("Abir Choudhury",1)
# # e.showData()

# m= Manager("Manash",23)
# m.showData()
# m.post()



# Creating Snake Water Gun Game with the use of computer generated input


# import random

# def check(comp,user):

#     if(comp==user):
#         return 0

#     if(comp==1 and user==2):
#         return -1
#     if(comp==2 and user==3):
#         return -1
#     if(comp==3 and user==1 ):
#         return -1

#     return 1

# while(1):

#     comp=random.randint(1,3)
#     user= int(input("Choose the number :\n 1. Snake\n 2. Water \n 3. Gun \n 4. Quit \n"))

#     if(user==4):
#         print("I am quiting the game")
#         break
#     score=check(comp,user)

#     print("Your choice is : ",user)
#     print("Comp choice is: ",comp)

#     if(score==0):
#         print("Its a Tie\n")
#     elif(score==1):
#         print("YOU WON!!!\n")
#     else:
#         print("YOU Lose!!\n")


# Instances are thosewhich are differnt for each object we create for an class and just need to be passed as an object instance.
# But Class variasbles are those which are same for all the objects that are being invoked for the class and are equally/Same for all the objects of the class

# class student:

#     companyName="AppPerfect"

#     def __init__(self,name):
#         self.name=name
#         self.raiseAmount=0.2

#     def showDetails(self):
#         print(f" The Employee name is {self.name} and the raise amount is {self.raiseAmount}  and works in comapny {self.companyName}")


# e1=student("Harry")
# e1.raiseAmount=0.5

# e2= student("Abir")
# e2.raiseAmount=0.7

# e3=student("Manash")

# e1.showDetails()
# e2.showDetails()
# e3.showDetails()


# Class Methods -These aste those which are used to directly make Manipulation on class value  like class variables inside a class and no instance are carried out

# class friend:
#     myBestFriend="Naman" # This is my class variable
#     def __init__(self,friend):
#         self.friend=friend
#     def show(self):
#         print(f"My friend name is {self.friend} but {self.myBestFriend}  is my best Friend of all")
     
#     @classmethod
#     def newFriend(self,newFriend):
#         self.myBestFriend= newFriend

# f1= friend("Priyanshuu")
# f1.show()
# f2= friend("Yash Soni")
# f2.show()
# f2.newFriend("Harshit Paneri") # If we dont use @class  Method Decorator then the change in class variable will not be there and only there will be instance change,i.e for the object for whcih it is being called
# f2.show()
# print(friend.myBestFriend)  ## Hence if we print the calss variable again, then the original value will only be shown


# But if  we use the @classmethod Tag- It help to directly edit the class variable or methods

# f3 = friend("Asim ali")
# f3.newFriend("Harshit Paneri")
# f3.show()
# print(friend.myBestFriend)  # This time it actuall changes the class variable value



# Dict : It is used to create dictionary for the kind of object value being passed

# class Person:
#     def __init__(self,name,age):
#         self.anme=name
#         self.age=age
#         self.version=12

# p=Person('Abir',21)
# print(p.__dict__)



# SUPER Keyword- It help to directly in herit methods for child class from its parent class, wherther it is any method or the constructor itself

# class Employee:
#     def __init__(self,name,emp_id):
#         self.name=name
#         self.id=emp_id

# class Programmer(Employee):
#     def __init__(self,name,emp_id,lang):
#         super().__init__(name,emp_id)
#         self.lang=lang

# prg=Programmer("Abir Choudhury" ,'2',"Python")
# print(prg.name)
# print(prg.id)
# print(prg.lang)


# Single Inheritance


# class Animal:
#     def __init__(self,name,breed):
#         self.name=name
#         self.breed= breed


#     def sound(self):
#         print("Sound of all the animals ")

# class Dog(Animal):

#     def __init__(self,name,col):
#        # self.name=nameS
#         #self.breed=breed
#         Animal.__init__(self,name,breed=Dog)
#         self.col=col
        
#     def show(self):
#         print(f"Name of animal is {self.name} and color is  {self.col}")

#     def sound(self):
#         Animal.sound(self)
#         print("Dog Barks!!!")

# d =Dog("Robin","Brown")
# d.show()
# d.sound()

# a= Animal("Cat","Mouse")
# a.sound()


#   MULTIPLE INHERITANCE- A child class generates from mutliple parent class and can inherits the propertie sof it

#     ### V.V. Imp---> Here the order matters.
            # if any function is invoked for a child class from its parent class which is common in all , then the order in which they have been called inside Child class , will be followed to call the method for class also




# MULTILEVEL Inheritance: Mutltiple child clss can be created one afte  another inheriting the properties of parent  class.
# Hence ,this way the last child class can inherit the properties of the first parent class also

class first:
    def __init__(self,name,species):
        self.name=name
        self.species= species

    def show_details(self):
        print(f"Name is : {self.name}")
        print(f"Species is :{self.species}")

class second(first):
    def __init__(self,name,breed):
        first.__init__(self,name,species="Dog")
        self.breed=breed

    def show_details(self):
        first.show_details(self)
        print(f"Breed of the species is : {self.breed}")

class third(second):
    def __init__(self,name,color):
        second.__init__(self,name,breed="Doberman")
        self.color=color

    def show_details(self):
        second.show_details(self)
        print(f"Colour of the species is : {self.color}")


# th= third("Robin","Brown")
# th.show_details()

se=second("Hin","Black")
se.show_details()
#POLYMORPHISM

class Bird:

	def intro(self):
		print("There are many types of birds.")

	def flight(self):
		print("Most of the birds can fly but some cannot.")

class sparrow(Bird):

	def flight(self):
		print("Sparrows can fly.")

class ostrich(Bird):

	def flight(self):
		print("Ostriches cannot fly.")

obj_bird = Bird()
obj_spr = sparrow()
obj_ost = ostrich()

obj_bird.intro()
obj_bird.flight()

obj_spr.intro()
obj_spr.flight()

obj_ost.intro()
obj_ost.flight()
