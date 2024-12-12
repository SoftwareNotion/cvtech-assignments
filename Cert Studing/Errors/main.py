# Imports
import os

# Main
os.system('cls')

try:
    user_input = int(input("Input a integer that is not 0: "))
    if user_input == 0:
        raise Exception("[Raise Error] You can't input 0.")
except ValueError:
    print("[Except Error] You must input a Integer.")
finally:
    print("Exited Program.")