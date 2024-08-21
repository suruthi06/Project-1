import mysql.connector as db
import pandas as pd
from mysql.connector import Error

# Database connection
connection = db.connect(
    host="localhost",
    user="root",
    port="3306",
    password="****",
    database="*****"
)

# Create a cursor
writer = connection.cursor()

# Query to drop the table if it exists and create a new one
table_query = '''
DROP TABLE IF EXISTS bus_routes;

CREATE TABLE bus_routes(
    id SERIAL PRIMARY KEY,
    route_name TEXT NOT NULL,
    route_link TEXT NOT NULL,
    busname TEXT NOT NULL,
    bustype TEXT NOT NULL,
    departing_time TIMESTAMP NOT NULL,
    duration TEXT NOT NULL,
    reaching_time TIMESTAMP NOT NULL,
    star_rating FLOAT NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    seats_available INT NOT NULL
)
'''

try:
    # Execute the query to create the table
    for statement in table_query.split(';'):
        if statement.strip():
            writer.execute(statement.strip())
    connection.commit()
    print("Table created successfully")
except Error as e:
    print(f"Error creating table: {e}")

# Read and combine all CSV files into one DataFrame
csv_files = ['bus_details.csv', 'bus_details1.csv', 'bus_details2.csv', 'bus_details3.csv', 'bus_details4.csv']
data = pd.concat([pd.read_csv(file) for file in csv_files])

# Prepare the insert query
insert_query = '''
INSERT INTO bus_routes (route_name, route_link, busname, bustype, departing_time, duration, reaching_time, star_rating, price, seats_available)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
'''

# Ensure datetime columns are correctly parsed
data['departing_time'] = pd.to_datetime(data['departing_time'])
data['reaching_time'] = pd.to_datetime(data['reaching_time'])

# Convert DataFrame rows to a list of tuples for executemany
data_tuples = [tuple(row) for row in data.itertuples(index=False, name=None)]

# Insert data into the table
try:
    writer.executemany(insert_query, data_tuples)
    connection.commit()
    print("Data inserted successfully")
except Error as e:
    print(f"Error inserting data: {e}")
finally:
    # Close the cursor and connection
    writer.close()
    connection.close()

