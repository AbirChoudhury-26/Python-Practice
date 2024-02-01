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

def add(x, y, z = 0): 
	return x + y+z

# Driver code 
print(add(2, 3))
print(add(2, 3, 4))
