# Single Inheritance:
"""Single inheritance enables a derived class to inherit properties from a single parent class, thus enabling code reusability and the addition of new features to existing code."""

# Python program to demonstrate
# single inheritance

# Base class
# class Parent:
# 	def func1(self):
# 		print("This function is in parent class.")

# # Derived class


# class Child(Parent):
# 	def func2(self):
# 		print("This function is in child class.")


# # Driver's code
# object = Child()
# object.func1()
# object.func2()


# Multiple Inheritance: 

"""
When a class can be derived from more than one base class this type of inheritance is called multiple inheritances. In multiple inheritances, all the features of the base classes are inherited into the derived class. 
"""


# Python program to demonstrate
# multiple inheritance

# Base class1
class Mother:
	mothername = ""

	def mother(self):
		print(self.mothername)

# Base class2


class Father:
	fathername = ""

	def father(self):
		print(self.fathername)

# Derived class


class Son(Mother, Father):
	def parents(self):
		print("Father :", self.fathername)
		print("Mother :", self.mothername)


# Driver's code
s1 = Son()
s1.fathername = "RAM"
s1.mothername = "SITA"
s1.parents()
