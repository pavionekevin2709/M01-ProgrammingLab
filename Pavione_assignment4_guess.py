# Import random to pick a number
import random

# Pick a random number between 1 and 100
secret_number = random.randint(1, 100)

# Set up variables
attempts = 0
max_attempts = 5
guesses = []  # List to store guesses

# Welcome message
print("Guess the number between 1 and 100! You have 5 tries.")

# Guessing loop
while attempts < max_attempts:
    # Get player's guess
    guess = input("Your guess: ")
    guess = int(guess)  # Turn input into a number
    attempts += 1  # Count the attempt
    guesses.append(guess)  # Save the guess

    # Check if guess is correct
    if guess == secret_number:
        print(f"You win! The number was {secret_number} in {attempts} tries!")
        break
    elif guess < secret_number:
        print("Too low!")
    else:
        print("Too high!")

# If out of tries, show the number
if attempts == max_attempts and guess != secret_number:
    print(f"Game over! The number was {secret_number}.")

# Show all guesses
print("Your guesses were:", guesses)