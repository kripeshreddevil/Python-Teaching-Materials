password = input("Enter your password: ")

if len(password) < 6:
    print("Your password is too short.")
elif password.isdigit() and password.isalpha():
    print("Your password is strong.")
else:
    print("Your password could be stronger.")
