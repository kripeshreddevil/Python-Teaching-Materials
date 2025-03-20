name = input("Please enter your username: ")
if len(name) < 8:
    print("The user must be at least 8 characters.")
elif len(name) > 14:
    print("The name is very long. It should be upto 14 characters.")
else:
    print("Everything looks good.")
