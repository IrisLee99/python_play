import random


def play():
    secret = random.randint(1, 100)
    attempts = 0
    print("Guess the Number!")
    print("I'm thinking of a number from 1 to 100.")

    while True:
        try:
            guess = int(input("Your guess: "))
        except ValueError:
            print("Please enter a whole number.")
            continue

        if not 1 <= guess <= 100:
            print("Choose a number between 1 and 100.")
            continue

        attempts += 1
        if guess < secret:
            print("Too low!")
        elif guess > secret:
            print("Too high!")
        else:
            print(f"You got it in {attempts} attempt(s)!")
            break


if __name__ == "__main__":
    play()