money_owed = float(input("Enter the amount of money owed: "))
interest_rate = float(input("Enter the interest rate (as a percentage): "))
payment = float(input("Enter the payment amount: "))
time_period = int(input("Enter the time period (in months): "))

total_amount = money_owed * (1 + (interest_rate / 100) * (time_period / 12))

for i in range(time_period):
    interest_paid = money_owed * (interest_rate / 100) * (1 / 12)  # interest for one month
    money_owed += interest_paid - payment
    if money_owed <= 0:
        print("The loan has been fully repaid in", i+1, "months")
        print("Your last payment is: £", money_owed)
        money_owed = 0
        break

print(f"The total amount to be paid is: £{total_amount}", end=" ")