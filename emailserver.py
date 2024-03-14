import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import pymysql
import config

# Connect to the MySQL database
connection = pymysql.connect(
    host='localhost',
    user='***REMOVED***',
    password='***REMOVED***',
    database='***REMOVED***',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)

# Function to retrieve data from the last row of the database
def get_last_application():
    try:
        with connection.cursor() as cursor:
            # Select the last row from the ***REMOVED*** table
            sql = "SELECT * FROM ***REMOVED*** ORDER BY id DESC LIMIT 1"
            cursor.execute(sql)
            last_application = cursor.fetchone()
            return last_application
    except Exception as e:
        print("Error retrieving last application ")

# Function to send email
def send_email(name, email):
    smtp_server = "***REMOVED***"
    port = ***REMOVED***
    sender_email = "***REMOVED***"
    password = config.email_password

    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = email
    message["Subject"] = "Application Received"

    body = f"Hello {name},\n\nThank you for your application."
    message.attach(MIMEText(body, "plain"))

    server = None
    try:
        server = smtplib.SMTP(smtp_server, port)
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, email, message.as_string())
        print("Email sent successfully")
    except Exception as e:
        print("Error sending email")
    finally:
        if server:
            server.quit()

# Retrieve data from the last application
last_application = get_last_application()
if last_application:
    name = last_application['name']
    email = last_application['email']

    # Send email confirmation
    send_email(name, email)

# Close database connection
send_email("tolib", )
connection.close()
