# iteratively checks user input validity
while True:
    guess = input("Guess a letter ")
    if guess.isalpha() and len(guess)==1:
        print("Good guess!")
        break
    else:
        print("Invalid letter, please enter a single alphabetical character")

word = "apple"
while True:
    guess = str(input("Guess a letter "))
    if guess in word:
        print(f"Good guess! {guess} is in the word.")
        break
    else:
        print(f"Sorry, {guess} is not in the word. Try again.")  