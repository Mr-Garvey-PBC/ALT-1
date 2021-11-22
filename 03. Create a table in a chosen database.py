import mysql.connector

# Connecting to SQL database
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Your Password",
)

print(mydb)

mycursor=mydb.cursor()

database_input=str(input('Enter the name of the existing database you want to use: '))  # ALT1, name must match exactly
mycursor.execute(f"USE {database_input}")  # Running the USE query to select which database to use

# Create two tables in the database selected in line 14

# Creating a table takes the format of:
# mycursor.execute("CREATE TABLE table_name(column1 datatype(255),column2 datatype(255), column3 datatype(255)")
# 255 represents the number of characters in the datatype you declare, 255 is just a standard number used.

mycursor.execute("CREATE TABLE Customer_Order_List (Customer_email VARCHAR(255), Customer_order_total VARCHAR(255))")

# Show the tables in the database
mycursor.execute('SHOW TABLES')
for x in mycursor:
    print(x)

# Can you identify anyways to improve the user experience?
