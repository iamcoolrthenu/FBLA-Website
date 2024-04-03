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
 
def get_last_application():
    try:
        # Execute MySQL command to select the last row from the ***REMOVED*** table
        sql_command = f'mysql -u {config.DATABASE_CONFIG['user']} -p {config.DATABASE_CONFIG['password']} -e "USE {config.DATABASE_CONFIG['database']}; SELECT * FROM {config.DATABASE_CONFIG['table']} ORDER BY id DESC LIMIT 1;"' 

        result = subprocess.run(sql_command, shell=True, capture_output=True, text=True)
        last_application_data = result.stdout.strip().split('\n')[1].split('\t')
        last_application = {
            'id': int(last_application_data[0]),
            'firstName': last_application_data[1],
            'lastName' : last_application_data[2],
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
application = get_last_application()
def send_email(subject='', body='', bcc='',receiver_email=''):
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    body = body
    message.attach(MIMEText(body, "plain"))
    server = smtplib.SMTP(smtp_server,port)
    server.starttls() # Secure the connection
    server.login(sender_email, password)
    recipients = [receiver_email] + [bcc] if bcc else [receiver_email]
    server.sendmail(sender_email, recipients, message.as_string())

def application_received():
    send_email(subject="Application Received", receiver_email=application["email"], body=f"""Dear {application["firstName"]} {application["lastName"]},

Thank you for your interest in joining our team at Santek. We appreciate the time and effort you've taken to apply for the {application['job']} role.

We'll be in touch shortly regarding the status of your application. If you have any questions or would like to provide additional information, please feel free to reach out to us at {config.Email_CONFIG['sender_email']}.

Thank you once again for considering a career with us. We look forward to the possibility of working together to turn innovative ideas into reality.

Best regards,

Tolib Sanni II
CEO
Santek
{config.Email_CONFIG['sender_email']}""")
    
