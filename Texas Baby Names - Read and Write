'''
Algorithm:     This algorithm reads in a file and answers a series of questions
               based on the information in the file. The answers are written
               out to a seperate file.
'''

#Reads the .txt file containing the names and writes the output file containing the answers
def main():
    infile = open("c:\\TestData\\TXBabyNames.txt", "r")
    content = infile.readlines()
    infile.close()

    outfile = open("c:\\TestData\\BochardM_TXBabyNames.txt", "w")

    outfile.write("Homework 5 by Madison Bochard\n\n")
    
    girls_since_1910(content, outfile)
    boys_since_1910(content, outfile)
    girls_born_1910_2012(content, outfile)
    boys_born_1910_2012(content, outfile)
    total_born_2012(content, outfile)
    total_your_name_since_1910(content, outfile)
    total_your_name_1910_to_1960(content, outfile)
    most_popular_boy_name(content, outfile)
    most_popular_girl_name(content, outfile)
    most_popular_year_your_name(content, outfile)
    
    outfile.close()

#How many girl babies have been born since 1910?
def girls_since_1910(data, file):
    girls_sum = 0
    
    for line in data:
        record = line.strip()
        record_list = record.split(",")
        if record_list[1] == "F":
            girls_sum += int(record_list[4])

    file.write("Question 1: How many girl babies have been born since 1910?\n")
    file.write("The number of baby girls born since 1910 is **"\
               + str(girls_sum) + "**.\n\n")

#How many boy babies have been born since 1910?
def boys_since_1910(data, file):
    boys_sum = 0
    
    for line in data:
        record = line.strip()
        record_list = record.split(",")
        if record_list[1] == "M":
            boys_sum += int(record_list[4])

    file.write("Question 2: How many boy babies have been born since 1910?\n")
    file.write("The number of baby boys born since 1910 is **"\
               + str(boys_sum) + "**.\n\n")

#How many girl babies were born 1910?  In 2012?
def girls_born_1910_2012(data, file):
    girls_born_1910 = 0
    girls_born_2012 = 0
    
    for line in data:
        record = line.strip()
        record_list = record.split(",")
        if record_list[1] == "F" and record_list[2] == "1910":
            girls_born_1910 += int(record_list[4])
        if record_list[1] == "F" and record_list[2] == "2012":
            girls_born_2012 += int(record_list[4])
            
    file.write("Question 3: How many girl babies were born in 1910? In 2012?\n")
    file.write("The number of baby girls born in 1910 is **" + str(girls_born_1910)\
               + "** and the number born in 2012 is **"\
               + str(girls_born_2012) + "**.\n\n")

#How many boy babies were born in 1910?  In 2012?
def boys_born_1910_2012(data, file):
    boys_born_1910 = 0
    boys_born_2012 = 0
    
    for line in data:
        record = line.strip()
        record_list = record.split(",")
        if record_list[1] == "M" and record_list[2] == "1910":
            boys_born_1910 += int(record_list[4])
        if record_list[1] == "M" and record_list[2] == "2012":
            boys_born_2012 += int(record_list[4])
            
    file.write("Question 4: How many boy babies were born in 1910?  In 2012?\n")
    file.write("The number of baby boys born in 1910 is **"\
               + str(boys_born_1910) + "** and the number born in 2012 is **"\
               + str(boys_born_2012) + "**.\n\n")

#What are the total number of babies born in Texas in 2012?
def total_born_2012(data, file):
    total_2012 = 0
    
    for line in data:
        record = line.strip()
        record_list = record.split(",")
        if record_list[2] == "2012":
            total_2012 += int(record_list[4])
    
    file.write("Question 5: What are the total number of babies born in Texas "\
               + "in 2012?\n")
    file.write("The total number of babies born in 2012 is **"\
               + str(total_2012) + "**.\n\n")

#What are the total number of babies born in Texas with your name since 1910?
def total_your_name_since_1910(data, file):
    total_name = 0

    for line in data:
        record = line.strip()
        record_list = record.split(",")
        if record_list[3] == "Madison":
            total_name += int(record_list[4])

    file.write("Question 6: What are the total number of babies born in Texas "\
               + "with your name since 1910?\n")
    file.write("The total number of babies born since 1910 with "\
               + "the name Madison is **" + str(total_name) + "**.\n\n")
        
