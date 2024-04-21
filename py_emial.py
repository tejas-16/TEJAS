
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(subject, message, from_email, to_email, smtp_server, smtp_port, smtp_username, smtp_password):
    msg = MIMEMultipart()
    msg['tejasvinchurkar16@gmail.com'] = from_email
    msg['tejasvinchurkar.scoe.comp@gmail.com'] = to_email
    msg['Subject: Unix Fastack Sanity Checkbject'] = subject
    msg.attach(MIMEText(message, "Hello Team, /Please help me with the sanity check."))

    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(smtp_username, smtp_password)
    server.sendmail(from_email, to_email, msg.as_string())
    server.quit()

# Example usage:
send_email("Subject: Unix Fastack Sanity Checkbject", "Hello Team,/Please help me with the sanity check.", "tejasvinchurkar16@example.com", "tejasvinchurkar.scoe.comp@example.com", "smtp.gmail.com", 587, "smtp_username", "smtp_password")



    
    
   
