with open("q21.txt","r") as file:
    total = 0
    for item in file:
        print(type(item))
        total = total + int(item)
    print(total)



