import sqlite3

# Connect to SQLite database (or create a new one if it doesn't exist)
conn = sqlite3.connect('car_rental.db')
cursor = conn.cursor()

# Create a table for the car rental system
cursor.execute('''
    CREATE TABLE IF NOT EXISTS cars (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        brand TEXT NOT NULL,
        model TEXT NOT NULL,
        year INTEGER NOT NULL,
        rental_rate REAL NOT NULL
    )
''')

# Function to add a new car to the database
def add_car(brand, model, year, rental_rate):
    cursor.execute('''
        INSERT INTO cars (brand, model, year, rental_rate)
        VALUES (?, ?, ?, ?)
    ''', (brand, model, year, rental_rate))
    conn.commit()
    print("Car added successfully!")

# Function to display all cars in the database
def display_cars():
    cursor.execute('SELECT * FROM cars')
    cars = cursor.fetchall()

    if not cars:
        print("No cars available.")
    else:
        print("Car ID | Brand  | Model  | Year | Rental Rate")
        print("----------------------------------------------")
        for car in cars:
            print(f"{car[0]} | {car[1]} | {car[2]} | {car[3]} | ${car[4]}")

# Function to update information for a specific car
def update_car(car_id, brand, model, year, rental_rate):
    cursor.execute('''
        UPDATE cars
        SET brand=?, model=?, year=?, rental_rate=?
        WHERE id=?
    ''', (brand, model, year, rental_rate, car_id))
    conn.commit()
    print("Car information updated successfully!")

# Function to delete a car from the database
def delete_car(car_id):
    cursor.execute('DELETE FROM cars WHERE id=?', (car_id,))
    conn.commit()
    print("Car deleted successfully!")

# Console-based menu
def main():
    while True:
        print("\nCar Rental System Menu:")
        print("1. Display Cars")
        print("2. Add Car")
        print("3. Update Car")
        print("4. Delete Car")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            display_cars()
        elif choice == '2':
            brand = input("Enter the brand: ")
            model = input("Enter the model: ")
            year = int(input("Enter the year: "))
            rental_rate = float(input("Enter the rental rate: "))
            add_car(brand, model, year, rental_rate)
        elif choice == '3':
            car_id = int(input("Enter the car ID to update: "))
            brand = input("Enter the new brand: ")
            model = input("Enter the new model: ")
            year = int(input("Enter the new year: "))
            rental_rate = float(input("Enter the new rental rate: "))
            update_car(car_id, brand, model, year, rental_rate)
        elif choice == '4':
            car_id = int(input("Enter the car ID to delete: "))
            delete_car(car_id)
        elif choice == '5':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == '__main__':
    main()

# Close the database connection
conn.close()
