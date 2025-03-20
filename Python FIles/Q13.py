with open("q13.txt", "r") as file:
    numbers_tuple = tuple(int(line.strip()) for line in file)

print(numbers_tuple)
