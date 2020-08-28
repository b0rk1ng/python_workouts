"""
Guessing a number between 1 and 100
"""

import random


def guessing_game():
    """
    Guess numbers untill correct guess
    No input or output
    """
    number = random.randint(1, 100)

    while True:
        guess = int(input("Guess a number... "))

        if guess > number:
            print(f"{guess} is too high, try again")

        elif guess < number:
            print(f"{guess} is too low, try again")

        else:
            print(f"You are right, it is {guess}!")
            break


if __name__ == "__main__":
    guessing_game()
