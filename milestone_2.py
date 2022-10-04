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