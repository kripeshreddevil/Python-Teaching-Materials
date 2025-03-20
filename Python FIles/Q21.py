myList = [1,2,3,4,5]

with open("q21.txt","w") as file:
    for num in myList:
        file.write(f'{num} \n')