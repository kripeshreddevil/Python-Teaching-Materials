# Reading an HTML file
with open("index.html", "r") as file:
    content = file.read()

print(content)  # Prints the full HTML content
