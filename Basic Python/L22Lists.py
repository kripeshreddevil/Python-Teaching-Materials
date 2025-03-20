# members = ["Mr. Brown", "Mr. White", "Mr. Black", "Mr. Grey", "Mr. Pink", "Mr. Red"]
# print(members[2:4])
# print(members[:2])



squares = [1, 4, 19, 16, 25]
squares[2] = 5

print(squares)


# print(squares + [36,49,81,100])
#
# squares.append(121)
#
# squares.append(243)
#
# print(squares)

#
# rgb = ["Red", "Green", "Blue"]
#
# rgba = rgb
#
# rgb.append("Alpha")
#
# correct_rgba = rgba[:]
#
# correct_rgba.append("Beta")
# print(correct_rgba)
#
# print(correct_rgba)

# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
# print(len(letters))
# letters[3:6] = ['1', '2', '3']
# print(letters)
#
# letters[3:6] = []
# print(letters)
#
# letters[:] = []
# print(letters)
#
# a = ['a', 'b', 'c']
# n = [1, 2, 3]
#
# x = [a,n]
# print(x[0][2])

# x = 22
# x1 = [22, "Ram", 2.4, True]
# print(type(x1))

squares = [1, 4, 9, 16, 25]

print(squares[-3:])

print(squares + [36, 49, 64, 81, 100])


cubes = [1, 8, 27, 65, 125]

cubes[3] = 64

print(cubes)

rgb = ["Red", "Green", "Blue"]

rgba = rgb

rgba.append("Beta")

print(rgba)

correct_rgba = rgba[:]

print(correct_rgba)

correct_rgba[-1] = "Alpha"

print(correct_rgba)

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

print(letters[2:5])

letters[2:5] = []

print(letters)

print(len(letters))

rgb = ["Red", "Green", "Blue"]
rgb.sort()
print(rgb)