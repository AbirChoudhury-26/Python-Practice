# # Python program to demonstrate
# # opening a file


# # Open function to open the file "myfile.txt"
# # (same directory) in read mode and store
# # it's reference in the variable file1

# file1 = open("myfile1.txt")

# # Reading from file
# print(file1.read())

# file1.close()


# WRITING  a file
"""
File_object = open(r"File_Name", "Access_Mode")
"""
# Open function to open the file "MyFile1.txt" 
# (same directory) in read mode and 
# file1 = open("MyFile.txt", "w") 

# # store its reference in the variable file1 
# # and "MyFile2.txt" in D:\Text in file2 
# file2 = open(r"D:\Text\MyFile2.txt", "w+") 


# CLOSING a file

# Opening and Closing a file "MyFile.txt" 
# for object name file1. 
# file1 = open("MyFile.txt", "w") 
# file1.close() 


# Python program to demonstrate
# writing to file

# Opening a file
# file1 = open('myfile.txt', 'w')
# L = ["This is Delhi \n", "This is Paris \n", "This is London \n"]
# s = "Hello\n"

# # Writing a string to file
# file1.write(s)

# # Writing multiple strings
# # at a time
# file1.writelines(L)

# # Closing file
# file1.close()

# # Checking if the data is
# # written to file or not
# file1 = open('myfile.txt', 'r')
# print(file1.read())
# file1.close()


# Python program to illustrate
# Append vs write mode
# file1 = open("myfile.txt", "w")
# L = ["This is Delhi \n", "This is Paris \n", "This is London \n"]
# file1.writelines(L)
# file1.close()

# # Append-adds at last
# file1 = open("myfile.txt", "a") # append mode
# file1.write("Today \n")
# file1.close()

# file1 = open("myfile.txt", "r")
# print("Output of Readlines after appending")
# print(file1.read())
# print()
# file1.close()

# # Write-Overwrites
# file1 = open("myfile.txt", "w") # write mode
# file1.write("Tomorrow \n")
# file1.close()

# file1 = open("myfile.txt", "r")
# print("Output of Readlines after writing")
# print(file1.read())
# print()
# file1.close()


# Program to show various ways to
# write data to a file using with statement

# L = ["This is Delhi \n", "This is Paris \n", "This is London \n"]

# # Writing to file
# with open("myfile.txt", "w") as file1:
# 	# Writing data to a file
# 	file1.write("Hello \n")
# 	file1.writelines(L)

# # Reading from file
# with open("myfile.txt", "r+") as file1:
# 	# Reading form a file
# 	print(file1.read())
