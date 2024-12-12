# Imports
import qrcode
import os

# Variables
thisfolder = os.listdir("/Users/Landon.Warren/Desktop/Python Assignments/QR Code")
newqrsource = ""

# Generate QRCode
def generateQR():
    qrsource = input("Type QRCode content: ")
    if qrsource == "":
        print("Please input something.")
        generateQR()
    elif qrsource == "dev del":
        for item in thisfolder:
            if item.endswith(".png"):
                os.remove(item)
        generateQR()

    else:
        qr = qrcode.make(qrsource)
        type(qr)
        newqrsource = qrsource.replace('/', "").replace('\\', "").replace(':', "")
        qr.save(f"{newqrsource}.png")
        print("Generated QRCode.")
        generateQR()

generateQR()