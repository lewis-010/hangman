import random

# create Hangman class
class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word = random.choice(word_list).lower()
        self.word_guessed = len(self.word)*["_"]
        self.num_letters = int(set(self.word))
        self.num_lives = int(num_lives)
        self.word_list = word_list
        self.list_of_guesses = []