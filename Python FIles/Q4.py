# Tuple of numbers
numbers = (10, 20, 30)

# Define the filename
filename = "q4.txt"

# Open the file in write mode
with open(filename, "w") as file:
    # Write each number on a new line
    for num in numbers:
        file.write(str(num) + "\n")

print(f"Tuple has been written to {filename}")

# Alternative Approach Using writelines()
#
numbers = (10, 20, 30)

with open("q4.txt", "w") as file:
    file.writelines(f"{num}\n" for num in numbers)

print("Tuple has been written using writelines().")

# Key Difference: writelines() writes multiple lines at once using generator expression (f"{num}\n" for num in numbers).

numbers = (10, 20, 30)

with open("q4.txt", "w") as file:
    file.writelines(numbers)

#The above code throws an error as writelines() expects an iterable of strings, but numbers is a tuple of integers.

# Solution:

numbers = (10, 20, 30)

with open("q4.txt", "w") as file:
    file.writelines(f"{num}\n" for num in numbers)  # Convert numbers to strings
