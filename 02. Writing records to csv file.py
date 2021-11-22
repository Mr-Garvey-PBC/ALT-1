import csv         # Import the csv module to use appropriate libraires and methods to deal with csv files

file=open('patients.csv','a',newline='')  # Opens a file called patients.csv or creates it if it doesnt exist, a means to open the file so it can be appended
db=csv.writer(file)  # Making a connection to our file to make it available to write to, we assign this connection to the variable db as a shortcut

record1=['Martin','Garvey','111111','1984','37']
record2=['Joe','Blog','222222','1990','31']

db.writerow(record1)
db.writerow(record2)
  
file.close()         # Close our file.    


# Task 1
# How could we use a loop to minimise manually adding lots of lists to record data

# Task 2
# How could we use a function to minimise manually adding lots of lists to record data




# TASK 1 - SOLUTION
# write_to_file='y'
# while write_to_file=='y':
#     record=[]
#     first_name=str(input('Please enter the first name: '))
#     sur_name=str(input('Please enter the sur name: '))
#     phone_number=str(input('Please enter the phone number: '))
#     dob=str(input('Please enter the dob: '))
#     age=str(input('Please enter the age: '))
#     record.extend([first_name,sur_name,phone_number,dob,age])
#     db.writerow(record)
#     write_to_file=str(input('Do you want to add another record y/n: '))
#     write_to_file=write_to_file.lower()

