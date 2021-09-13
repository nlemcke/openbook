def guessing_game(low=0, hi=100):
    """Guess the number that the computer picked between hi and low"""
    import random
    number = random.randrange(low, hi)
    guess = int(input("Guess my number between " + str(low) + "and " + str(hi) + ": "))
    print(guess)

guessing_game()
