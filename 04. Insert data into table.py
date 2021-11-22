import mysql.connector

# Connecting to SQL database
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Your Password",
)

print(mydb)
mycursor=mydb.cursor()

mycursor.execute("USE ALT1")  # Running the USE query to select which database to use


email=str(input('Please enter customer email: '))
customer_total=str(input('Please enter the customer order total: '))

sql = "INSERT INTO Customer_Order_List (Customer_email, Customer_order_total) VALUES (%s, %s)"
val = (email, customer_total)
mycursor.execute(sql,val)
mydb.commit()


sql='SELECT * FROM Customer_Order_List'
mycursor.execute(sql)
for i in mycursor:
    print(i)

# How can i change this program to insert multiple records
