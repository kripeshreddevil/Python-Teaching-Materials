# # List of strings

# fruits = ["Apple", "Banana", "Cherry"]

# Define the filename
# filename = "q3.txt"

# Open the file in write mode
# with open(filename, "w") as file:
#     # Write each fruit on a new line
#     for fruit in fruits:
#         file.write(fruit + "\n")
#
# print(f"List has been written to {filename}")

# Alternative Approach Using writelines()

# fruits = ["Apple\n", "Banana\n", "Cherry\n"]
#
# with open("q3.txt", "w") as file:
#     file.writelines(fruits)


fruits = ["Apple", "Banana", "Cherry"]

with open("q3.txt", "w") as file:
    file.writelines(f"{frt}\n" for frt in fruits)

# Key Difference: writelines() requires \n to be added manually in each element.