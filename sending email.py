import smtplib
import ssl
from email.message import EmailMessage

# Define email sender and receiver
email_sender = 'cpe4735@stacmail.net'
email_password = 'your_app_password' # Use an App Password if 2FA is on
email_receiver = 'cameronrobertpetrie@gmail.com'

# Set the subject and body of the email
subject = 'Email From Python'
body = """
This is a test email sent from a Python script.
You can include multiple lines here.
"""

# Create the email message object
msg = EmailMessage()
msg.set_content(body)
msg['Subject'] = subject
msg['From'] = email_sender
msg['To'] = email_receiver

# Add SSL (secure) context
context = ssl.create_default_context()

# Log in to the SMTP server and send the email
try:
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.ehlo()  # Optional, but good practice
        server.starttls(context=context) # Secure the connection
        server.ehlo()  # Can be called again
        server.login(email_sender, email_password)
        server.send_message(msg)
    print("Email sent successfully!")

except smtplib.SMTPException as e:
    print(f"Error: unable to send email. {e}")
