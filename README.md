># The Hangman Project
Hangman is a simple guessing game. One player will think of a word and another will attempt to find out the hidden word by guessing a single letter of the alphabet at a time. If the letter guessed is in the word, then that letter is revealed and the guessing continues until all the blanks or revealed. If the this is not completed within a specified number of attempts, the person guessing loses the game. 

>## Milestone 1
- List of 5 items created and random.choice() used to choose a word from the list to be guessed.
- *"__ name__ == __ main __"* used to ensure certain code isn't executed when milestone_1.py is imported.

![](milestone_1_code.png)
>## Milestone 2

- Two functions created for checking the validity of the user's guess and for checking if the guess is in the hidden word.
    - *check_guess()* checks if the guess is in the hidden word and returns relevant outputs.
    - *ask_for_input()* requests the user guess a letter and checks the validity of the guess, if the input is not valid this code will loop until an accepted guess is made.

![](milestone_2_code.png)
>## Milestone 3
- *Hangman* class created with the following attributes defined:
    - *word* = the word to be guessed from the *word_list*.
    - *word_guessed* = a list of the letters of the *word* with '' for each letter not guessed.
    - *num_letters* = the number of unique letters in the *word* that have not been guessed.
    - *num_lives* = the number of lives the player has at the start of the game.
    - *list_of_guesses* = a list of the guesses that have already been made.
<br/><br/>
- Two methods created to check the validity of the users guess and if the guess is correct or not.
    - check_guess = checks if the guess is in the *word*.
    - ask_for_input = requests the user make a guess and checks the validity of the guess.

![](milestone_3_code.png)
>## Putting the game together
- The final task was to put the code together through a *play_game()* function
- Inside the *play_game()* function an instance of the *Hangman* class was created (*game*). 
- Outputs for the values of *num_lives* and *num_letters* were suitably set.
    - E.g., *game.num_lives != 0 and game.num_letters==0* are the conditions for outputting the congratulations message.
- A 7th attribute was also added to the *Hangman* class.
    - *self.print_msg* is a list of strings that are randomly selected with *random.choice* when the user guesses correctly.
    - This should add a bit of variety to the game.