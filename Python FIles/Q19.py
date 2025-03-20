with open("q19.txt", "r") as file:
    lines = file.readlines()  # Read all lines into a list
    line_count = len(lines)   # Get the length of the list

print(f"Total number of lines: {line_count}")
