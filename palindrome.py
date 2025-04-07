#For this assignment use the words.txt file.
#Read in all the words. Count how many are palindromes, or words that are spelled the same forwads and backwards.
#For example, wow is a paldindrome.
#A different file wile be used for grading.
#Correct answer for this file: 

OutFile = open("words.txt")

rev =- 1
Total = 0

with open('words.txt','r') as OutFile:
    ReadFile = OutFile.readlines()
    for FileCount in OutFile:
        Count = len(FileCount)
        if str[FileCount] == str[rev]:
            Total += 1
            rev =- 1

print (f"There are {Total} Palidromes")