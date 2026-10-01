expenses = []

for i in range(7):
    expense = float(input(f"Enter expense {i+1}: "))
    expenses.append(expense)

total = sum(expenses)

print('you spent: £', total)