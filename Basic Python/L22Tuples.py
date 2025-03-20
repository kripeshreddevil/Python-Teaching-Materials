# Tuples are sequences of values separated by commas
t = (12345, 54321, 'hello!')
print(t)

print("Tuple t:", t)           # Output: (12345, 54321, 'hello!')
print("First element t[0]:", t[0])  # Output: 12345

# Tuples may be nested
u = t, (1, 2, 3, 4, 5)
print("Nested tuple u:", u)    # Output: ((12345, 54321, 'hello!'), (1, 2, 3, 4, 5))

# Tuples can contain mutable objects
v = ([1, 2, 3], [3, 2, 1])
print("Tuple containing mutable objects v:", v)  # Output: ([1, 2, 3], [3, 2, 1])

# Creating empty and single-item tuples
empty = ()  # Empty tuple
singleton = 'hello',  # Single-item tuple (note the trailing comma)
print("Empty tuple:", empty)         # Output: ()
print("Singleton tuple:", singleton) # Output: ('hello',)
print("Length of empty tuple:", len(empty))  # Output: 0
print("Length of singleton tuple:", len(singleton))  # Output: 1

# Tuple packing
t = 12345, 54321, 'hello!'  # Values are packed into a tuple
print("Tuple packing t:", t)  # Output: (12345, 54321, 'hello!')

# Tuple unpacking
x, y, z = t  # Values from the tuple are unpacked into variables
print("Unpacked x:", x)  # Output: 12345
print("Unpacked y:", y)  # Output: 54321
print("Unpacked z:", z)  # Output: hello!

# Note: Sequence unpacking works for any sequence, not just tuples
