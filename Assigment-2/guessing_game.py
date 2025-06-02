import random

number = random.randint(1, 100)
attempts = 0

while True:
    try:
        guess = int(input("1.To exit press Zero.\n2.Guess a number between 1 and 100:  "))
        attempts += 1
        if guess == 0 : break
        if guess < number:
            print("Too low")
        elif guess > number:
            print("Too high")
        else:
            print("Correct! Attempts:", attempts)
            break
    except ValueError:
        print("Please enter a valid number")

print("Thank you for playing!")