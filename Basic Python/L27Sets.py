# # Creating a set
my_set = {1,3,22,21, 2, 3, 4, 4, 5}  # Duplicates are automatically removed
print("Set:", my_set)  # Output: {1, 2, 3, 4, 5}
# print("Type:", type(my_set))
#
# # Defining sets
set1 = {1, 2, 7, 3, 4}
print(set1[2])
set2 = {3, 4, 5, 6}
#
# # Union: Combines elements from both sets (no duplicates)
union_result = set1.union(set2)
print("Union of set1 and set2:", union_result)  # Output: {1, 2, 3, 4, 5, 6}
#
# # Intersection: Common elements in both sets
# intersection_result = set1.intersection(set2)
# print("Intersection of set1 and set2:", intersection_result)  # Output: {3, 4}
#
# # Difference: Elements in set1 but not in set2
difference_result = set2.difference(set1)
print("Difference of set2 and set1:", difference_result)  # Output: {1, 2}
#
# # Adding elements to a set
# set1.add(7)
# print("After adding 7 to set1:", set1)
#
# # Removing an element from a set
# set1.remove(2)
# print("After removing 2 from set1:", set1)
#
# print(sorted(set1))
#
#
my_set = {3, 1, 4, 2}
print(my_set)  # Output could be: {1, 2, 3, 4} or any other order


a = set('abracadabra')
print(a)

b = set('abracadabra')
print(b)

my_list = [9, 1, 2, 3, 5, 7]
print(set(my_list))