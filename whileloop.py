#------------------------------------
# While loop
#------------------------------------

i=1
while i<5:
    print(i)
    i+=1

print("Done with while loop")

#------------------------------------
#Building guessing game
#------------------------------------

secretWord = "Python"
guess = ""
guessCount = 0
guessLimit = 3
outOfGuesses = False

while guess != secretWord and not(outOfGuesses):
    if guessCount < guessLimit:
        guess = input("Enter your guess : ")
    else:
        outOfGuesses = True
    guessCount += 1

if outOfGuesses:
    print("You're out of guesses")
else:
    print("You win!")