import mysql.connector
from datetime import datetime

# Database connection
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="bus_booking"
)
cursor = conn.cursor()

# Create table
cursor.execute('''
CREATE TABLE IF NOT EXISTS bookings (
    passenger_id INT AUTO_INCREMENT PRIMARY KEY,
    passenger_name VARCHAR(255) NOT NULL,
    passenger_age INT NOT NULL,
    no_of_passengers INT NOT NULL,
    datetime_of_booking DATETIME NOT NULL,
    price FLOAT NOT NULL
)
''')
conn.commit()

# Constants
TOTAL_SEATS = 50
PRICE = 1500
SOURCE = "Asansol"
DESTINATION = "Kolkata"


def check_seat_availability():
    cursor.execute('SELECT SUM(no_of_passengers) FROM bookings')
    booked_seats = cursor.fetchone()[0] or 0
    available_seats = TOTAL_SEATS - booked_seats
    print(f"Available seats: {available_seats}")


def book_ticket():
    passenger_name = input("Enter passenger name: ")
    passenger_age = int(input("Enter passenger age: "))
    no_of_passengers = int(input("Enter number of passengers: "))

    cursor.execute('SELECT SUM(no_of_passengers) FROM bookings')
    booked_seats = cursor.fetchone()[0] or 0
    available_seats = TOTAL_SEATS - booked_seats

    if no_of_passengers > available_seats:
        print(f"Sorry, only {available_seats} seats are available.")
        return

    price = PRICE * no_of_passengers
    if passenger_age > 60:
        price *= 0.5

    datetime_of_booking = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    cursor.execute('''
    INSERT INTO bookings (passenger_name, passenger_age, no_of_passengers, datetime_of_booking, price)
    VALUES (%s, %s, %s, %s, %s)
    ''', (passenger_name, passenger_age, no_of_passengers, datetime_of_booking, price))
    conn.commit()
    print("Booking successful!")


def show_all_bookings():
    cursor.execute('SELECT * FROM bookings')
    bookings = cursor.fetchall()
    for booking in bookings:
        #print(booking)
        print(f"ID: {booking[0]}, Name: {booking[1]}, Age: {booking[2]}, No of Passengers: {booking[3]}, Date & Time of Booking: {booking[4]}, Price: {booking[5]}")


def update_booking():
    passenger_id = int(input("Enter passenger ID to update: "))
    cursor.execute('SELECT * FROM bookings WHERE passenger_id = %s', (passenger_id,))
    booking = cursor.fetchone()
    if not booking:
        print("Booking not found!")
        return

    passenger_name = input(f"Enter new passenger name (current: {booking[1]}): ") or booking[1]
    passenger_age = input(f"Enter new passenger age (current: {booking[2]}): ") or booking[2]
    no_of_passengers = input(f"Enter new number of passengers (current: {booking[3]}): ") or booking[3]

    price = PRICE * int(no_of_passengers)
    if int(passenger_age) > 60:
        price *= 0.5

    cursor.execute('''
    UPDATE bookings
    SET passenger_name = %s, passenger_age = %s, no_of_passengers = %s, price = %s
    WHERE passenger_id = %s
    ''', (passenger_name, passenger_age, no_of_passengers, price, passenger_id))
    conn.commit()
    print("Booking updated successfully!")


def cancel_booking():
    passenger_id = int(input("Enter passenger ID to cancel: "))
    cursor.execute('SELECT * FROM bookings WHERE passenger_id = %s', (passenger_id,))
    booking = cursor.fetchone()
    if not booking:
        print("Booking not found!")
        return

    cursor.execute('DELETE FROM bookings WHERE passenger_id = %s', (passenger_id,))
    conn.commit()
    print("Booking cancelled successfully!")


def main():
    while True:
        print("\nMenu:")
        print("1. Seat availability")
        print("2. Booking portal")
        print("3. Show all bookings")
        print("4. Update booking details")
        print("5. Cancel booking")
        print("6. Exit application")

        choice = input("Enter your choice: ")

        if choice == '1':
            check_seat_availability()
        elif choice == '2':
            book_ticket()
        elif choice == '3':
            show_all_bookings()
        elif choice == '4':
            update_booking()
        elif choice == '5':
            cancel_booking()
        elif choice == '6':
            break
        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()

# Close the connection
conn.close()