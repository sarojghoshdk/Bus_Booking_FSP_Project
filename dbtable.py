import mysql.connector

database = mysql.connector.connect(
    host='localhost',
    user='root',
    password='1234'
)
connection = database.cursor()
selectdb = 'use bus_booking'
connection.execute(selectdb)
tableCreationQuery = '''

create table passenger(
                    id int primary key auto_increment,
                    name varchar(255),
                    age int,
                    no_of_passenger int,
                    source varchar(255),
                    destination varchar(255),
                    price int)
'''
connection.execute(tableCreationQuery)
connection = database.cursor()
describeTableQuery = 'DESC passenger'
connection.execute(describeTableQuery)
for descriptions in connection:
    print(descriptions)
database.close()