import random

number = random.randrange(0, 100)

def guessGame():

    guess = int(input("Input your guess: "))
    while True:
        if guess == number:
            print('--Correct!')
            break
        elif guess < number:
            print('--Higher!')
            guessGame()
            break
        elif guess > number:
            print('--Lower!')
            guessGame()
            break
        
guessGame()