while True:
    guess = input("Guess a letter ")
    if guess.isalpha() and len(guess)==1:
        print("Good guess!")
        break
    else:
        print("Invalid letter, please enter a single alphabetical character")