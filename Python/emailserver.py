#!/usr/bin/env python

import os
import subprocess
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Email configuration
smtp_server = os.getenv('MAIL_SERVER')
port = int(os.getenv('PORT'))
sender_email = os.getenv('SENDER_EMAIL')
password = os.getenv('SENDER_PASSWORD')

# Database configuration
db_user = os.getenv('USER')
db_password = os.getenv('MYSQL_PWD')
db_database = os.getenv('MYSQL_DATABASE')
db_table = os.getenv('TABLE1')

def get_last_application():
    try:
        # Execute MySQL command to select the last row from the ***REMOVED*** table
        sql_command = f"mysql -u {db_user} -p{db_password} -e \"USE {db_database}; SELECT * FROM {db_table} ORDER BY id DESC LIMIT 1;\""
        
        result = subprocess.run(sql_command, shell=True, capture_output=True, text=True)
        last_application_data = result.stdout.strip().split('\n')[1].split('\t')
        last_application = {
            'id': int(last_application_data[0]),
            'firstName': last_application_data[1],
            'lastName': last_application_data[2],
            'phone': last_application_data[3],
            'email': last_application_data[4],
            'resume': last_application_data[5],
            'cover_letter': last_application_data[6],
            'additional_info': last_application_data[7],
            'job': last_application_data[8]
        }
        return last_application
    except Exception as e:
        print("Error retrieving last application: ", e)

# Function to send email
def send_email(subject='', body='', bcc='', receiver_email=''):
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    message.attach(MIMEText(body, "plain"))
    
    server = smtplib.SMTP(smtp_server, port)
    server.starttls()  # Secure the connection
    server.login(sender_email, password)
    
    recipients = [receiver_email] + ([bcc] if bcc else [])
    server.sendmail(sender_email, recipients, message.as_string())
    
    server.quit()  # Close the connection

def application_received(application):
    email_body = f"""Dear {application["firstName"]} {application["lastName"]},

Thank you for your interest in joining our team at Santek. We appreciate the time and effort you've taken to apply for the {application['job']} role.

We'll be in touch shortly regarding the status of your application. If you have any questions or would like to provide additional information, please feel free to reach out to us at {sender_email}.

Thank you once again for considering a career with us. We look forward to the possibility of working together to turn innovative ideas into reality.

Best regards,

Tolib Sanni II
CEO
Santek
{sender_email}"""
    send_email(subject="Application Received", receiver_email=application["email"], body=email_body)

# Retrieve the last application and send confirmation email
application = get_last_application()
if application:
    application_received(application)
else:
    print("No application found to send confirmation email.")

