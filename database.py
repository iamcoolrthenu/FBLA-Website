import mysql.connector

# Connect to the MySQL server
db_connection = mysql.connector.connect(
    host="localhost",
    user="***REMOVED***",
    password="***REMOVED***",
    database="***REMOVED***"
)

# Create a cursor object to execute SQL queries
cursor = db_connection.cursor()

# Create a new table
create_table_query = """
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password VARCHAR(100) NOT NULL
)
"""
cursor.execute(create_table_query)

# Commit changes and close the connection
db_connection.commit()
db_connection.close()

print("Database and table created successfully!")
