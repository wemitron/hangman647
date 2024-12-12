#import modules
import random

class hangman:
    def __init__(self, word_list, num_lives=5):

        self.word_list =  word_list
        self.word = random.choice(word_list)
        self.word_guessed = ["_"]*len(self.word)
        print(self.word)
        #print(self.word_guessed)
        self.num_letters = len(set(self.word)) #sotres number of unique letters in word
        self.list_of_guesses = []
        self.num_lives = num_lives
    
    def check_guess(self,guess):
        """Checks if user's guess is in the word and prints whether they are correct or not.
        
        Parameters: 
        guess (str) : user's guess of letter in word
        
        """
        guess = guess.lower()
        #check if guess is in word
        if guess in self.word:
            print(f"Good guess! {guess} is in the word. ")
            letter = 0
            for letter in range(len(self.word)):
                if guess == self.word[letter]:
                    self.word_guessed[letter] = guess
                    print(self.word_guessed)
            self.num_letters -= 1
        else:
            print(f"Sorry, {guess} is not in the word. Try again.")
            self.num_lives -= 1
            print(f"You have {self.num_lives} lives left.")

    def ask_for_input(self):
        """Asks user to enter a guess and validates input is a single letter
        Returns:
        guess (str) : user's guess of letter in word
        """
        while True:
            guess = input("\nGuess a letter: ")         
            if guess.isalpha() == False or len(guess) != 1:
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
                print(f"List of guesses:{self.list_of_guesses}")

        

hangman_game = hangman(["mango", "kiwi", "banana", "peach", "cherry"])
hangman_game.ask_for_input()
