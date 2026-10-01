print("Welcome to the tax calculator!")

income = float(input("Enter your income: "))
lower_tax_rate = 0.2  # 20% tax rate 
higher_tax_rate = 0.4  # 40% tax rate 
if income > 50000:
    tax = 50000*lower_tax_rate + (income - 50000) * higher_tax_rate
else:
    tax = 50000*lower_tax_rate
print("Your estimated tax is:", tax)