import random 
secret_number = random.randint(1,20)

print("Welcome to the Number Guessing Game!")
for guesses_taken in range(1, 7):
    guess = int(input("Take a guess (between 1 and 20): "))

    if guess < secret_number:
        print("Your guess is too low.")
    elif guess > secret_number:
        print("Your guess is too high.")
    else:
        break  # This condition is the correct guess!
    if guess == secret_number:
        print(f"Good job! You guessed my number in {guesses_taken} guesses!")