# Method-1

"""Using an “in” operator which is used as a comparison operator"""


# MyString1 = "A geek in need is a geek indeed"
# reqString="ned"
# if reqString in MyString1:
# 	print("Yes! it is present in the string")
# else:
# 	print("No! it is not present")
 


 # Method- 2

"""
Split Method-  First split the given string into words and store them in a variable  then using the if condition, check if a substring is present in the given string or not.
"""

# input strings str1 and substr
string = "geeks for geeks" # or string=input() -> taking input from the user
substring = "geeks" # or substring=input()

# splitting words in a given string
s = string.split()
print(s)  # This returns a list of substrings of original String
# checking condition
# if substring is present in the given string then it gives output as yes
if substring in s:
	print("yes")
else:
	print("no")


# Method-3
	
"""
 Find Method-checks if a substring is present in the string, which is done in one line. find() function returns -1 if it is not found, else it returns the first occurrence
"""

def check(string, sub_str):
	if (string.find(sub_str) == -1):
		print("NO")
	else:
		print("YES")


# driver code
string = "geeks for geeks"
sub_str = "geek"
check(string, sub_str)


# Method-4

" Index Method"

any_string = "Geeks for Geeks substring "
start = 0
end = 1000
print(any_string.index('substring', start, end))
