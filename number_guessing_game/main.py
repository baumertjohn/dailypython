# Number Guessing Game
# User gets 10 chances to guess number between 1 and 100

import random

RANDOM_NUMBER = random.randint(1, 100)
win = False

print("Welcome to the Number Guessing Game!")
print("I have selected a number between 1 and 100.")
print("You have 10 attempts to guess the correct number.")

for guess_count in range(1, 11):
    user_guess = int(input("Enter your guess: "))
    if user_guess == RANDOM_NUMBER:
        print(
            f"Congratulations! You've guessed the correct number in {guess_count} attempts."
        )
        win = True
        break
    elif user_guess < RANDOM_NUMBER:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")

if not win:
    print("You lose!")
