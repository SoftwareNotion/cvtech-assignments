# Imports
import random
import pyperclip

# Variables
lineDecor = "━━━━━━━━━━━━"
jpHiraChar = ["あ", "い", "う", "え", "お", "か", "き", "く", "け", "こ", "さ", "し", "す", "せ", "そ", "た", "ち", "つ"]
engHiraChar = ["a", "i", "u", "e", "o", "ka", "ki", "ku", "ke", "ko", "sa", "shi", "su", "se", "so", "ta", "chi", "tsu"]
hiraCharNum = 0
prompt = []
promptTrans = []
promptStr = ""
promptStrTrans = ""
promptNum = random.randrange(3, 13)


# Translate Text
def translate():
    transText = input("Translate Text:")
    if transText == promptStrTrans:
        print("--Correct!--")

    elif transText == "dev":
        print(f"[Copied to Clipboard: {promptStrTrans}]")
        pyperclip.copy(promptStrTrans)
        translate()

    else:
        print("--Incorrect.--")
        translate()   


# Print Characters
print(lineDecor)
for i in range(promptNum):
    hiraCharNum = random.randrange(0, len(jpHiraChar))
    prompt.append(jpHiraChar[hiraCharNum])
    promptTrans.append(engHiraChar[hiraCharNum])
    

for i in prompt:
    promptStr += i

for i in promptTrans:
    promptStrTrans += i

    

print(promptStr)
print(lineDecor)
translate()