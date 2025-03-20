instruction = input("Welcome to the Car game. Enter 'help' to understand the game: ").lower()
has_started = True
while instruction != "quit":
    if instruction == "start":
        if has_started:
            print("Car has already Started.")
        else:
            has_started = True
            print("Car started....")
    elif instruction == "stop":
        if not has_started:
            print("Car is already stopped.")
        else:
            has_started = False
            print("Car stopped....")

    elif instruction == "help":
        print('''
start - to start the car
stop - to stop the car
quit - to exit
''')
    else:
        print("I don't understand that.")
    instruction = input("> ").lower()

print("Exiting the game...")
