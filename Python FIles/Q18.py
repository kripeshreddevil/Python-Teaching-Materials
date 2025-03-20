menu_dict = {}

# Read the file and store data in a dictionary
with open("q18.txt", "r") as file:
    for line in file:
        dish, price = line.strip().split(", ")
        menu_dict[dish] = float(price)  # Convert price to float

# Display the dictionary
print(menu_dict)
