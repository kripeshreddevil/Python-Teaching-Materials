filename = "q2.txt"

with open(filename, "w") as file:
    # Writing multiple lines to the file
    file.write("Line 1\n")
    file.write("Line 2\n")
    file.write("Line 3\n")

print(f"Text has been written to {filename}")
