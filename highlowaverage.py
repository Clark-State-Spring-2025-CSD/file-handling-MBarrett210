#For this assignment use the numbers.txt file.
#A different numbers.txt will be used for grading.
#Read in all the numbers. Display the following information:
#How many numbers in the file
#Total of all the number
#Average
#Highest number
#Lowest number
#Correct answers for the included file:

OutFile = open("numbers.txt")

Sum = 0
Count = 0


for FullLine in OutFile:
    CoreLine = int(FullLine)
    Count += 1
    highnum = max(Count)
    lownum = min(FullLine)
    Sum += CoreLine
    Total = len(FullLine)

OutFile.close()

avg = Sum / Count

print (f"Total Number is: {Total}")
print (f"Average is {avg}")
print (f"Highest NUmbner is: {highnum}")
print (f"Lowest Number is {lownum}")