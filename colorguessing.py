import random

def main():
    """Start a color guessing game."""
    print("Guess the color!")

    rainbow = [
        "red",
        "orange",
        "yellow",
        "green",
        "blue",
        "indigo",
        "violet"
    ]


    x = random.choice(rainbow)
    print(x)
    guess = None

    while x != guess:
        guess = str(input("What color am i thinking of? "))

        if x == guess:
            print("You guessed {}. Congrutulations you got it right!".format(guess))
            break
        else:
            print("You guessed {}. Unfortunately its wrong. Try again!".format(guess))

main()