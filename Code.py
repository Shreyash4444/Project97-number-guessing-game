import random

print("Number Guessing Game")

number = random.randint(1, 9)

chances = 0

print("Guess a number between 1 to 9")
guess = int(input("enter your guess:- "))

while chances < 5:

    if guess == number:

        print("Congratulations YOU WON!!!")
        break

    else guess < number:
        print < number("Your number was too low:Guess a number higher than", guess)

    else:
        print(Your guess was too high:guess a numer lower than",guess)

    chances += 1

if not chances < 5:
    print ("YOU LOSE!!!The number is",number)