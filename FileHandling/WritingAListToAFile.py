lines = ["Line 1\n", "Line 2\n", "Line 3\n"]

with open("example.txt", "w") as file:
    file.writelines(lines)

print("List written to file successfully!")
