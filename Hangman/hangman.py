import random
import os

fruits = ["Apple", "Banana", "Cherry", "Orange", "Pear", "Kiwi"]
fruit = random.choices(fruits)
fruit = str(fruit).replace('[', '').replace(']', '').replace('\'', '')
fruitSecret = ""
fruitLength = len(fruit)
fruitLetters = []
registeredLetters = []
chances = fruitLength + 2
count = 0

for item in fruit:
    count += 1
    fruitLetters.append(fruit[count - 1].lower())
    fruitSecret = fruitSecret + "_"

print(fruitSecret)
print(f"Your word has \"{fruitLength}\" letters.")

def guessWord():
    global chances
    global fruitSecret
    if fruitSecret.capitalize() == fruit: 
            os.system('cls')
            print(" __  __              _      ___      __")
            print(" \\ \\/ /__  __ __    | | /| / (_)__  / /")
            print("  \\  / _ \\/ // /    | |/ |/ / / _ \\/_/ ")
            print("  /_/\\___/\\_,_/     |__/|__/_/_//_(_)  ")
            print("")
            print(f'You got it right!: "{fruit}"')
    else:
        answer = input("Guess a letter: ")

        if chances > 1:
            if answer.lower() not in fruitLetters:
                os.system('cls')
                chances = chances - 1
                print(fruitSecret)
                print('NO! YOU\'RE BAD AT THIS!')
                print(f'You have "{chances} chances left."')
                guessWord()
            else:
                if answer.lower() not in registeredLetters:
                    os.system('cls')
                    for i, letter in enumerate(fruitLetters):
                        if answer == letter:
                            fruitSecretList = list(fruitSecret)
                            fruitSecretList[i] = letter
                            newFruitSecret = "".join(fruitSecretList)
                            fruitSecret = newFruitSecret

                    print(fruitSecret)
                    print('You got a letter!')
                    registeredLetters.append(answer)
                    guessWord()

                else:
                    os.system('cls')
                    print(fruitSecret)
                    print(f'You already got "{answer}"!')
                    guessWord()
        else:
            os.system('cls')
            print(" __  __              __                __")
            print(" \\ \\/ /__  __ __    / /  ___  ___ ___ / /")
            print("  \\  / _ \\/ // /   / /__/ _ \\(_-</ -_)_/ ")
            print("  /_/\\___/\\_,_/   /____/\\___/___/\\__(_)  ")
            print("")
            print(f'Your word was: "{fruit}"')

guessWord()