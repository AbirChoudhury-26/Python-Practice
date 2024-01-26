"""
What is the super () method used for?
A method from a parent class can be called in Python using the super() function. It’s typical practice in object-oriented programming to call the methods of the superclass and enable method overriding and inheritance.
"""


# # parent class
# class Person():
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def display(self):
#         print(self.name, self.age)

# # child class
# class Student(Person):
#     def __init__(self, name, age):
#         self.sName = name
#         self.sAge = age
#         # inheriting the properties of parent class
#         super().__init__("Rahul", age)

#     def displayInfo(self):
#         print(self.sName, self.sAge)

# obj = Student("Mayank", 23)
# obj.display()
# obj.displayInfo()

# Inheritance with super function 

# code
# A Python program to demonstrate inheritance

# class Person:

# 	# Constructor
# 	def __init__(self, name, id):
# 		self.name = name
# 		self.id = id

# 	# To check if this person is an employee
# 	def Display(self):
# 		print(self.name, self.id)
	

# class Emp(Person):
	
# 	def __init__(self, name, id):
# 		self.name_ = name
# 		super().__init__(name, id)

# 	def Print(self):
# 		print("Emp class called")

# Emp_details = Emp("Mayank", 103)

# # calling parent class function
# print(Emp_details.name_, Emp_details.name



# Multiple Inheritance with Super

# class Mammal():

# 	def __init__(self, name):
# 		print(name, "Is a mammal")

# class canFly(Mammal):

# 	def __init__(self, canFly_name):
# 		print(canFly_name, "cannot fly")

# 		# Calling Parent class
# 		# Constructor
# 		super().__init__(canFly_name)

# class canSwim(Mammal):

# 	def __init__(self, canSwim_name):

# 		print(canSwim_name, "cannot swim")

# 		super().__init__(canSwim_name)

# class Animal(canFly, canSwim):

# 	def __init__(self, name):
# 		super().__init__(name)

# # Driver Code
# Carol = Animal("Dog")


# MultiLevel Inheritance with Super

class Mammal():

	def __init__(self, name):
		print(name, "Is a mammal")


class canFly(Mammal):

	def __init__(self, canFly_name):
		print(canFly_name, "cannot fly")

		# Calling Parent class
		# Constructor
		super().__init__(canFly_name)


class canSwim(canFly):

	def __init__(self, canSwim_name):

		print(canSwim_name, "cannot swim")

		super().__init__(canSwim_name)


class Animal(canSwim):

	def __init__(self, name):

		# Calling the constructor
		# of both the parent
		# class in the order of
		# their inheritance
		super().__init__(name)


# Driver Code
Carol = Animal("Dog")



