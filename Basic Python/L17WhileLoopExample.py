import random

secret_number = random.randint(1,10)
print(secret_number)
count = 1
while count <= 3:
    user_input = int(input('Please enter your guess.'))
    if user_input == secret_number:
        print(f'Congratulations, you guessed in {count} attempt.')
        quit()
    count += 1
print("You have reached the guess limit.")




