'''
Algorithm:  Takes the user's inputted numeric values and prints out
            the largest and smallest numbers.
'''
#sets the initial value of the largest and smallest numbers
largest = None
smallest = None

#Infinite while loop that continually asks the user for numeric values
while True:
    inputNum = input("Enter a number: ")

    #Validates that the user is inputting numeric values
    try:
        if inputNum == "done":
            break
        else:
            num = int(inputNum)
    except:
        print("Invalid input")
        continue

    #Goes through the inputted numeric values and assigns them to the
    #largest and smallest variables
    if largest is None or smallest is None:
        largest = num
        smallest = num
    elif largest < num:
        largest = num
    elif smallest > num:
        smallest = num

#Prints out the largest and smallest numbers
print("Maximum is", largest)
print("Minimum is", smallest)
