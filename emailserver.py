#!/usr/bin/env python
import subprocess
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import config

# Function to retrieve data from the last row of the database
smtp_server = config.Email_CONFIG['smtp_server']
port = config.Email_CONFIG['port']  # For starttls
sender_email = config.Email_CONFIG['sender_email']
password = config.Email_CONFIG['password']
#receiver_email = "tolib"

def get_last_application():
    try:
        # Execute MySQL command to select the last row from the ***REMOVED*** table
        sql_command = f'mysql -u {config.DATABASE_CONFIG['user']} -p {config.DATABASE_CONFIG['password']} -e "USE {config.DATABASE_CONFIG['database']}; SELECT * FROM {config.DATABASE_CONFIG['table']} ORDER BY id DESC LIMIT 1;"' 

        result = subprocess.run(sql_command, shell=True, capture_output=True, text=True)
        last_application_data = result.stdout.strip().split('\n')[1].split('\t')
        last_application = {
            'id': int(last_application_data[0]),
            'name': last_application_data[1],
            'phone': last_application_data[2],
            'email': last_application_data[3],
            'resume': last_application_data[4],
            'cover_letter': last_application_data[5],
            'additional_info': last_application_data[6],
        }
        return last_application
    except Exception as e:
        print("Error retrieving last application: ", e)

# Function to send email
def send_email():
    smtp_server = "***REMOVED***"
    port = ***REMOVED***
    sender_email = "***REMOVED***"
    password = config.email_password

    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = get_last_application()[3]
    message["Subject"] = "Application Received"
    body = "Greetings"
    message.attach(MIMEText(body, "plain"))
    server = smtplib.SMTP(smtp_server,port)
    server.starttls() # Secure the connection
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message.as_string())

send_email("Tolib","***REMOVED***")

    
