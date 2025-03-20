dish_name = input("Enter the dish name: ")
price = input("Enter the price of the dish: ")

with open("q9.txt", "a") as file:
    file.write(f"{dish_name}, {price}\n")
