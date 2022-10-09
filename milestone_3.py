import random

class Hangman():
    def __init__(self, word_list, num_lives=5):
        ''' Parameters:
            ----------
            word_list: list
                List of words to be guessed
            num_lives: int
                Number of lives the player has
            
            Attributes:
            ----------
            word: str
                The word to be guessed (picked randomly from word_list)
            word_guessed: list
                List of the letters of each word, with unguessed letters represented with '_'
            num_letters: int
                The number of unique letters in the word the word that have not been guessed
            list_of_guesses: list
                List of the letters that have already been attempted 
            print_msg: list
                List of print statements to be randomly shown if a guess is correct
            '''
        self.word = random.choice(word_list).lower()
        self.word_guessed = len(self.word)*["_"]
        self.num_letters = len(set(self.word))
        self.num_lives = int(num_lives)
        self.word_list = word_list
        self.list_of_guesses = []
        self.print_msg = ["Nice one!", "Good guess!", "Getting there!", "That's correct!", "Well played!", "Yep, that's a letter!"]

    def check_guess(self, guess):
        ''' 
        Checks if the player's guess is in the word.
        If correct: 
            - random string from print_msg list is shown 
            - '_' in word_guessed list is replaced with correct letter
            - value of num_letters decreases by 1
        If incorrect:
            - value of num_lives decreases by 1
            - number of lives remaining printed to player
        Letter guessed is appended to list_of_guesses.        
        '''
        guess = guess.lower()
        if guess in self.word:
            print(f"{random.choice(self.print_msg)} {guess} is in the word.")
            for i,letter in enumerate(self.word):
                if guess == letter:
                    self.word_guessed[i] = guess
            self.num_letters-=1
            print(self.word_guessed)
        else:
            self.num_lives-=1
            print(f"Sorry, {guess} is not in the word")
            if self.num_lives > 2 and self.num_lives!=1:
                print(f"You have {self.num_lives} lives left.")
            elif self.num_lives==2:
                print("Uh oh, only two lives left!")
            else:
                print("Only 1 life left, make it count!")
        self.list_of_guesses.append(guess)

    def ask_for_input(self):
        ''' 
        Request input from user and checks validity of the guess.
        If valid (single alphabetical character):
            - runs check_guess method
        If invalid:
            - prints request for a valid input or prints guess already in list_of_guesses        
        '''
        while True:
            guess = input("Guess a letter: ")
            if len(guess)>1 or not guess.isalpha():
                print("Invald letter. Please enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You have already tried that letter.")
            else:
                self.check_guess(guess)
                break

def play_game():
    word_list = ["banana", "grape", "watermelon", "apple", "plum", "cherry", "lemon", "orange", "mango", "papaya"]
    num_lives = input("Welcome to hangman. How many lives would you like? ")
    print("Good luck! HINT: the word is a type of fruit.")
    game = Hangman(word_list, num_lives)
    while True:
            if game.num_lives==0:
                print("Sorry, game over.")
                break
            elif game.num_letters == 1:
                print("Only one letter left!")
                game.ask_for_input()
            elif game.num_letters > 0:
                game.ask_for_input()
            elif game.num_lives !=0 and game.num_letters==0:
                print("Congratulations, you have won!")
                break

if __name__=="__main__":
    play_game()