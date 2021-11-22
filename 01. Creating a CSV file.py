import csv         # Import the csv module to use appropriate libraires and methods to deal with csv files

header= ['First-Name','LastName','PhoneNum','dob','age'] # Create a list called header that contains the attributes for the database

file=open('patients.csv','a',newline='')  # Opens a file called patients.csv or creates it if it doesnt exist, a means to open the file so it can be appended
print(file)
db=csv.writer(file)  # Making a connection to our file to make it available to write to, we assign this connection to the variable db as a shortcut
db.writerow(header)  # Write the header list to our file

file.close()         # Close our file.
