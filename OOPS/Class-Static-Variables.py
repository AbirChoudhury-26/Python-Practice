# # Python program to show that the variables with a value 
# # assigned in class declaration, are class variables

# # Class for Computer Science Student
# class CSStudent:
# 	stream = 'cse'				 # Class Variable
# 	def __init__(self,name,roll):
# 		self.name = name		 # Instance Variable
# 		self.roll = roll		 # Instance Variable

# # Objects of CSStudent class
# a = CSStudent('Geek', 1)
# b = CSStudent('Nerd', 2)

# print(a.stream) # prints "cse"
# print(b.stream) # prints "cse"
# print(a.name) # prints "Geek"
# print(b.name) # prints "Nerd"
# print(a.roll) # prints "1"
# print(b.roll) # prints "2"

# # Class variables can be accessed using class
# # name also
# print(CSStudent.stream) # prints "cse"

# # Now if we change the stream for just a it won't be changed for b
# a.stream = 'ece'
# print(a.stream) # prints 'ece'
# print(b.stream) # prints 'cse'

# # To change the stream for all instances of the class we can change it 
# # directly from the class
# CSStudent.stream = 'mech'

# print(a.stream) # prints 'ece'
# print(b.stream) # prints 'mech'

""""
Advantages:
Memory efficiency: Since static variables are shared among all instances of a class, they can save memory by avoiding the need to create multiple copies of the same data.
Shared state: Static variables can provide a way to maintain shared state across all instances of a class, allowing all instances to access and modify the same data.
Easy to access: Static variables can be accessed using the class name itself, without needing an instance of the class. This can make it more convenient to access and modify the data stored in a static variable.
Initialization: Static variables can be initialized when the class is defined, making it easy to ensure that the variable has a valid starting value.
Readability: Static variables can improve the readability of the code, as they clearly indicate that the data stored in the variable is shared among all instances of the class.
"""

"""
Disadvantages:
Inflexibility: Static variables can be inflexible, as their values are shared across all instances of the class, making it difficult to have different values for different instances.
Hidden dependencies: Static variables can create hidden dependencies between different parts of the code, making it difficult to understand and modify the code.
Thread safety: Static variables can be problematic in a multithreaded environment, as they can introduce race conditions and synchronization issues if not properly synchronized.
Namespace pollution: Static variables can add to the namespace of the class, potentially causing name conflicts and making it harder to maintain the code.
Testing: Static variables can make it more difficult to write effective unit tests, as the state of the static variable may affect the behavior of the class and its methods.
"""