import sys, smtplib, mimetypes
import pandas as pd
import numpy as np

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.message import EmailMessage

def login_user(email, password):
    smtp = smtplib.SMTP('smtp.gmail.com', 587)
    smtp.starttls()
    smtp.login(email, password)

def get_emails(emails_path):
    print(f'[.] Reading emails from {emails_path}.')
    emails = pd.read_csv(emails_path)

    print(f'[!] {len(emails.index)} emails read from {emails_path}.')

    return emails

def send_emails(sender_email, sender_email_password, emails_path, emails_col_name, names_col_name):
    login_user(sender_email, sender_email_password)
    print(f'[!] Logged in as {sender_email}.')
    
    emails_df = get_emails(emails_path)

    print(f'Using {sender_email} to send emails to {len(emails_df.index)} emails')

if __name__ == "__main__":
    sender_email = str(sys.argv[1])
    sender_email_password = str(sys.argv[2])
    emails_path = str(sys.argv[3])
    emails_col_name = str(sys.argv[4])
    names_col_name = str(sys.argv[5])

    send_emails(sender_email, sender_email_password, emails_path, emails_col_name, names_col_name)