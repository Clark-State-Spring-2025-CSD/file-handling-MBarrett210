#Read in the echo.txt file and display it in the terminal using print()
#This is a guided practice. Either follow the video or your instructor in class.

OutFile = open("echo.txt")

with open('echo.txt', 'r') as OutFile:
    ReadFile = OutFile.readlines()
    print(ReadFile)