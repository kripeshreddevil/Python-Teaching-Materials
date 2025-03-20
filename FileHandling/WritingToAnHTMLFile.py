# Writing to an HTML file
html_content = """<!DOCTYPE html>
<html>
<head>
    <title>My First HTML Page</title>
</head>
<body>
    <h1>Hello, World!</h1>
    <p>Welcome to my webpage.</p>
</body>
</html>"""

with open("index.html", "w") as file:
    file.write(html_content)

print("HTML file created successfully.")
