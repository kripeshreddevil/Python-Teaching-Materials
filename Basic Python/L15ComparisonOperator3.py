weight = int(input("Enter your weight (either in pound or kilos) "))
weight_unit = (input("Enter 'K' if your weight is in Kilos or 'P' if your weight is in Pound. ")).lower()
if weight_unit == 'k':
    print(f'Your weight in pound is : {weight / 0.45}')
elif weight_unit == 'p':
    print(f'Your weight in kilogram is : {weight*0.45}')
else:
    print("Please enter a valid weight unit.")


