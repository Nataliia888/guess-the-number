import random
number = random.randint(1,5)
isGuessRight = False
while isGuessRight != True:
 guess = input("Guess a number between 1 and 5: ")
 if int(guess) == number:
   print("You guessed {}. That is right! You win!".format(guess))
   isGuessRight = True
   break
 else:
   print("You guessed {}. Sorry, that isn’t it. Try again.".format(guess))
