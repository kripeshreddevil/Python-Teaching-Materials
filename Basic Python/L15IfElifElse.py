number = 30

if number % 2 == 0:
    print("The number is divisible by 2.")
if number % 3 == 0:
    print("The number is divisible by 3.")
if number % 5 == 0:
    print("The number is divisible by 5.")



if grade > 80:
    print ("Dist")

if grade > 60:
    print("First")

if grade > 40:
    print("pass")

if grade < 40:
    print("fail")

# When to Use Which?
# Use multiple if statements if the conditions are independent
# and you may want multiple blocks of code to execute.
# Use if-elif-else if the conditions are mutually exclusive
# (only one condition can be true at a time).