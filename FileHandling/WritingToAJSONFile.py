import json

# Data to write
data = {
    "employees": [
        {"name": "Alice", "age": 25, "city": "New York"},
        {"name": "Bob", "age": 30, "city": "Los Angeles"},
        {"name": "Charlie", "age": 28, "city": "Chicago"}
    ]
}

# Writing to JSON
with open("data.json", "w") as file:
    json.dump(data, file, indent=4)

print("JSON file written successfully.")
