with open("example.txt", "r+") as file:
    file.seek(0)  # Move cursor to the beginning
    file.write("Overwriting content!")
    file.truncate()  # Remove extra old content if new content is shorter
