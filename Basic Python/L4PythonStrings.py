# x = "Python for 'Beginners'"
# print(x)
#
# course_info = "Python for 'Beginners'"
# substring_info = course_info[0:3]
# print(substring_info)
# #
# #
# name = "Jennifer"
# print(name[:-2])
#
#
# message = "It's a string"
# print(message)
#
# message = '"Beautiful is better than ugly.", Said Tim Peters'
# print(message)
# message = 'He said, "We\'re the  people of this country"'
# print(message)
# message = r'C:\python\bin'
# print(message)
#
# mail = ("Dear Sir,"
# "The python class is from 10 to 11"
# "Regards,"
# "Coordinator")
#
# print(mail)
#
# new_mail = '''
# Dear Sir,
#
# The python class is from 10 to 11
#
# Regards,
# Coordinator
# '''
#
# print(new_mail)

#
# x = ("Dear User,"
#      "You cannot proceed to this page."
#      "Regards")
# print(x)

#the following print statement is for multiline strings
# print('''Dear Sir,
#        I am feeling tired.
#        Please end the class right now.
#        '''
#        )

# message = 'He said, "We\'re the  people of this country"'
# print(message)
#
# #multiline string
# help_message = '''
# Usage: mysql command
#     -h hostname
#     -d database name
#     -u username
#     -p password
# '''
#
# print(help_message)
#
#
#
# #Using variables in Python strings with the f-strings
#
# name = 'John'
# message = f'Hi {name}'
# print(message)
#
# x = 5
# print(f'The value of x is {x}')

#
#
#Concatenating Python strings
# When you place the string literals next to each other,
# Python automatically concatenates them into one string. For example:


# greeting = 'Good ' 'Morning!'
# print(greeting)
#
# Python strings are immutable.
# It means that you cannot change the string.
# For example, you’ll get an error if you update one or more characters in a string:
#


str1 = "Python String"
str1[0] = 'J'
print(str1)

# # @Python strings are immutable
#
# str1 = "Python String"
# str1 = 'J' + str1[1:]
# print(str1)


# first_num = 5
# second_num = 10
# print("The sum is ", first_num+second_num)
# print("The sum of " + str(first_num) + " and " + str(second_num) + " is " + str(first_num+second_num))
# print(f'The sum of {first_num} and {second_num} is {first_num+second_num}')
