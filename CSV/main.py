# Imports
import csv
import json
import os

# Delete Fils
thisfolder = os.listdir("/Users/Landon.Warren/Desktop/Python Assignments/CSV")
for item in thisfolder:
    if item.endswith(".csv"):
        os.remove(item)
    elif item.endswith(".json"):
        os.remove(item)
 
# CSV

fName = input("First Name: ")
lName = input("Last Name: ")
age = input("Age: ")

data = []
data = [
    [f'{fName}', f'{lName}', f'{age}']
]

csvFilePath = f'{fName}.csv'
jsonFilePath = f'{fName}.json'

# Open the file in write mode
with open(csvFilePath, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)
 
with open(jsonFilePath, "w") as f:
    f.write(json.dumps(data, sort_keys=False, indent=4, separators=(',', ': '))) #for pretty

# Print a confirmation message
print(f"CSV file '{csvFilePath}' created successfully.")