data = {"name": "Alice", "age": 25, "city": "New York"}

with open("q6.txt", "w") as file:
    for key, val in data.items():
        file.write(f"{key}: {val}\n")  # Write key-value pair with a newline

#
#
# # Alternative Approach: Using writelines()
#
# data = {"name": "Alice", "age": 25, "city": "New York"}
#
# with open("q6.txt", "w") as file:
#     file.writelines(f"{key}: {value}\n" for key, value in data.items())  # Using generator expression
#
