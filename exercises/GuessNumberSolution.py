import random

# Generate a random number to be guessed
number = random.randint(1, 100)
print("Guess a magic number between 0 and 100")
guess = -1
while guess != number:
    guess = int(input("Enter your guess: "))
    if guess == number:
        print("Yes, the number is", number)
    elif guess > number:
        print("Your guess is too high")
    else:
        print("Your guess is too low")