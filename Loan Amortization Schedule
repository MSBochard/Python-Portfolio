"""
Algorithm:     Sets up a loan amortization schedule based off the user's
               inputted inital balance, interest rate, and loan period.
"""

#Ask user for loan information and assign to variables
balance = int(input("Loan Amount: "))
yearPeriod = int(input("Number of Years: "))
interest = (int(input("Annual Interest Rate: ")) / 100)

#Math for the total monthly payment 
monthPeriod = yearPeriod * 12
monthlyInterest = interest / 12
monthlyPayment = balance * ((monthlyInterest * (1 + monthlyInterest) ** monthPeriod) /
                           ((1 + monthlyInterest) ** monthPeriod - 1))

#monthlyPayment = (balance / monthPeriod) + (monthlyInterest * balance)
totalPayment = monthlyPayment * monthPeriod

#Print the monthly and total payments for the loan
print("Monthly Payment: $" + format(monthlyPayment, ".2f"))
print("Total Payment: $" + format(totalPayment, ".2f"))

#Create the amoritization schedule using a loop
print("Payment #\t Interest\t Principal\t Balance")
for i in range(1, monthPeriod + 1):
    interest = monthlyInterest * balance
    principal = monthlyPayment - interest
    balance = balance - principal
    print(i, "\t\t", format(interest, ".2f"), "    \t", format(principal, ".2f"),
          "    \t", format(balance, ".2f"))

