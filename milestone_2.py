#%%

#import modules
import random

word_list = ["mango", "kiwi", "banana", "peach", "cherry"]

#generate random word from list
word = random.choice(word_list)

guess = input("Please enter a single letter")
# %%

if len(guess) == 1:
    print("Good guess!")
else:
    print("Oopsie! That's not a valid input.")