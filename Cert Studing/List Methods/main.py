# Imports
import os

# Start
pylist = ["Landon", "Spencer", "Gabriel", "Kale", "Cameron", "Gavin", "Sierra", "Connor", "Connor"]
result = ""
extend = ["1", "1", "1", "2", "3"]
def print_list():
    os.system('cls')
    print(f"Result: {result}")
    print(pylist)
    print("append | clear | copy | count | extend | index | insert | pop | remove | reverse | sort")
print_list()

# Methods
def method_input():
    while True:
        method = input()
        global result
        if method.startswith("append "):
            new_method = method.replace("append ", "")
            pylist.append(new_method)
            result = f"Added \"{new_method}\"."
        elif method.startswith("clear"):
            pylist.clear()
            result = "Cleared the list."
        elif method.startswith("copy"):
            result = pylist.copy()
        elif method.startswith("count "):
            new_method = method.replace("count ", "")
            result = pylist.count(new_method)
        elif method.startswith("extend"):
            pylist.extend(extend)
            result = f"Extended the list with all items from {extend}."
        elif method.startswith("index "):
            new_method = method.replace("index ", "")
            result = pylist.index(new_method)
        elif method.startswith("pop "):
            new_method = method.replace("pop ", "")
            result = f"Removed \"{pylist[int(new_method)]}\"."
            pylist.pop(int(new_method))
        elif method.startswith("remove "):
            new_method = method.replace("remove ", "")
            pylist.remove(new_method)
            result = f"Removed \"{new_method}\"."
        elif method.startswith("reverse"):
            pylist.reverse()
            result = f"Reversed the order of the list."
        elif method.startswith("sort"):
            pylist.sort()
            result = f"Sorted the list alphabeticaly."
        print_list()
    
method_input()