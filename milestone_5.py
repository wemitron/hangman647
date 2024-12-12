#import modules
import random

class hangman:

    def __init__(self, word_list, num_lives):
        """ Initialise the attributes of the hangman class.
        
        Parameters: 

        word_list (lst) : list of words the computer can choose from.
        word (str) : randomly selected word from  word_list.
        word_guessed (lst) : placeholder list of the word to be guessed.
        num_letters (int) : number of unique letters in the word.
        list_of_guesses (lst) : list containing the player's guesses.
        num_lives (int) : the player's number of lives.

        
        """

        self.word_list =  word_list
        self.word = random.choice(word_list)
        self.word_guessed = ["_"]*len(self.word)
        self.num_letters = len(set(self.word)) 
        self.list_of_guesses = []
        self.num_lives = num_lives
    
    def check_guess(self,guess):
        """Checks if player's guess is in the word and prints whether they are correct or not.
        
        Parameters: 

        guess (str) : player's guess of a letter in the word.
        
        """
        guess = guess.lower()
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
        """Asks player to enter a guess and validates input is a single letter.

        Returns:

        guess (str) : player's guess of a letter in the word.
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
                break
    
def play_game(word_list):
    num_lives = 5
    game = hangman(word_list,num_lives)
    print(f"The word to guess is {game.word_guessed}")
    while True:

        if game.num_lives == 0:
            print( 'You lost!')
            break
        elif game.num_letters == 0 :
            print("Congratulations. You won!")
            break
        else:
            game.ask_for_input()
            
        
word_list = ["mango", "kiwi", "banana", "peach", "cherry"]  
play_game(word_list)