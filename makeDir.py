# Author: Mason Akershoek
# App Name: Make Dir Utility

import os

def main():
    print("Welcome to the Make Dir Utility.")
    print("By. Mason Akershoek\n")
    cwd = getDir()
    showName = getShow()
    diskNum = getDisks()
    ch = input("Would you like to see the directory structure first?(y or n) ")

    if ch == "y":
        showDir(cwd, showName, diskNum)
    
    makeDirs(cwd, showName, diskNum) 

    print("Operation complete!")
    

def getDir():
    cwd = input("Enter the directory where you want this dir: ")
    return cwd

def getShow():
    showName = input("Enter the name of the show: ")
    return showName

def getDisks():
    diskNum = input("Enter number of disks in case: ")
    diskNum = int(diskNum)
    return diskNum

def makeDirs(cwd, showName, diskNum):
    path = os.path.join(cwd, showName)
    os.mkdir(path)
    for x in range (0, diskNum, 1):
        index = x+1
        path = os.path.join(cwd, showName, "D"+str(index))
        os.mkdir(path)

def showDir(cwd, showName, diskNum):
    print("\n\nCurrent Working Directory: ", cwd, "\n")
    print(showName)
    for x in range (0, diskNum, 1):
        index = x+1
        print("|--" + "D" + str(index))
    ch = input("\nWould you like to continue with the operation (y or n):  ")
    if ch == "n":
        quit()
        

if __name__=="__main__":
    main()