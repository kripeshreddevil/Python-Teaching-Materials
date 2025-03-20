numbers = [1, 3, 21, 2, 4, 44, 2]
for num in numbers:
    if num < numbers[0]:
        numbers[0] = num
print(numbers[0])