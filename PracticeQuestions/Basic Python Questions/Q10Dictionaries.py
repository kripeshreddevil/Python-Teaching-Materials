numbers = {
    1: "One",
    2: "Two",
    3: "Three",
    4: "Four",
    5: "Five",
    6: "Six",
    7: "Seven",
    8: "Eight",
    9: "Nine",
    0: "Zero"
}

user_input = input("Enter the number:")
x = len(user_input)
for num in range(x):
    change = int(user_input[num])
    print(f'{numbers.get(change, "!")}',end=" ")
