import random
import time

def typing_speed_test():
    words = ["elephant", "giraffe", "chocolate", "buttlerfly", "adventure"]
    word = random.choice(words)

    print("welcome to typing speed test!")
    print(f"Type the following word as fast as you can: {word}")
    input("Press enter when ready...")

    start_time = time.time()
    user_input = input("Typer here:")
    end_time = time.time()
    if user_input == word:
        time_taken = round(end_time - start_time, 2)
        print(f"Great job! You typed the word in {time_taken} seconds")
    else:
        print(f"Opps! You typed the wrong word. The correct word was '{word}'. Try again!")

if __name__ == "__main__":
    typing_speed_test()