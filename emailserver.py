import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import config

# SMTP server configuration
smtp_server = "***REMOVED***"
port = ***REMOVED***  # For starttls
sender_email = "***REMOVED***"
password = config.email_password
receiver_email = "***REMOVED***"

# Create a multipart message and set headers
message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = "Blank"

# Body of email
body = "Greetings"
message.attach(MIMEText(body, "plain"))

# Connect to the server and send the email
server = None
try:
    server = smtplib.SMTP(smtp_server,port)
    server.starttls() # Secure the connection
    server.login(sender_email, password)
    # Send the email
    server.sendmail(sender_email, receiver_email, message.as_string())
    print("Email sent successfully")
except Exception as e:
    print(f"Error: {e}")
finally:
    server.quit()