import mysql.connector
import config

# Establish connection to MySQL server
mydb = mysql.connector.connect(
    host=config.DATABASE_CONFIG['host'],
    user=config.DATABASE_CONFIG['user'],
    password=config.DATABASE_CONFIG['password']
)

# Create a cursor object to interact with the database
mycursor = mydb.cursor()

# Check if the database exists
mycursor.execute("SHOW DATABASES")
databases = mycursor.fetchall()
database_exists = False
for db in databases:
    if db[0] == config.DATABASE_CONFIG['database']:
        database_exists = True
        break

# If the database doesn't exist, create it
if not database_exists:
    mycursor.execute(f"CREATE DATABASE {config.DATABASE_CONFIG['database']}")
    print("Database created successfully.")

# Select the database
mycursor.execute(f"USE {config.DATABASE_CONFIG['database']}")

# Check if the table exists
mycursor.execute("SHOW TABLES")
tables = mycursor.fetchall()
table_exists = False
for table in tables:
    if table[0] == config.DATABASE_CONFIG['table1']:
        table_exists = True
        break

# If the table doesn't exist, create it
if not table_exists:
    mycursor.execute(f"CREATE TABLE {config.DATABASE_CONFIG['table1']} (id INT AUTO_INCREMENT PRIMARY KEY, firstName VARCHAR(255), lastName VARCHAR(255), phone VARCHAR(20), email VARCHAR(255), resume BLOB, cover_letter BLOB, additional_info TEXT, job VARCHAR(255))")
    print(f"Table {config.DATABASE_CONFIG['table1']} created successfully.")

# Check if the second table exists
table_exists = False
for table in tables:
    if table[0] == config.DATABASE_CONFIG['table2']:
        table_exists = True
        break

# If the second table doesn't exist, create it
if not table_exists:
    mycursor.execute(f"CREATE TABLE {config.DATABASE_CONFIG['table2']} (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), alias VARCHAR(255), description VARCHAR(255), locations VARCHAR(255), datePosted INT, type VARCHAR(50))")
    print(f"Table {config.DATABASE_CONFIG['table2']} created successfully.")

# Commit changes
mydb.commit()

# Close cursor and database connection
mycursor.close()
mydb.close()
