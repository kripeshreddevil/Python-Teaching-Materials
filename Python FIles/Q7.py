# Define staff details as a list of strings
staff_details = ["John, Manager", "Alice, Chef", "Bob, Chef"]

# Open the file in write mode and write each staff detail on a new line
with open("q7.txt", "w") as file:
    for staff in staff_details:
        file.write(staff + "\n")  # Write each entry followed by a newline


# Alternative Approach: Using writelines()

# staff_details = ["John, Manager\n", "Alice, Chef\n", "Bob, Chef\n"]
#
# with open("q7.txt", "w") as file:
#     file.writelines(staff_details)  # Write all lines at once
