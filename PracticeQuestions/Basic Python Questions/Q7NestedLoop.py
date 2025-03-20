# for item in [8,8,2,2,8,8,2,2,2]:
#     print(item * '*')

for item in [2,2,2,2,2,2,2,9,9]:
    output = ''
    for innerItem in range(item):
        output += 'x'
    print(output)
