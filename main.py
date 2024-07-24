import mysql.connector

database = mysql.connector.connect(
    host='localhost',
    user='root',
    password='1234'
)
connection = database.cursor()
databaseCreationQuery = 'CREATE DATABASE bus_booking'
connection.execute(databaseCreationQuery)

displayingDatabasesQuery = 'SHOW DATABASES'
connection.execute(displayingDatabasesQuery)

for databases in connection:
    print(databases)
connection = database.cursor()

database.close()
