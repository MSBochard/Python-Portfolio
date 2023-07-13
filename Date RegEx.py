"""
Algorithm:     Write a regular expression that will clean up dates
               in different date formats (such as 4/16/2017, 04/16/2017,
               and 2016/4/16) by replacing them with dates in a single,
               standard format.
"""

import re

def main():
    date = input("Enter in a numerical date: ")

    newDate = dateConversion(date)

    print(newDate)
    restart()

def restart():
    go = input("Would you like to enter a new date? yes or no: ")

    if go.lower() == 'yes':
        main()
    else:
        exit()

def dateConversion(date):
    #MDYYYY
    if re.search(r"^(\d{1})/(\d{1})/(\d{4})$", date):
        return re.sub(r"(\d{1})/(\d{1})/(\d{4})", r"0\1/0\2/\3", date)
    #MDDYYYY
    elif re.search(r"^(\d{1})/(\d{2})/(\d{4})$", date):
        return re.sub(r"(\d{1})/(\d{2})/(\d{4})", r"0\1/\2/\3", date)
    #MMDYYYY
    elif re.search(r"^(\d{2})/(\d{1})/(\d{4})$", date):
        return re.sub(r"(\d{2})/(\d{1})/(\d{4})", r"\1/0\2/\3", date)
    #MMDDYYYY
    elif re.search(r"^(\d{2})/(\d{2})/(\d{4})$", date):
        return date
    #YYYYMD
    elif re.search(r"^(\d{4})/(\d{1})/(\d{1})$", date):
        return re.sub(r"(\d{4})/(\d{1})/(\d{1})", r"0\2/0\3/\1", date)
    #YYYYMMD
    elif re.search(r"^(\d{4})/(\d{2})/(\d{1})$", date):
        return re.sub(r"(\d{4})/(\d{2})/(\d{1})", r"\2/0\3/\1", date)
    #YYYYMDD
    elif re.search(r"^(\d{4})/(\d{1})/(\d{2})$", date):
        return re.sub(r"(\d{4})/(\d{1})/(\d{2})", r"0\2/\3/\1", date)
    #YYYYMMDD
    elif re.search(r"^(\d{4})/(\d{2})/(\d{2})$", date):
        return re.sub(r"(\d{4})/(\d{2})/(\d{2})", r"\2/\3/\1", date)
    
main()
