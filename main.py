## Ques : We are going to write a program that generates a random number and asks the user to guess it.
## If the player guess is highter than the actual number, the program displays "Lower number please". Similarly if the user's guess is too low, the program prints "highter number please".
## When the user guesses the correct number, the program displays the number of fuesses the player used to arrive at the number.

## Hint : use the random module
import random
randNumber = random.randint(1, 100)
userGuess = None
guesses = 0

while(userGuess != randNumber):
    userGuess = int(input("Enter your guess : "))
    guesses += 1
    if(userGuess==randNumber):
        print("You guessed it right!")
    else:
        if(userGuess>randNumber):
            print("You guessed it wrong! Enter a smaller number")
        else:
            print("You guessed it wrong! Enter a larger number")
        

print(f"You guesses the number in {guesses} guesses")
with open("hiscore.txt", "r") as f:
    hiscore = int(f.read())

if(guesses<hiscore):
    print("You have just broken the high score!")
    with open("hiscore.txt", "w") as f:
        f.write(str(guesses))