import random

number = random.randrange(1, 1000)
guesses = 0
guess = int(input("Guess my number between 1 and 1000: "))

while guess != number:
    guesses += 1
    print("Sorry, wrong answer.")
    if guess > number:
        print("My number is closer to 0")
        guess = int(input("Guess again: ")
    else:
        print("My number is closer to 1000")
        guess = int(input("Guess again: ")

print("Good job", number, "is my number")
