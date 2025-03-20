numbers = [20, 21, 2, 1, 11, 21, 21, 21, 33, 23, 2, 34]
for num in numbers:
    if numbers.count(num) > 1:
        numbers.remove(num)
print(numbers)


new_list = [21, 22, 21, 22, 33, 21, 33, 5, 55]
without_dups = []
for new in new_list:
    if new not  in without_dups:
        without_dups.append(new)
print(without_dups)



