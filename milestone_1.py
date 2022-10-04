# import libraries
import random

# create list for 5 favourite fruits
word_list = ["banana", "grape", "watermelon", "apple", "plum"]

# pass list through random module
word = random.choice(word_list)
# print(word)

# get input from user (guess the fruit)
guess = input("Guess a letter: ")
if guess.isalpha() and len(guess)==1:
    print("Good guess!")
else:
    print("Oops! That is not a valid input.")