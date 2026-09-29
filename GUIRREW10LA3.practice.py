import random

while True:
    secret_number = random.randint(1, 25)

    guess = int(input("Guess the secret number (1-25): "))

    if guess == secret_number:
        print("Correct! You guessed the number!")
    else:
        print("Wrong! The secret number was", secret_number)

    again = input("Would you like to play again (y/n)? ")

    if again.lower() != "y":
        print("Thank you for playing!")
        break
