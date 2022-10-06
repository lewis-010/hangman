import random

class Hangman():
    def __init__(self, word_list=["banana", "grape", "watermelon", "apple", "plum"], num_lives=5):
        self.word = random.choice(word_list).lower()
        self.word_guessed = len(self.word)*["_"]
        self.num_letters = len(set(self.word))
        self.num_lives = int(num_lives)
        self.word_list = word_list
        self.list_of_guesses = []

    def check_guess(self, guess):
        guess = guess.lower()
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
            self.list_of_guesses.append(guess) 
    
    def ask_for_input(self):
        while True:
            guess = input("Guess a letter: ")
            if len(guess)>1 or not guess.isalpha():
                print("Invald letter. Please enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter.")
            else:
                self.check_guess(guess)
                break
    
Hangman().ask_for_input()