import mysql.connector

connection = mysql.connector.connect(
#type in your username
user = "",
#type in your password
password = "",
#type in the database IP address your are connecting to
host = " . . . . "
#type in your database name you want to connect to 
database = " "
)

#here we initializing the selector to start interacting with the database 
selector = connection.Cursor()
#then start sending SQL queris to the selector to excute them ex: SELECT * FROM database-name
query = selector.excute("")
#storing the result and then printing it 
result = selector.fetchall()
print(result) 