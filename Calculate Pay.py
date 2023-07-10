'''
Algorithm:  Calculates pre-tax pay based on the number of hours worked and the
            hourly rate. If over 40 hours worked, then hourly pay is 1.5x.
'''
#Asks user to input number of hours worked and their hourly rate
hrstr = input("Enter Hours: ")
ratestr = input("Enter Hourly Rate: ")

#Validates that the inputted values were numeric, exits if not
try:
    fhr = float(hrstr)
    frate = float(ratestr)
except:
    print("Error, please enter numeric input")
    quit()

#Creates function that calculates the user's pay based on their inputted
#hours worked and hourly rate. If the user worked more than 40 hours, then
#they would get time and a half for the hours over 40
def computePay(hr, rate):
    if hr > 40.0:
        regpay = hr * rate
        otpay = (hr - 40.0) * (rate * 0.5)

        pay = regpay + otpay
        
        return pay
    else:
        pay = hr * rate

        return pay

#Calls the computePay function and prints the user's pay
print("Pay", computePay(fhr, frate))

