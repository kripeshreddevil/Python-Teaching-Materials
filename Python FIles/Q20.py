with open("q20.txt", "r") as file:
    for line in file:
        if "excellent" in line.lower():  # Use .lower() to make case-insensitive
            print(line.strip())  # Display the line without extra spaces/newlines
