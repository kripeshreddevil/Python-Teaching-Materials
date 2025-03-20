try:
    age = int(input("Enter the age:"))
    risk_score = int(input("Enter the risk score."))
    risk = risk_score / age
    print(risk)
except ValueError:
    print("Age should be numeric.")
except ZeroDivisionError:
    print("Age cannot be zero.")