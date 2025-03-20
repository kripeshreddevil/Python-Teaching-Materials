menu_content = """Burger, 10.99
Pizza, 12.99
Pasta, 8.99"""

with open("q16.txt", "w") as file:
    file.write(menu_content)

with open("q16.txt", "r") as file:
    print(file.read())
