def hello():
    print("Welcome to Python Tutorial")

print(__name__) # Hence if the  type of __name__ is main here that means the below condt. matches and exceute the given instrutions
print("Outside main function")
if __name__=="__main__":  # __main__==__main__,yes---->then Go Inside and execute the given instructions
    hello()
    name="My name is Abir and this is my file"
    print("Inside main function")
    print(name)