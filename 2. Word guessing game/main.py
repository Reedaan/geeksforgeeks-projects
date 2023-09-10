import random as rand

def get_random_word(words):
    return(rand.choice(words))
    

word_list = ['rainbow', 'computer', 'science', 'programming',
         'python', 'mathematics', 'player', 'condition',
         'reverse', 'water', 'board', 'geeks']

lives = 5
number_of_guesses = 0
user_guess_list = []

username = input("Welcome to the word guessing game! What's your name?: ")
print(f"Good luck {username}!")

guess_word = [x for x in get_random_word(word_list)]
guess_word_hidden = ["_" for x in guess_word]
guess_word_string = ""

for x in guess_word:
    guess_word_string += str(x)

print(guess_word)

while "_" in guess_word_hidden:
    if lives > 0:
        print(guess_word_hidden)
        print(f"You have {lives} lives left")
        user_guess = input("Guess the letter: ").lower()
        if len(user_guess) > 1 or user_guess in user_guess_list:
            print("It appears that you put more than one letter, or you already guessed that letter!")
        else:
            if lives > 0:
                user_guess_list.append(user_guess)
                number_of_guesses += 1
                if user_guess in guess_word:
                    indices = [i for i, x in enumerate(guess_word) if x == user_guess]
                    for index, x in enumerate(indices):
                        guess_word_hidden[x] = guess_word[x]
                    
                else:
                    user_guess_list.append(user_guess)
                    lives -= 1
            else:
                break
    else:
        break

if lives > 0:
    print(f"You won! You had {lives} lives left. The word was: {guess_word_string}")
else:
    print(f"You lost! The word was {guess_word_string}")

