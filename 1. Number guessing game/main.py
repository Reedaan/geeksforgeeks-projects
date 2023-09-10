import random

range = int(input("What's the maximum range for numbers?: "))
number_to_guess = random.randint(1, range)

users_guess = False
number_of_guesses = 0

while users_guess == False:
    number_of_guesses += 1
    print(number_to_guess)
    user_number = int(input("Guess the number: "))
    if user_number == number_to_guess:
        users_guess == True
        break
    elif user_number < number_to_guess:
        print("The random number is higher than your guess!")
    elif user_number > number_to_guess:
        print("The random number is lower than your guess!")
print(f"You won! Total number of guesses: {number_of_guesses}")


