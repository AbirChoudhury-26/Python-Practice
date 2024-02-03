# Polymorphism

"""
Polymorphism simply means having many forms. For example, we need to determine if the given species of birds fly or not, using polymorphism we can do this using a single function.
"""

# class Bird:

# 	def intro(self):
# 		print("There are many types of birds.")

# 	def flight(self):
# 		print("Most of the birds can fly but some cannot.")

# class sparrow(Bird):

# 	def flight(self):
# 		print("Sparrows can fly.")

# class ostrich(Bird):

# 	def flight(self):
# 		print("Ostriches cannot fly.")

# obj_bird = Bird()
# obj_spr = sparrow()
# obj_ost = ostrich()

# obj_bird.intro()
# obj_bird.flight()

# obj_spr.intro()
# obj_spr.flight()

# obj_ost.intro()
# obj_ost.flight()

# A simple Python function to demonstrate 
# Polymorphism

# def add(x, y, z = 0): 
# 	return x + y+z

# # Driver code 
# print(add(2, 3))
# print(add(2, 3, 4))



# Polymorphism with class Methods

class India():
	def capital(self):
		print("New Delhi is the capital of India.")

	def language(self):
		print("Hindi is the most widely spoken language of India.")

	def type(self):
		print("India is a developing country.")

class USA():
	def capital(self):
		print("Washington, D.C. is the capital of USA.")

	def language(self):
		print("English is the primary language of USA.")

	def type(self):
		print("USA is a developed country.")

obj_ind = India()
obj_usa = USA()
for country in (obj_ind, obj_usa):
	country.capital()
	country.language()
	country.type()

# Polymorphism with Inheritance
	
# class Bird:
# 	def intro(self):
# 		print("There are many types of birds.")
		
# 	def flight(self):
# 		print("Most of the birds can fly but some cannot.")

# class sparrow(Bird):
# 	def flight(self):
# 		print("Sparrows can fly.")
		
# class ostrich(Bird):
# 	def flight(self):
# 		print("Ostriches cannot fly.")
	
# obj_bird = Bird()
# obj_spr = sparrow()
# obj_ost = ostrich()

# obj_bird.intro()
# obj_bird.flight()

# obj_spr.intro()
# obj_spr.flight()

# obj_ost.intro()
# obj_ost.flight()
	


# Polymorphism with a Function & Objects


def func(obj):
	obj.capital()
	obj.language()
	obj.type()

obj_ind = India()
obj_usa = USA()

func(obj_ind)
func(obj_usa)
