number = int(input("Enter a number: "))

if number % 2 == 0:
    if number % 3 == 0:
        print(f"{number} is even and divisible by 3.")
    else:
        print(f"{number} is even but not divisible by 3.")
else:
    print(f"{number} is odd.")
