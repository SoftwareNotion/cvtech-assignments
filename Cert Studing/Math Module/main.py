# Imports
import math
import os

# Variables
result = ""
info = ""

# Functions
def print_info():
    os.system("cls")
    print(f"Result: {result}")
    print(f"Information: {info}")
    print("sqrt # | ceil # | floor # | fabs # | pow # # | log # | sin # | cos # | tan # | pi | e | tau | inf | nan | exit")

def continuous_input():
    global result
    global info
    while True:
        user_input = input("")
        input_data1 = user_input.split(' ')[1]
        try:
            input_data2 = user_input.split(' ')[2]
        except:
            pass
        if user_input.startswith("sqrt"):
            result = math.sqrt(float(input_data1))
            info = f"Found the square root of {input_data1}."
            print_info()
        elif user_input.startswith("ceil"):
            result = math.ceil(float(input_data1))
            info = f"Rounded {input_data1} up."
            print_info()
        elif user_input.startswith("floor"):
            result = math.floor(float(input_data1))
            info = f"Rounded {input_data1} down."
            print_info()
        elif user_input.startswith("fabs"):
            result = math.fabs(float(input_data1))
            info = f"Found the absolute value of {input_data1}."
            print_info()
        elif user_input.startswith("pow"):
            result = math.pow(float(input_data1), float(input_data2))
            info = f"Found {input_data1} to the power of {input_data2}."
            print_info()
        elif user_input.startswith("log"):
            result = math.log(float(input_data1))
            info = f"Found the natural logarithm of {input_data1}"
            print_info()
        elif user_input.startswith("sin"):
            result = math.sin(float(input_data1))
            info = f"Found the sine of {input_data1}"
            print_info()
        elif user_input.startswith("cos"):
            result = math.cos(float(input_data1))
            info = f"Found the cosine of {input_data1}"
            print_info()
        elif user_input.startswith("tan"):
            result = math.tan(float(input_data1))
            info = f"Found the tangent of {input_data1}"
            print_info()

print_info()
continuous_input()