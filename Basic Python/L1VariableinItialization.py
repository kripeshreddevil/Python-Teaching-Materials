# Initial values
sales = 1000  # Initial sales amount in dollars
cost = 600  # Initial cost of products

# Addition shorthand (sales increase by 200)
sales += 200
sales = sales + 200# Equivalent to sales = sales + 200
print("Sales after increase:", sales)  # Output: 1200

# Subtraction shorthand (cost decreases by 50)
cost -= 50  # Equivalent to cost = cost - 50
print("Cost after decrease:", cost)  # Output: 550

# Multiplication shorthand (sales doubled due to growth)
sales *= 2  # Equivalent to sales = sales * 2
print("Sales after doubling:", sales)  # Output: 2400

# Division shorthand (cost halved due to better pricing)
cost /= 2  # Equivalent to cost = cost / 2
print("Cost after halving:", cost)  # Output: 275.0

# Modulus shorthand (find remainder after dividing sales by 100)
remainder = sales % 100  # Equivalent to remainder = sales % 100
print("Remainder after dividing sales by 100:", remainder)  # Output: 0

# Exponentiation shorthand (sales growth rate raised to the power of 3)
growth_rate = 1.5
growth_rate **= 3  # Equivalent to growth_rate = growth_rate ** 3
print("Growth rate raised to the power of 3:", growth_rate)  # Output: 3.375
