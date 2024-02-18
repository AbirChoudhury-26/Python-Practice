"""
Python String split() method splits a string into a list of strings after breaking the given string by the specified separator.
"""


string = "one,two,three"
words = string.split(',')
print(words)


""" Syntax: str.split(separator, maxsplit) """
"""
Separator: This is a delimiter. The string splits at this specified separator. If is not provided then any white space is a separator.
Maxsplit: It is a number, that tells us to split the string into a maximum of the provided number of times. If it is not provided then the default is -1 which means there is no limit.

"""