with open("example.txt", "r+") as file:
    content = file.read()
    file.write("\nNew line added at the end.")
    print(content)

print("Read and write operation completed!")
