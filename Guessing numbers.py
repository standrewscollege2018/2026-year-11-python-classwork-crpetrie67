Number = 3

ask_guess = True

while ask_guess == True:
    # Get the guess and check if it is correct
    # If correct, set ask_guess to False
    guess = int(input("Guess a number from 1 to 10"))
    if guess == NUMBER:
        ask_guess = False
    else:
        print("Incorrect")
        
print("Well done")