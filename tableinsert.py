import mysql.connector

database = mysql.connector.connect(
    host='localhost',
    user='root',
    password='1234'
)
connection = database.cursor()
selectdb = 'use bus_booking'
connection.execute(selectdb)

name = (input("Passenger Name : "))
age = (int(input("Passenger Age : ")))
no_of_passenger = (int(input("No of Passenger : ")))
source = (input("Passenger Source : "))
destination = (input("Passenger Destination : "))
price = (int(input("Price : ")))


insertQuery = '''
          insert into passenger(name,age,no_of_passenger,source,destination,price) values (%s,%s,%s,%s,%s,%s);
'''

insertvalues = [
    (name,age,no_of_passenger,source,destination,price)
]
connection.executemany(insertQuery,insertvalues)
database.commit()
database.close()
