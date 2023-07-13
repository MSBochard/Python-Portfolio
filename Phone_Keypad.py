# Algorithm:     Convert a phone number with letters into a dialable, numeric phone number.

def main():

    ph_num = input("Enter the phone number to be converted: ")
    converted_num = getNumber(ph_num)
    print("The numerical version of the phone number is:", converted_num)
    

def getNumber(string):
    ph_str = string.upper()
    new_ph_str = ''
    for index in range(0, len(ph_str)):
        if ph_str[index] in 'ABC':
            new_ph_str += '2'
        elif ph_str[index] in 'DEF':
            new_ph_str += '3'
        elif ph_str[index] in 'GHI':
            new_ph_str += '4'
        elif ph_str[index] in 'JKL':
            new_ph_str += '5'
        elif ph_str[index] in 'MNO':
            new_ph_str += '6'
        elif ph_str[index] in 'PQRS':
            new_ph_str += '7'
        elif ph_str[index] in 'TUV':
            new_ph_str += '8'
        elif ph_str[index] in 'WXYZ':
            new_ph_str += '9'
        else:
            new_ph_str += ph_str[index]

    return new_ph_str

main()
