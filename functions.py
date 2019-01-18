import os
import time
import datetime

users = ["Aydon", "", ""]
command_list = ["$viewfiles\n", "$newfile\n", "$web\n", "$restart", "$editfile",  "$deletefile", "$shutdown\n"]
files = ["functions.py", "startfile.py"]
def load(t):
    for x in range(t):
        print("...")
        time.sleep(0.5)
        os.system("CLS")
        print(" ..")
        time.sleep(0.5)
        os.system("CLS")
        print("  .")
        time.sleep(0.5)
        os.system("CLS")


def comp():
    os.system("CLS")
    print("User: Aydon Joseph")
    command = input("PiConsole: ")
    if command == "$help":
        for x in command_list:
            print(x)
        
        time.sleep(10)
        os.system("CLS")
        comp()
    elif command == "$viewfiles":
        for x in files:
            print(x)

        time.sleep(5)
        comp()
        
    elif command == "$web":
        os.system("cd C:\Program Files (x86)\Google\Chrome\Application")
        os.system("start chrome.exe")
        os.system("CLS")
        comp()
    elif command == "$shutdown":
        os.system("exit")
    elif command == "$newfile":
        os.system("CLS")
        name = input("What would you like to name the file?")
        os.system("type nul >" + name)
        files.append(name)
        comp()
    elif command == "$restart":
        os.system("exit")
        os.system("start PiConsole64.py")
    elif command == "$editfile":
        os.system("CLS")
        file = input("Filename: ")
        os.system("CLS")
        print("To save and exit press CTRL + Z")
        os.system("copy con " + file)
        os.system("start functions.py")
        comp()
    elif command == "$deletefile":
        os.system("CLS")
        filename = input("Filename: ")
        os.system("del " + filename)
        os.system("CLS")
        comp()
        
def username():
    print("Loading PiConsole")
    load(2)
    username = input("Enter Username: \n")
    comp()

