import csv

# Data to write
data = [
    ["Name", "Age", "City"],
    ["Alice", 25, "New York"],
    ["Bob", 30, "Los Angeles"],
    ["Charlie", 28, "Chicago"]
]

# Writing to CSV
with open("data.csv", mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)

print("CSV file written successfully.")
