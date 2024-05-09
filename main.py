import random
from art import logo

#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).


def main():
    target = random.randint(1,100)
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number betwween 1 and 100.")
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if difficulty == 'easy':
        lives = 10
    else:
        lives = 5
    
    
    playing = True
    while playing:
        if lives == 0:
            playing = False
            print(f"You ran out of guesses. The number was {target} You lose!")
        else:
            print("Guess again.")
            print(f"You have {lives} attempts remaining to the guess the number.")
            guess = int(input("Make a guess: "))

            if guess < target:
                print("Too low.")
                lives -= 1
            elif guess > target:
                print("Too high.")
                lives -= 1
            elif guess == target:
                print(f"YOU WON! The answer was {guess}")
                playing = False


main()
        