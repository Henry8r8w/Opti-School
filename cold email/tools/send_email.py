import smtplib
import os
import typing
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders



def send_email(recipient_email: str, company: str, representative: str = "", 
               sender_name: str = "", subject: str = "", 
               template_path: str = "", attachments: list = []) -> None:
    with open(template_path, "r") as file: 
        body = file.read()
    
    body = body.replace("<Entity>",entity)
    body = body.replace("<Representative>", representative)
    body = body.replace("<Sender>", sender_name)
    
    sender_email = "your_email"  
    sender_password = "owey qwep qfcj bevr"  # obtain your app password and put it here
    smtp_server = "smtp.gmail.com" 
    smtp_port = 587
    
    msg = MIMEMultipart() 
    msg["From"] = sender_email
    msg["To"] = recipient_email
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain"))


    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(sender_email, sender_password)
    server.sendmail(sender_email, recipient_email, msg.as_string())
    server.quit()
    print("success at delivering to ",recipient_email )

   
