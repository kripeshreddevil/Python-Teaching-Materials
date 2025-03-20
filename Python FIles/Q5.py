colors = {"Red", "Green", "Blue"}

with open("q5.txt", "w") as file:
    for color in colors:
        file.write(color + "\n")


# Alternative Approach: Using writelines()

colors = {"Red", "Green", "Blue"}

with open("q5.txt", "w") as file:
    file.writelines(color + "\n" for color in colors)  # Using generator expression

