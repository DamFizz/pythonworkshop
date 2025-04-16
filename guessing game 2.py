import random
def main():
    """Start a number guessing game between 1 - 100."""
    print("Guess the number!")

    x = random.randint(1, 100)
    guess = None

    while x != guess:

        guess = int(input("Pink a number between 1 - 100: "))

        if x == guess:
            print("You guessed it!")
        elif x > guess:
            print("Too low!")
        elif x < guess:
            print("Too high!")

main()