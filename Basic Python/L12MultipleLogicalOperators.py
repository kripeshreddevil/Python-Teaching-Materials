has_high_income = False
has_good_credit = True
has_criminal_record = False
if (has_high_income or has_good_credit) and not has_criminal_record:
    print("You are eligible for loan.")
else:
    print("You are not eligible for loan.")