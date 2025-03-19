import mysql.connector #this is the library that we will use to connect to the database
conn=mysql.connector.connect(
    host="localhost" # this is the host where the database is located
    user="root" # this is the username that we will use to connect to the database
    password="Ji20zer00@john" # this is the password that we will use to connect to the database
)
cursor = conn.cursor()
database_name = "SalesDB" # this is the name of the database that we will use
cursor.execute(f"CREATE DATABASE IF NOT EXISTS SalesDB")
print(f"Database 'SalesDB' created successifully!")
cursor.close()
conn.close()