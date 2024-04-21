import smtplib
import ssl
import os

port = 465
smtp_server = "smtp.gmail.com"
USERNAME = os.environ.get('USER_EMAIL')
PASSWORD = os.environ.get('USER_PASSWORD')
recipient_email = "tejasvinchurkar16@gmail.com"  # Replace with the recipient's email address

message = """
Subject: Unix Fastack Sanity Check

Hello Team, 

Please help me with the sanity check.
"""

context = ssl.create_default_context()

with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(USERNAME, PASSWORD)
    server.sendmail(USERNAME, recipient_email, message)
