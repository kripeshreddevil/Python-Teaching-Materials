database_name = "ironman"
database_password = "stark"
print(f'''
Jarvis Welcomes you.
Would you like to login? 
Or you haven't registered yet?

Press 'x' for login
Press 'y' for registration
''')
username = ""
password = ""
user_input = input("Enter your choice.").lower()
while True:
    if user_input == 'x':
        username = input("Enter your username: ")
        password = input("Enter the password: ")
        if username == database_name and password == database_password:
            print("Welcome to Jarvis World.")
            break
        else:
            print("One of them either username or password does not match.")

    if user_input == 'y':
        name = input("Enter your Full Name: (upto 50 Characters ")
        username = input("Enter your username: (8-14 characters) ")
        password = input("Enter the password: (8-14 characters) ")
        rePassword = input("Retype the password: ")
        email = input("Enter the email:")
        if password == rePassword and len(name) < 50 and (8 < len(username) < 14) and (8 < len(password) < 14):
            print("User Created Successfully.")
        else:
            print("Either password and rePassword doesn't match or any of the criteria is not fulfilled.")

