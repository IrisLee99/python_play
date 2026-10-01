ticket_price = 0
userAge = int(input("Enter your age: "))
isMember = input("Are you a member? (yes/no): ").strip().lower() == "yes"

if userAge <= 12:
    ticket_price = 6
elif userAge <= 17:
    ticket_price = 7
else:
    ticket_price = 8

if isMember:
    ticket_price -= 2

print(f"The ticket price is: £{ticket_price}")