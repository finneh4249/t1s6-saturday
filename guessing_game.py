# Guessing Game

import random
guess_num = random.randint(1, 50)

user_guess = None

while user_guess != guess_num:
    user_guess = int(input("\nGuess a number between 1 and 50: "))

    if user_guess < guess_num:
        print("\nOh no! Too low :(")
    elif user_guess > guess_num:
        print("\nOh no! Too high :(")

print("\n*** Well guessed! You win! ***")
