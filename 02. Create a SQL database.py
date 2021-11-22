import mysql.connector

# Connecting to SQL database
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Your Password",
)

print(mydb)

mycursor=mydb.cursor()

# Run query CREATE DATABASE to create a new database called ALT1
mycursor.execute("CREATE DATABASE ALT1")

# Try running this program twice and see what error you get
