import sys
import pandas as pd
import numpy as np


def get_emails(emails_path):
    print(f'Reading emails from {emails_path}.')

def send_emails(sender_email, sender_email_password, emails_path):
    emails_df = get_emails(emails_path)
    print(f'Using {sender_email} to send emails to {sender_email_password}, {emails_path}')

if __name__ == "__main__":
    sender_email = str(sys.argv[1])
    sender_email_password = str(sys.argv[2])
    emails_path = str(sys.argv[3])

    send_emails(sender_email, sender_email_password, emails_path)