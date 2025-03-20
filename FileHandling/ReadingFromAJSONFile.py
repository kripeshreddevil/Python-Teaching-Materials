import json

# Reading from JSON
with open("data.json", "r") as file:
    data = json.load(file)

print(data)  # Prints the JSON content as a Python dictionary
