import random

def guessing_game():
    number = random.randint(1, 100)

    while True:
        guess = int(input("Guess a number... "))

        if guess > number:
            print(f'{guess} is too high, try again')

        elif guess < number:
            print(f'{guess} is too low, try again')

        else:
            print(f'You are right, it is {guess}!')
            break

if __name__ == '__main__':
    guessing_game()
