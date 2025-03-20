import sys

a = 5
print("Type of a: ", type(a))
print("Size of a: ", sys.getsizeof(a), "bytes")

b = 5.0
print("\nType of b: ", type(b))
print("Size of b: ", sys.getsizeof(b), "bytes")

c = 2 + 4j
print("\nType of c: ", type(c))
print("Size of c: ", sys.getsizeof(c), "bytes")