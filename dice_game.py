import random

player1 = input('Enter play one\'s name:')
player2 = input('Enter play two\'s name:')

dice_total = lambda: random.randint(1, 6) + random.randint(1, 6)
roll1 = dice_total()
roll2 = dice_total()

print(f"{player1} rolled: {roll1}")
print(f"{player2} rolled: {roll2}")

if roll1 > roll2:
    print(f"{player1} wins!")
elif roll2 > roll1:
    print(f"{player2} wins!")
else:
    print("It's a tie!")