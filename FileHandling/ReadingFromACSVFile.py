import csv

# Reading from CSV
with open("data.csv", mode="r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)  # Prints each row as a list

