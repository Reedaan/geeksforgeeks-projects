import random

game_end = False


def roll_number():
    rolled_number = random.randint(1000, 9999)
    return rolled_number

rolled_number = roll_number()
rolled_number_hidden = ["_" for x in range(len(str(rolled_number)))]
rolled_number_str = str(rolled_number)
number_of_tries = 0
username = input("Welcome to the mastermind game! What's your name?: ")

while game_end == False:
    if "_" in rolled_number_hidden:
        guessed_number = 0
        print(rolled_number_hidden)
        player_guess = input("Guess a 4 digit number: ")
        if len(player_guess) != 4:
            print("Please provide a 4 digit number!")
        else:
            number_of_tries += 1
            for i in range(4):
                if player_guess[i] == rolled_number_str[i]:
                    rolled_number_hidden[i] = player_guess[i]
                    guessed_number += 1
            if guessed_number != 4:
                print(f"Not quite the number,but you got {guessed_number} numbers correct!")  
    else:
        print(f"Congratulations! It took you {number_of_tries} tries.")
        game_end = True
    
               
           
                
