# Imports
import string
import random

# Password Generator
def chooseNumber():
    try:
        passNum = int(input("How many passwords?: "))
        if passNum > 100:
            print("--Too many passwords. (> 100)")
            chooseNumber()
        elif passNum <= 0:
            print("--No passwords generated. (< 0)")
            chooseNumber()
        else:
            try:
                passlength = int(input("Choose your password length: "))
                if passlength > 100:
                    print("--Password is too long. (> 100)")
                    chooseNumber()
                elif passlength <= 0:
                    print("--Password is too short. (< 0)")
                    chooseNumber()
                else:
                    password = "" 
                    i = 0
                    while i < passNum:
                        password = password.join((random.choices(string.ascii_letters + string.digits + string.punctuation, k=passlength)))
                        i = i + 1
                        print(password)
                        password = ""
            
            except ValueError:
                print("--Please enter a number.")
                chooseNumber()
    except ValueError:
        print("--Please enter a number.")
        chooseNumber()

chooseNumber()