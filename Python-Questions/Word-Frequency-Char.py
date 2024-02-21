# Method-1 

""" Using Dictionary Comprehnesion +count()"""

# # Python3 code to demonstrate working of
# # Words Frequency in String Shorthands
# # Using dictionary comprehension + count() + split()

# # Initializing string
# test_str = 'Gfg is best . Geeks are good and Geeks like Gfg'

# # Printing original string
# print("The original string is : " + str(test_str))

# # Words Frequency in String Shorthands
# # Using dictionary comprehension + count() + split()
# res = {key: test_str.count(key) for key in test_str.split()}

# # Printing result
# print("The words frequency : " + str(res))


# Method-2

""" Using Counter + split"""

# Python3 code to demonstrate working of
# Words Frequency in String Shorthands
# Using Counter() + split()

from collections import Counter

# initializing string
test_str = 'Gfg is best . Geeks are good and Geeks like Gfg'

# printing original string
print("The original string is : " + str(test_str))

# Words Frequency in String Shorthands
# using Counter() + split()
res = Counter(test_str.split())

# Printing result
print("The words frequency : " + str(dict(res)))

