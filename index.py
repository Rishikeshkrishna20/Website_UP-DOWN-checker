import requests
import smtplib
from email.mime.text import MIMEText #used for sending plain text email
from email.mime.multipart import MIMEMultipart
import os
from dotenv import load_dotenv

load_dotenv();#load the environment variable 
def check_website(url):
    try:
        response = requests.get(url)
        print(response)
        if response.status_code == 200:
            return True
        else:
            return False
    except Exception as e:
        print("website check failed", e)
        return False
    
def send_email(sender_email, password, receiver_email, subject, body):
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = receiver_email
    message['Subject'] = subject

    message.attach(MIMEText(body,'plain'))

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls() #start TLS encryption
        server.login(sender_email, password)
        text = message.as_string()
        server.sendmail(sender_email, receiver_email, text)
        print("Email sent Successfully")
    except Exception as e:
        print("Failed",e)

   
url = input(" Enter your url: ")

if not check_website(url):
    sender_email = os.getenv("SENDER_EMAIL")
    subject = "Website is not working"
    body = "The application is terminated"
    receiver_email = os.getenv("RECEIVE_EMAIL")
    password = os.getenv("APP_PASSWORD")
    send_email(sender_email, password, receiver_email, subject, body)

else: 
    print("The website is up")