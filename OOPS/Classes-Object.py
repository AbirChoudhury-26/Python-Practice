# Python3 program to
# demonstrate instantiating
# a class
class Dog:

	# A simple class
	# attribute
	attr1 = "mammal"
	attr2 = "dog"

	# A sample method
	def fun(self):
		print("I'm a", self.attr1)
		print("I'm a", self.attr2)


# Driver code
# Object instantiation
Rodger = Dog()

# Accessing class attributes
# and method through objects
print(Rodger.attr1)
Rodger.fun()


class GFG:
	def __init__(self, name, company):
		self.name = name
		self.company = company

	def show(self):
		print("Hello my name is " + self.name+" and I" +
			" work in "+self.company+".")


obj = GFG("John", "GeeksForGeeks")
obj.show()

# Python3 program to
# demonstrate instantiating
# a class
class Dog:

	# A simple class
	# attribute
	attr1 = "mammal"
	attr2 = "dog"

	# A sample method
	def fun(self):
		print("I'm a", self.attr1)
		print("I'm a", self.attr2)


# Driver code
# Object instantiation
Rodger = Dog()

# Accessing class attributes
# and method through objects
print(Rodger.attr1)
Rodger.fun()


# class GFG:
# 	def __init__(somename, name, company):
# 		somename.name = name
# 		somename.company = company

# 	def show(somename):
# 		print("Hello my name is " + somename.name +
# 			" and I work in "+somename.company+".")


# obj = GFG("John", "GeeksForGeeks")
# obj.show()


# __init__() method
# The __init__ method is similar to constructors in C++ and Java. Constructors are used to initializing the object’s state. Like methods, a constructor also contains a collection of statements(i.e. instructions) that are executed at the time of Object creation. It runs as soon as an object of a class is instantiated. The method is useful to do any initialization you want to do with your object.

# Sample class with init method
class Person:

	# init method or constructor
	def __init__(self, name):
		self.name = name

	# Sample Method
	def say_hi(self):
		print('Hello, my name is', self.name)


p = Person('Nikhil')
p.say_hi()
