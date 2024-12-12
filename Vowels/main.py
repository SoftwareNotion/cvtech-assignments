import os

os.system('cls')
userString = input("Enter a string: ")
vowels = ['a', 'u', 'i', 'e', 'o']
vowelCount = 0
aCount = 0
uCount = 0
iCount = 0
eCount = 0
oCount = 0

for letter in userString:
    if letter.lower() in vowels:
        vowelCount = vowelCount + 1
        if letter.lower() == vowels[0]:
            aCount = aCount + 1
        elif letter.lower() == vowels[1]:    
            uCount = uCount + 1
        elif letter.lower() == vowels[2]:
            iCount = iCount + 1
        elif letter.lower() == vowels[3]:
            eCount = eCount + 1
        elif letter.lower() == vowels[4]:
            oCount = oCount + 1

print(f"Vowels Found: {vowelCount}")
print(f"A: {aCount}, U: {uCount}, I: {iCount}, E: {eCount}, O: {oCount}.")