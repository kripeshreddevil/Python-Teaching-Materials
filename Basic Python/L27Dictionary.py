Footballer = [{
    "name":"Wayne Rooney",
    "jersey_no": 10,
    "is_retired": True
},
    {
    "name":"David Beckham",
    "jersey_no": 7,
    "is_retired": True
}
]

print(Footballer[1]["name"])
print(Footballer[0]["jersey_no"])
print(Footballer[0].get("is_retired"))
print(Footballer[1].get("club","Manchester United"))

# Define the dictionary
# myData = {1: "hello", 2: 22, 2: 23,  3: 33, 4: 33}
#
# # List of keys to check
# keys_to_check = [1, 2, 4]
#
# # Check if all keys exist in the dictionary
# all_keys_exist = all(key in myData for key in keys_to_check)
#
# # Print the result
# if all_keys_exist:
#     print("All keys exist in the dictionary.")
# else:
#     print("Not all keys exist in the dictionary.")
#
