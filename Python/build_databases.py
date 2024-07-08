import os
import mysql.connector
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Database configuration
db_host = os.getenv('MYSQL_HOST')
db_user = os.getenv('USER')
db_password = os.getenv('MYSQL_PWD')
db_database = os.getenv('MYSQL_DATABASE')
table1 = os.getenv('TABLE1')
table2 = os.getenv('TABLE2')
mydb = 0
y = 0
# Check if all necessary environment variables are loaded
if not all([db_host, db_user, db_password, db_database, table1, table2]):
    for x in [db_host, db_user, db_password, db_database, table1, table2]:
        y += 1
        try:
            print(x)
        except:
            print(y)
    raise ValueError("Some environment variables are missing. Please check the .env file." )
    

try:
    # Establish connection to MySQL server
    mydb = mysql.connector.connect(
        host=db_host,
        user=db_user,
        password=db_password
    )

    # Create a cursor object to interact with the database
    with mydb.cursor() as mycursor:
        # Check if the database exists
        mycursor.execute("SHOW DATABASES")
        databases = mycursor.fetchall()
        database_exists = any(db[0] == db_database for db in databases)

        # If the database doesn't exist, create it
        if not database_exists:
            mycursor.execute(f"CREATE DATABASE {db_database}")
            print("Database created successfully.")

        # Select the database
        mycursor.execute(f"USE {db_database}")

        # Function to check if a table exists
        def check_table_exists(table_name):
            mycursor.execute("SHOW TABLES")
            tables = mycursor.fetchall()
            return any(table[0] == table_name for table in tables)

        # If the first table doesn't exist, create it
        if not check_table_exists(table1):
            mycursor.execute(f"""
                CREATE TABLE {table1} (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    firstName VARCHAR(255),
                    lastName VARCHAR(255),
                    phone VARCHAR(20),
                    email VARCHAR(255),
                    resume BLOB,
                    cover_letter BLOB,
                    additional_info TEXT,
                    job VARCHAR(255)
                )
            """)
            print(f"Table {table1} created successfully.")

        # If the second table doesn't exist, create it
        if not check_table_exists(table2):
            mycursor.execute(f"""
                CREATE TABLE {table2} (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    name VARCHAR(255),
                    alias VARCHAR(255),
                    description VARCHAR(255),
                    locations VARCHAR(255),
                    datePosted INT,
                    type VARCHAR(50)
                )
            """)
            print(f"Table {table2} created successfully.")

    # Commit changes
    mydb.commit()

except mysql.connector.Error as err:
    print(f"Error: {err}")

finally:
    # Close database connection
    if mydb.is_connected():
        mydb.close()
        print("Database connection closed.")
