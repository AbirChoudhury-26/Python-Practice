# # # A Python program to demonstrate inheritance
# class Person(object):

# # Constructor
#     def __init__(self, name, id):
#         self.name = name
#         self.id = id

#     # To check if this person is an employee
#     def Display(self):
#         print(self.name, self.id)


# # Driver code
# emp = Person("Satyam", 102) # An Object of Person
# emp.Display()

# class Emp(Person):

#     def Print(self):
# 	    print("Emp class called")
	
# Emp_details = Emp("Mayank", 103)

# # calling parent class function
# Emp_details.Display()

# # Calling child class function
# Emp_details.Print()


# Some more example


# A Python program to demonstrate inheritance

# Base or Super class. Note object in bracket.
# (Generally, object is made ancestor of all classes)
# In Python 3.x "class Person" is
# equivalent to "class Person(object)"


# class Person(object):

# 	# Constructor
# 	def __init__(self, name):
# 		self.name = name

# 	# To get name
# 	def getName(self):
# 		return self.name

# 	# To check if this person is an employee
# 	def isEmployee(self):
# 		return False


# # Inherited or Subclass (Note Person in bracket)
# class Employee(Person):

# 	# Here we return true
# 	def isEmployee(self):
# 		return True


# # Driver code
# emp = Person("Geek1") # An Object of Person
# print(emp.getName(), emp.isEmployee())

# emp = Employee("Geek2") # An Object of Employee
# print(emp.getName(), emp.isEmployee())


# Super with Inheritance

# parent class
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



# Adding Property Inheritance

# parent class
# class Person():
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def display(self):
#         print(self.name, self.age)

# # child class
# class Student(Person):
#     def __init__(self, name, age, dob):
#         self.sName = name
#         self.sAge = age
#         self.dob = dob
#         # inheriting the properties of parent class
#         super().__init__("Rahul", age)

#     def displayInfo(self):
#         print(self.sName, self.sAge, self.dob)

# obj = Student("Mayank", 23, "16-03-2000")
# obj.display()
# obj.displayInfo()


# Multi-Level Inheritance

# When we have a child and grandchild relationship. This means that a child class will inherit from its parent class, which in turn is inheriting from its parent class.

# A Python program to demonstrate inheritance

# Base or Super class. Note object in bracket.
# (Generally, object is made ancestor of all classes)
# In Python 3.x "class Person" is
# equivalent to "class Person(object)"

class Base(object):

	# Constructor
	def __init__(self, name):
		self.name = name

	# To get name
	def getName(self):
		return self.name


# Inherited or Sub class (Note Person in bracket)
class Child(Base):

	# Constructor
	def __init__(self, name, age):
		Base.__init__(self, name)
		self.age = age

	# To get name
	def getAge(self):
		return self.age

# Inherited or Sub class (Note Person in bracket)


class GrandChild(Child):

	# Constructor
	def __init__(self, name, age, address):
		Child.__init__(self, name, age)
		self.address = address

	# To get address
	def getAddress(self):
		return self.address


# Driver code
g = GrandChild("Geek1", 23, "Noida")
print(g.getName(), g.getAge(), g.getAddress())
