age = int(input("Enter your age: "))
print("You will be", age + 1, "years old next year.")

birth_year = 2025 - age
print("You were born in approximately", birth_year)

decades = age // 10
print("You have lived for", decades, "decades.")

if age < 18:
    print("You are a minor.")
elif age < 65:
    print("You are an adult.")
else:
    print("You are a senior citizen.")
