import sqlite3

# Connect to SQLite database (or create a new one if it doesn't exist)
conn = sqlite3.connect('car_rental.db')

# Create a cursor object to execute SQL queries
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

# Example usage
add_car('Toyota', 'Camry', 2020, 50.0)
add_car('Honda', 'Civic', 2021, 45.0)
add_car('Ford', 'Escape', 2019, 55.0)

display_cars()

update_car(2, 'Honda', 'Accord', 2022, 48.0)

delete_car(1)

display_cars()

# Close the database connection
conn.close()
