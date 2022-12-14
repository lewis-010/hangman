# The Hangman Project
Hangman is a simple guessing game. One player will think of a word and another will attempt to find out the hidden word by guessing a single letter of the alphabet at a time. If the letter guessed is in the word, then that letter is revealed and the guessing continues until all the blanks or revealed. If the this is not completed within a specified number of attempts, the person guessing loses the game.
- note - docstrings included in *milestone_3.py* file 
## Milestone 1
- List of 5 items created and random.choice() used to choose a word from the list to be guessed.
- *__ name__ ==" __ main __"* used to ensure certain code isn't executed when milestone_1.py is imported.
```python
import random

# create list for 5 favourite fruits
word_list = ["banana", "grape", "watermelon", "apple", "plum"]

# pass list through random module
word = random.choice(word_list)

# get input from user (guess the fruit)
if __name__=="__main__":
    guess = input("Guess a letter: ")
    if guess.isalpha() and len(guess)==1:
        print("Good guess!")
    else:
        print("Oops! That is not a valid input.")
```
## Milestone 2
- Two functions created for checking the validity of the user's guess and for checking if the guess is in the hidden word.
    - *check_guess()* checks if the guess is in the hidden word and returns relevant outputs.
    - *ask_for_input()* requests the user guess a letter and checks the validity of the guess, if the input is not valid this code will loop until an accepted guess is made.
```python
# import milestone_1 code 
import milestone_1 as ms1

# check_guess function checks if guessed letter is in the word
def check_guess (guess):
    guess = guess.lower()
    if guess in ms1.word:
        print(f"Good guess! {guess} is in the word.")
    else:
        print(f"Sorry, {guess} is not in the word. Try again.")

# ask_for_input function gets user to guess and checks the validity
def ask_for_input():
    while True:
        guess = input("Guess a letter: ")
        if guess.isalpha() and len(guess)==1:
            break
        else:
            print("Invalid input, please enter a single alphabetical character.")
    check_guess(guess)

ask_for_input()
```
## Milestone 3
- *Hangman* class created with the following attributes defined:
    - *word* = the word to be guessed from the *word_list*.
    - *word_guessed* = a list of the letters of the *word* with '' for each letter not guessed.
    - *num_letters* = the number of unique letters in the *word* that have not been guessed.
    - *num_lives* = the number of lives the player has at the start of the game.
    - *list_of_guesses* = a list of the guesses that have already been made.
- Two methods created to check the validity of the users guess and if the guess is correct or not.
    - check_guess = checks if the guess is in the *word*.
    - ask_for_input = requests the user make a guess and checks the validity of the guess.
<br/><br/>

## Putting the game together
- The final task was to put the code together through a *play_game()* function
- Inside the *play_game()* function an instance of the *Hangman* class was created (*game*). 
- Outputs for the values of *num_lives* and *num_letters* were suitably set.
    - E.g., *game.num_lives != 0 and game.num_letters==0* are the conditions for outputting the congratulations message.
- A 7th attribute was also added to the *Hangman* class.
    - *self.print_msg* is a list of strings that are randomly selected with *random.choice* when the user guesses correctly.
    - This should add a bit of variety to the game.
```python
import random

class Hangman():
     def __init__(self, word_list, num_lives=5):
        self.word = random.choice(word_list).lower()
        self.word_guessed = len(self.word)*["_"]
        self.num_letters = len(set(self.word))
        self.num_lives = int(num_lives)
        self.word_list = word_list
        self.list_of_guesses = []
        self.print_msg = ["Nice one!", "Good guess!", "Getting there!", "That's correct!", "Well played!", "Yep, that's a letter!"]

    def check_guess(self, guess):
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
```