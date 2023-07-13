'''
Algorithm:  Converts numeric grade values into their letter grade equivalents.
'''
#Asks the user to input a numeric grade value
scorestr = input("Enter a score between 0.0 and 100.0: ")

#Validates the input variable's value
try:
    score = float(scorestr)
except:
    print("Invalid Score")
    quit()

#Converts the numeric grade into the equivalent letter grade format
if score > 100.0 or score < 0.0:
    print("Score is out of range")
elif score >= 90.0:
    print("A")
elif score >= 80.0:
    print("B")
elif score >= 70.0:
    print("C")
elif score >= 60.0:
    print("D")
else:
    print("F")
