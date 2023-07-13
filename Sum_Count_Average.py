'''
Algorithm:  Has the user input a series of numbers until the user enters "done"
            then takes those numbers and prints out the sum of the number,
            the amount of numbers entered, and the average of then numbers.
'''
#Set initial values for the sum and count variables
numSum = 0
numCnt = 0

#Infinite while loop to continue to ask for a number until the user
#inputs a value that causes the program to exit the loop
while True:
    inputNum = input("Enter a number: ")

    try:
        if inputNum == "done":
            break
        else:
            num = float(inputNum)
    except:
        print("Invalid input")
        continue

    numSum = numSum + num
    numCnt = numCnt + 1

#Prints out the sum of the numbers, the amount of numbers, and the average
print("Sum is", numSum)
print("Count is", numCnt)
print("Average is", numSum / numCnt)
