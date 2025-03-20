with open("q15.txt", "r") as file:
    key_value_dict = {line.split(":")[0].strip(): line.split(":")[1].strip() for line in file}

print(key_value_dict)