#What are the total number of babies born in Texas with your name between
#1910 and 1960?
def total_your_name_1910_to_1960(data, file):
    total_name_1910_to_1960 = 0

    for line in data:
        record = line.strip()
        record_list = record.split(",")
        if int(record_list[2]) >= 1910 and int(record_list[2]) <= 1960:
            if record_list[3] == "Madison":
                total_name_1910_to_1960 += int(record_list[4])

    file.write("Question 7: What are the total number of babies born in "\
               + "Texas with your name between 1910 and 1960?\n")
    file.write("The total number of babies born bewteen 1910 and 1960 "\
               + "with the name Madison is **" + str(total_name_1910_to_1960)\
               + "**, all of which are male because the name Madison did "\
               + "not become a feminine name until 1985.\n\n")

#What name was the most popular (had the highest count in one year):
#List the count for boys and then for girls.
#                       And
#What year was that? List the year the name was the most popular for
#boys and then for girls.
def most_popular_boy_name(data, file):
    popular_name_amount = 0
    popular_name = ""
    popular_year = ""
    data_list = []
    year = 1910
    amount_list = []
    
    for line in data:
        record = line.strip()
        record_list = record.split(",")
        data_list.append(record_list)

    for i in range(0, len(data_list)):
        if data_list[i][1] == "M" and int(data_list[i][2]) == year:
            amount_list.append(int(data_list[i][4]))
            year += 1

    popular_name_amount = max(amount_list)

    for i in range(0, len(data_list)):
        if int(data_list[i][4]) == popular_name_amount:
            popular_name = data_list[i][3]
            popular_year = data_list[i][2]
        
    file.write("Questions 8 & 9: What boy name was the most popular? "\
               + "What year was that?\n")
    file.write("The most popular boy name was **" + str(popular_name) + "** with **"\
               + str(popular_name_amount) + "** babies born in the year **"\
               + str(popular_year) + "**.\n\n")

#Answers the same questions as above but for most popular girl name
def most_popular_girl_name(data, file):
    popular_name_amount = 0
    popular_name = ""
    popular_year = ""
    data_list = []
    year = 1910
    amount_list = []
    
    for line in data:
        record = line.strip()
        record_list = record.split(",")
        data_list.append(record_list)

    for i in range(0, len(data_list)):
        if data_list[i][1] == "F" and int(data_list[i][2]) == year:
            amount_list.append(int(data_list[i][4]))
            year += 1

    popular_name_amount = max(amount_list)

    for i in range(0, len(data_list)):
        if int(data_list[i][4]) == popular_name_amount:
            popular_name = data_list[i][3]
            popular_year = data_list[i][2]
        
    file.write("Questions 8 & 9: What girl name was the most popular? "\
               + "What year was that?\n")
    file.write("The most popular girl name was **" + str(popular_name) + "** with **"\
               + str(popular_name_amount) + "** babies born in the year **"\
               + str(popular_year) + "**.\n\n")

#In what year was your name (or Ira's name) the most popular (had the highest count)?
def most_popular_year_your_name(data, file):
    popular_name_amount = 0
    popular_year = ""
    data_list = []
    amount_list = []    

    for line in data:
        record = line.strip()
        record_list = record.split(",")
        data_list.append(record_list)

    for i in range(0, len(data_list)):
        if data_list[i][3] == "Madison" and data_list[i][1] == "F":
            amount_list.append(int(data_list[i][4]))

    popular_name_amount = max(amount_list)

    for i in range(0, len(data_list)):
        if int(data_list[i][4]) == popular_name_amount:
            popular_year = data_list[i][2]

    file.write("Question 10: In what year was your name the most popular?\n")
    file.write("The year where Madison was the most popular female name was **"\
               + str(popular_year) + "** with a count of **"\
               + str(popular_name_amount) + "**.\n\n")


        
main()
