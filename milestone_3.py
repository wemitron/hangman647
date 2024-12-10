#import modules
import random

word_list = ["mango", "kiwi", "banana", "peach", "cherry"]

#generate random word from list
word = random.choice(word_list)
print(word)

def ask_for_input():
    """Asks user to enter a guess and validates input is a single letter
    
    Returns:
    guess (str) : user's guess of letter in word

    """
    while True:
        guess = input("Guess a letter")
        if guess.isalpha() == True and len(guess) == 1:
            return guess
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")

def check_guess(guess):
    """Checks if user's guess is in the word and prints whether they are correct or not.
    
    Parameters: 
    guess (str) : user's guess of letter in word
    
    """
    guess = guess.lower()
    #check if guess is in word
    if guess in word:
        print(f"Good guess! {guess} is in the word. ")
    else:
        print(f"Sorry, {guess} is not in the word. Try again.")

guess = ask_for_input()
check_guess(guess)