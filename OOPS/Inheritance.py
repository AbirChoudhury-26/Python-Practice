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


class Person(object):

	# Constructor
	def __init__(self, name):
		self.name = name

	# To get name
	def getName(self):
		return self.name

	# To check if this person is an employee
	def isEmployee(self):
		return False


# Inherited or Subclass (Note Person in bracket)
class Employee(Person):

	# Here we return true
	def isEmployee(self):
		return True


# Driver code
emp = Person("Geek1") # An Object of Person
print(emp.getName(), emp.isEmployee())

emp = Employee("Geek2") # An Object of Employee
print(emp.getName(), emp.isEmployee())
