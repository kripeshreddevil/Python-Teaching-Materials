# # Creating a dictionary
# my_dict = {"name": "Alice", "age": 25, "city": "New York"}
#
# print("Dictionary:", my_dict)
# print("Name:", my_dict["name"])  # Accessing value by key
# print("Type:", type(my_dict))
#
# # Creating a dictionary
# person = {"name": "John", "age": 30, "city": "London"}
#
# # Accessing values
# print("Name:", person["name"])  # Output: John
#
# # Adding a new key-value pair
# person["job"] = "Engineer"
# print("After adding job:", person)
#
# # Updating an existing value
# person["age"] = 35
# print("After updating age:", person)
#
# # Removing a key-value pair using del
# del person["city"]
# print("After deleting city:", person)
#
# # Getting keys and values
# print("Keys:", person.keys())    # Output: dict_keys(['name', 'age', 'job'])
# print("Values:", person.values())  # Output: dict_values(['John', 35, 'Engineer'])
#
# # Checking if a key exists
# print("Is 'name' in dictionary?", "name" in person)  # Output: True

my_set = {1,3,22,21, 2, 3, 4, 4, 5}  # Duplicates are automatically removed

print("Set:", my_set)  # Output: {1, 2, 3, 4, 5}
print("Type:", type(my_set))